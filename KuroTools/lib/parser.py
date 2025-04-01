from io import BufferedReader
import struct
from typing import Any, Literal, Tuple, Union
from ctypes import c_int32

def readint(
    stream: BufferedReader,
    size: int,
    endian: Literal["little", "big"] = "little",
    signed: bool = False,
) -> int:
    return int.from_bytes(stream.read(size), byteorder=endian, signed=signed)

def readintoffset(
    stream: BufferedReader,
    offset: int,
    size: int,
    endian: Literal["little", "big"] = "little",
    signed: bool = False,
) -> int:
    return_offset = stream.tell()
    stream.seek(offset)
    output = readint(stream, size, endian, signed)
    stream.seek(return_offset)
    return output


def readintoffset(
    stream: BufferedReader,
    offset: int,
    size: int,
    endian: Literal["little", "big"] = "little",
    signed: bool = False,
) -> int:
    return_offset = stream.tell()
    stream.seek(offset)
    output = readint(stream, size, endian, signed)
    stream.seek(return_offset)
    return output


def readfloat(stream: BufferedReader) -> float:
    return struct.unpack("<f", stream.read(4))[0]


def readtext(
    stream: BufferedReader, encoding: str = "utf-8", raw: bool = False
) -> str | bytes:
    output = b""
    char = stream.read(1)
    while char != b"\0":
        output += char
        char = stream.read(1)

    if raw:
        return output
    else:
        return output.decode(encoding)


def readtextoffset(stream: BufferedReader, offset: int, encoding: str = "utf-8") -> str:
    return_offset = stream.tell()
    stream.seek(offset)
    output = readtext(stream, raw=True)
    stream.seek(return_offset)
    return output.decode(encoding)


def process_number(
    stream: BufferedReader, datatype: str, signed: bool = False
) -> Tuple[Union[float, int], int]:
    int_size = {"byte": 1, "short": 2, "int": 4, "long": 8}
    if datatype in int_size:
        return readint(stream, int_size[datatype], signed=signed), int_size[datatype]
    else:
        return readfloat(stream), 4


def process_data(
    stream: BufferedReader, datatype: str | dict, max_length: int
) -> Tuple[Any, int]:
    processed = 0
     
    if isinstance(datatype, dict):
        data = []
        for _ in range(datatype["size"]):
            inner_data = {}
            for key, value in datatype["schema"].items():
                inner_value, data_processed = process_data(
                    stream, value, max_length - processed
                )
                inner_data[key] = inner_value
                processed += data_processed
            data.append(inner_data)
    elif datatype.startswith("data"):
        if len(datatype) <= 4:
            hex_text = stream.read(max_length - processed).hex()
        else:
            length = int(datatype[4:])
            hex_text = stream.read(length).hex()
            processed += length
        hex_text = " ".join(
            hex_text[j : j + 2] for j in range(0, len(hex_text), 2)
        ).upper()
        data = hex_text
    elif datatype.endswith(("byte", "short", "int", "long", "float")):
        if datatype.startswith("u"):
            data, data_processed = process_number(stream, datatype[1:], False)
        else:
            data, data_processed = process_number(stream, datatype, True)
        processed += data_processed
    elif datatype.startswith("toffset"):
        if datatype == "toffset":
            data = readtextoffset(stream, readint(stream, 8))
        else:
            data = readtextoffset(stream, readint(stream, 8), encoding=datatype[7:])
        processed += 8
    elif (datatype.startswith("u") and  datatype.endswith("array")):
        length = int(int(datatype[1:len(datatype)-5])/8)
        offset = readint(stream, 8)
        count = readint(stream, 4)
        data = [] 
        for i_usz in range(0, count):
            data.append(readintoffset(stream, offset + i_usz * length, length))
        processed += (8 + 4)
    else:
        raise Exception(f"Unknown data type {datatype}")

    return (data, processed)

def get_size_from_schema(
    schema : dict
) -> int:
    total_size = 0
    for key, value in schema["schema"].items():
        sz =  get_datatype_size(value)
        total_size += sz
    return total_size  

def get_datatype_size(
    datatype: str | dict
) -> int:
    sz = 0
    if isinstance(datatype, dict):
        for _ in range(datatype["size"]):
            for key, value in datatype["schema"].items():
                sz_processed =  get_datatype_size(value)
                sz += sz_processed
    elif datatype.startswith("data"):
        if len(datatype) <= 4:
            raise Exception("No size was defined for this datatype.")
        else:
            length = int(datatype[4:])
            sz += length
    elif datatype.endswith(("byte", "short", "int", "long", "float")):
        if datatype.startswith("u"):
            datatype = datatype[1:]
        sizes = {"byte": 1, "short": 2, "int": 4, "float": 4,  "long": 8}
        sz += sizes[datatype]
    elif datatype.startswith("toffset"):
        sz += 8
    elif (datatype.startswith("u") and  datatype.endswith("array")):
        sz += (8 + 4)
    else:
        raise Exception(f"Unknown data type {datatype}")

    return sz

def remove2MSB(value: int)->int:
    shl = value << 2 #I thought it would get rid of the 2 MSB, but it is working on a 64bits register!!!
    sar = c_int32(shl).value >> 2
    return sar #The fact that the last shift is arithmetic is important!! Otherwise wrong value for float and signed integer

def identifytype(value: int)->str:
    removeLSB = value & 0xC0000000
    MSB = removeLSB >> 0x1E

    if (MSB == 0):
        return "undefined"
    elif (MSB == 1):
        return "integer"
    elif (MSB == 2):
        return "float"
    elif (MSB == 3):
        return "string"


def get_actual_value_str(stream: BufferedReader, value: int)->str:
    removeLSB = value & 0xC0000000
    actual_value = remove2MSB(value)
    MSB = removeLSB >> 0x1E
    if (MSB == 3):
        text = readtextoffset(stream, actual_value)
        fixed_text = text.replace("\n", "\\n")
        return "\"" + fixed_text + "\""
    elif (MSB == 2):
        actual_value = actual_value << 2 #No right shift for the floats
        bytes = struct.pack("<i",actual_value)
        return str(struct.unpack("<f", bytes)[0])
    elif (MSB == 1):
        return str((int(actual_value)))
    else:
        return str(hex(int(actual_value)))

