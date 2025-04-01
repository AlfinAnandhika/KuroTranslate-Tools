# --- START OF FILE ED9InstructionsSet.py ---

import sys
import math # Добавлен импорт math для wrap_conversion
from lib.parser import readint, readintoffset, readtextoffset, remove2MSB, identifytype, get_actual_value_str
import struct # Добавлен импорт struct для wrap_conversion

#Note: All the pointers pushed to the stack have their pointers updated when recompiling (their position doesn't really matter)
#However all the code locations matter and need to be precisely updated to their new location, we do that by setting labels


def init_command_names_dicts():

    global commands_dict
    global reverse_commands_dict

    # Добавляем все известные и недостающие команды
    commands_dict= {
    # Категория 0 (System)
    (0, 0x00) : "Cmd_system_00", (0, 0x01) : "Cmd_system_01", (0, 0x02) : "Cmd_system_02", (0, 0x03) : "Cmd_system_03",
    (0, 0x04) : "Cmd_system_04", (0, 0x05) : "Cmd_system_05", (0, 0x06) : "Cmd_system_06", (0, 0x07) : "Cmd_system_07",
    (0, 0x08) : "Cmd_system_08", (0, 0x09) : "Cmd_system_09", (0, 0x0A) : "Cmd_system_0A", (0, 0x0B) : "Cmd_system_0B",
    (0, 0x0C) : "Cmd_system_0C", (0, 0x0D) : "Cmd_system_0D", (0, 0x0E) : "Cmd_system_0E", (0, 0x0F) : "Cmd_system_0F",
    (0, 0x10) : "Cmd_system_10", (0, 0x11) : "Cmd_system_11", (0, 0x12) : "Cmd_system_12", (0, 0x13) : "Cmd_system_13",
    (0, 0x14) : "Cmd_system_14", (0, 0x15) : "Cmd_system_15", (0, 0x16) : "Cmd_system_16", (0, 0x17) : "Cmd_system_17",
    (0, 0x18) : "Cmd_system_18", (0, 0x19) : "Cmd_system_19", (0, 0x1A) : "Cmd_system_1A", (0, 0x1B) : "Cmd_system_1B",
    (0, 0x1C) : "Cmd_system_1C", (0, 0x1D) : "Cmd_system_1D", (0, 0x1E) : "Cmd_system_1E", (0, 0x1F) : "Cmd_system_1F",
    (0, 0x20) : "Cmd_system_20", (0, 0x21) : "Cmd_system_21", (0, 0x22) : "Cmd_system_22", (0, 0x23) : "Cmd_system_23",
    (0, 0x24) : "Cmd_system_24", (0, 0x25) : "Cmd_system_25", (0, 0x26) : "Cmd_system_26", (0, 0x27) : "Cmd_system_27",
    (0, 0x28) : "Cmd_system_28", (0, 0x29) : "Cmd_system_29", (0, 0x2A) : "Cmd_system_2A", (0, 0x2B) : "Cmd_system_2B",
    (0, 0x2C) : "Cmd_system_2C", (0, 0x2D) : "Cmd_system_2D", (0, 0x2E) : "Cmd_system_2E", (0, 0x2F) : "Cmd_system_2F",
    (0, 0x30) : "Cmd_system_30", (0, 0x31) : "Cmd_system_31", (0, 0x32) : "Cmd_system_32", (0, 0x33) : "Cmd_system_33",
    (0, 0x34) : "Cmd_system_34", (0, 0x35) : "Cmd_system_35", (0, 0x36) : "Cmd_system_36", (0, 0x37) : "Cmd_system_37",
    (0, 0x39) : "Cmd_system_39", (0, 0x3A) : "Cmd_system_3A", (0, 0x3B) : "Cmd_system_3B", (0, 0x3C) : "Cmd_system_3C",
    (0, 0x3E) : "Cmd_system_3E", (0, 0x3F) : "Cmd_system_3F", (0, 0x40) : "Cmd_system_40", (0, 0x41) : "Cmd_system_41",
    (0, 0x42) : "Cmd_system_42", (0, 0x43) : "Cmd_system_43", (0, 0x44) : "Cmd_system_44", (0, 0x45) : "Cmd_system_45",
    (0, 0x46) : "Cmd_system_46", (0, 0x47) : "Cmd_system_47", (0, 0x48) : "Cmd_system_48", (0, 0x49) : "Cmd_system_49",
    (0, 0x4A) : "Cmd_system_4A", (0, 0x4B) : "Cmd_system_4B", (0, 0x4C) : "Cmd_system_4C", (0, 0x4D) : "Cmd_system_4D",
    (0, 0x4E) : "Cmd_system_4E", (0, 0x4F) : "Cmd_system_4F", (0, 0x50) : "Cmd_system_50", (0, 0x51) : "Cmd_system_51",
    (0, 0x52) : "Cmd_system_52", (0, 0x53) : "Cmd_system_53", (0, 0x54) : "Cmd_system_54", (0, 0x55) : "Cmd_system_55",
    (0, 0x56) : "Cmd_system_56", (0, 0x57) : "Cmd_system_57", (0, 0x58) : "Cmd_system_58", (0, 0x59) : "Cmd_system_59",
    (0, 0x5A) : "Cmd_system_5A", (0, 0x5B) : "Cmd_system_5B", (0, 0x5C) : "Cmd_system_5C", (0, 0x5D) : "Cmd_system_5D",
    (0, 0x5E) : "Cmd_system_5E", (0, 0x5F) : "Cmd_system_5F", (0, 0x60) : "Cmd_system_60", (0, 0x61) : "Cmd_system_61",
    (0, 0x62) : "Cmd_system_62", (0, 0x63) : "Cmd_system_63", (0, 0x64) : "Cmd_system_64", (0, 0x65) : "Cmd_system_65",
    (0, 0x66) : "Cmd_system_66", (0, 0x67) : "Cmd_system_67", (0, 0x68) : "Cmd_system_68", (0, 0x69) : "Cmd_system_69",
    (0, 0x6A) : "Cmd_system_6A", (0, 0x6B) : "Cmd_system_6B", (0, 0x6C) : "Cmd_system_6C", (0, 0x6D) : "Cmd_system_6D",
    (0, 0x6E) : "Cmd_system_6E", (0, 0x6F) : "Cmd_system_6F", (0, 0x70) : "Cmd_system_70", (0, 0x71) : "Cmd_system_71",
    (0, 0x72) : "Cmd_system_72", (0, 0x73) : "Cmd_system_73", (0, 0x74) : "Cmd_system_74", (0, 0x75) : "Cmd_system_75",
    (0, 0x76) : "Cmd_system_76", (0, 0x77) : "Cmd_system_77", (0, 0x78) : "Cmd_system_78", (0, 0x79) : "Cmd_system_79",
    (0, 0x7A) : "Cmd_system_7A", (0, 0x7B) : "Cmd_system_7B", (0, 0x7C) : "Cmd_system_7C", (0, 0x7D) : "Cmd_system_7D",
    (0, 0x7E) : "Cmd_system_7E", (0, 0x7F) : "Cmd_system_7F", (0, 0x80) : "Cmd_system_80", (0, 0x81) : "Cmd_system_81",
    (0, 0x82) : "Cmd_system_82", (0, 0x83) : "Cmd_system_83", (0, 0x84) : "Cmd_system_84", (0, 0x85) : "Cmd_system_85",
    (0, 0x86) : "Cmd_system_86", (0, 0x87) : "Cmd_system_87", (0, 0x88) : "Cmd_system_88", (0, 0x89) : "Cmd_system_89",
    (0, 0x8A) : "Cmd_system_8A", (0, 0x8B) : "Cmd_system_8B", (0, 0x8C) : "Cmd_system_8C", (0, 0x8D) : "Cmd_system_8D",
    (0, 0x8E) : "Cmd_system_8E", (0, 0x8F) : "Cmd_system_8F", (0, 0x90) : "Cmd_system_90", (0, 0x92) : "Cmd_system_92",
    (0, 0x93) : "Cmd_system_93", (0, 0x94) : "Cmd_system_94", (0, 0x95) : "Cmd_system_95", (0, 0x96) : "Cmd_system_96",
    (0, 0x97) : "Cmd_system_97", (0, 0x98) : "Cmd_system_98", (0, 0x99) : "Cmd_system_99", (0, 0x9A) : "Cmd_system_9A",
    (0, 0x9B) : "Cmd_system_9B", (0, 0x9C) : "Cmd_system_9C", (0, 0x9D) : "Cmd_system_9D", (0, 0x9E) : "Cmd_system_9E",
    (0, 0x9F) : "Cmd_system_9F", (0, 0xA0) : "Cmd_system_A0", (0, 0xA1) : "Cmd_system_A1", (0, 0xA2) : "Cmd_system_A2",
    (0, 0xA3) : "Cmd_system_A3", (0, 0xA4) : "Cmd_system_A4", (0, 0xA5) : "Cmd_system_A5", (0, 0xA6) : "Cmd_system_A6",
    (0, 0xA7) : "Cmd_system_A7", (0, 0xA8) : "Cmd_system_A8", (0, 0xA9) : "Cmd_system_A9", (0, 0xAA) : "Cmd_system_AA",
    (0, 0xAB) : "Cmd_system_AB", (0, 0xAC) : "Cmd_system_AC", (0, 0xAD) : "Cmd_system_AD", (0, 0xAE) : "Cmd_system_AE",
    (0, 0xAF) : "Cmd_system_AF", (0, 0xB0) : "Cmd_system_B0", (0, 0xB1) : "Cmd_system_B1", (0, 0xB2) : "Cmd_system_B2",
    (0, 0xB3) : "Cmd_system_B3", (0, 0xB4) : "Cmd_system_B4", (0, 0xB5) : "Cmd_system_B5", (0, 0xB6) : "Cmd_system_B6",
    (0, 0xB7) : "Cmd_system_B7", (0, 0xB8) : "Cmd_system_B8", (0, 0xB9) : "Cmd_system_B9", (0, 0xBA) : "Cmd_system_BA",
    (0, 0xBB) : "Cmd_system_BB", (0, 0xBC) : "Cmd_system_BC", (0, 0xBD) : "Cmd_system_BD", (0, 0xBE) : "Cmd_system_BE",
    (0, 0xBF) : "Cmd_system_BF", (0, 0xC0) : "Cmd_system_C0", (0, 0xC1) : "Cmd_system_C1", (0, 0xC2) : "Cmd_system_C2",
    (0, 0xC3) : "Cmd_system_C3", (0, 0xC4) : "Cmd_system_C4", (0, 0xC5) : "Cmd_system_C5", (0, 0xC6) : "Cmd_system_C6",
    (0, 0xC7) : "Cmd_system_C7", (0, 0xC8) : "Cmd_system_C8", (0, 0xC9) : "Cmd_system_C9", (0, 0xCA) : "Cmd_system_CA",
    (0, 0xCB) : "Cmd_system_CB", (0, 0xCC) : "Cmd_system_CC", (0, 0xCD) : "Cmd_system_CD", (0, 0xCE) : "Cmd_system_CE",
    (0, 0xCF) : "Cmd_system_CF", (0, 0xD0) : "Cmd_system_D0", (0, 0xD1) : "Cmd_system_D1", (0, 0xD2) : "Cmd_system_D2",
    (0, 0xD3) : "Cmd_system_D3", (0, 0xD4) : "Cmd_system_D4", (0, 0xD5) : "Cmd_system_D5", (0, 0xD6) : "Cmd_system_D6",
    (0, 0xD7) : "Cmd_system_D7", (0, 0xD8) : "Cmd_system_D8", (0, 0xD9) : "Cmd_system_D9", (0, 0xDA) : "Cmd_system_DA",
    (0, 0xDB) : "Cmd_system_DB", (0, 0xDC) : "Cmd_system_DC", (0, 0xDD) : "Cmd_system_DD", (0, 0xDE) : "Cmd_system_DE",
    (0, 0xDF) : "Cmd_system_DF", (0, 0xE0) : "Cmd_system_E0", (0, 0xE1) : "Cmd_system_E1", (0, 0xE2) : "Cmd_system_E2",
    (0, 0xE3) : "Cmd_system_E3", (0, 0xE4) : "Cmd_system_E4", (0, 0xE5) : "Cmd_system_E5", (0, 0xE6) : "Cmd_system_E6",
    (0, 0xE7) : "Cmd_system_E7", (0, 0xE8) : "Cmd_system_E8", (0, 0xE9) : "Cmd_system_E9", (0, 0xEA) : "Cmd_system_EA",
    (0, 0xEB) : "Cmd_system_EB", (0, 0xEC) : "Cmd_system_EC", (0, 0xED) : "Cmd_system_ED", (0, 0xEE) : "Cmd_system_EE",
    (0, 0xEF) : "Cmd_system_EF", (0, 0xF0) : "Cmd_system_F0", (0, 0xF1) : "Cmd_system_F1", (0, 0xF2) : "Cmd_system_F2",
    (0, 0xF3) : "Cmd_system_F3", (0, 0xF4) : "Cmd_system_F4", (0, 0xF5) : "Cmd_system_F5", (0, 0xF6) : "Cmd_system_F6",
    (0, 0xF7) : "Cmd_system_F7", (0, 0xF8) : "Cmd_system_F8", (0, 0xF9) : "Cmd_system_F9",

    # Категория 1 (Characters)
    (1, 0x00) : "Cmd_characters_00", (1, 0x01) : "Cmd_characters_01", (1, 0x02) : "Cmd_characters_02", (1, 0x03) : "Cmd_characters_03",
    (1, 0x04) : "Cmd_characters_04", (1, 0x05) : "Cmd_characters_05", (1, 0x06) : "Cmd_characters_06", (1, 0x07) : "Cmd_characters_07",
    (1, 0x08) : "Cmd_characters_08", (1, 0x09) : "Cmd_characters_09", (1, 0x0A) : "Cmd_characters_0A", (1, 0x0B) : "Cmd_characters_0B",
    (1, 0x0C) : "Cmd_characters_0C", (1, 0x0D) : "Cmd_characters_0D", (1, 0x0E) : "Cmd_characters_0E", (1, 0x0F) : "Cmd_characters_0F",
    (1, 0x10) : "Cmd_characters_10", (1, 0x11) : "Cmd_characters_11", (1, 0x12) : "Cmd_characters_12", (1, 0x13) : "Cmd_characters_13",
    (1, 0x14) : "Cmd_characters_14", (1, 0x15) : "Cmd_characters_15", (1, 0x16) : "Cmd_characters_16", (1, 0x17) : "Cmd_characters_17",
    (1, 0x18) : "Cmd_characters_18", (1, 0x19) : "Cmd_characters_19", (1, 0x1A) : "Cmd_characters_1A", (1, 0x1B) : "Cmd_characters_1B",
    (1, 0x1C) : "Cmd_characters_1C", (1, 0x1D) : "Cmd_characters_1D", (1, 0x1E) : "Cmd_characters_1E", (1, 0x1F) : "Cmd_characters_1F",
    (1, 0x20) : "Cmd_characters_20", (1, 0x21) : "Cmd_characters_21", (1, 0x22) : "Cmd_characters_22", (1, 0x23) : "Cmd_characters_23",
    (1, 0x24) : "Cmd_characters_24", (1, 0x25) : "Cmd_characters_25", (1, 0x26) : "Cmd_characters_26", (1, 0x27) : "Cmd_characters_27",
    (1, 0x28) : "Cmd_characters_28", (1, 0x29) : "Cmd_characters_29", (1, 0x2A) : "Cmd_characters_2A", (1, 0x2B) : "Cmd_characters_2B",
    (1, 0x2C) : "Cmd_characters_2C", (1, 0x2D) : "Cmd_characters_2D", (1, 0x2E) : "Cmd_characters_2E", (1, 0x2F) : "SetAnimation",
    (1, 0x30) : "Cmd_characters_30", (1, 0x31) : "Cmd_characters_31", (1, 0x32) : "Cmd_characters_32", (1, 0x33) : "Cmd_characters_33",
    (1, 0x34) : "Cmd_characters_34", (1, 0x35) : "Cmd_characters_35", (1, 0x36) : "Cmd_characters_36", (1, 0x37) : "Cmd_characters_37",
    (1, 0x38) : "Cmd_characters_38", (1, 0x39) : "Cmd_characters_39", (1, 0x3A) : "Cmd_characters_3A", (1, 0x3B) : "Cmd_characters_3B",
    (1, 0x3C) : "Cmd_characters_3C", (1, 0x3D) : "Cmd_characters_3D", (1, 0x3E) : "Cmd_characters_3E", (1, 0x3F) : "Cmd_characters_3F",
    (1, 0x40) : "Cmd_characters_40", (1, 0x41) : "Cmd_characters_41", (1, 0x42) : "Cmd_characters_42", (1, 0x43) : "Cmd_characters_43",
    (1, 0x44) : "Cmd_characters_44", (1, 0x45) : "Cmd_characters_45", (1, 0x46) : "Cmd_characters_46", (1, 0x47) : "Cmd_characters_47",
    (1, 0x48) : "Cmd_characters_48", (1, 0x49) : "Cmd_characters_49", (1, 0x4A) : "Cmd_characters_4A", (1, 0x4B) : "Cmd_characters_4B",
    (1, 0x4C) : "Cmd_characters_4C", (1, 0x4D) : "Cmd_characters_4D", (1, 0x4E) : "Cmd_characters_4E", (1, 0x4F) : "Cmd_characters_4F",
    (1, 0x50) : "Cmd_characters_50", (1, 0x51) : "Cmd_characters_51", (1, 0x52) : "Cmd_characters_52", (1, 0x53) : "Cmd_characters_53",
    (1, 0x54) : "Cmd_characters_54", (1, 0x55) : "Cmd_characters_55", (1, 0x56) : "Cmd_characters_56", (1, 0x57) : "Cmd_characters_57",
    (1, 0x58) : "Cmd_characters_58", (1, 0x59) : "Cmd_characters_59", (1, 0x5A) : "Cmd_characters_5A", (1, 0x5B) : "Cmd_characters_5B",
    (1, 0x5C) : "Cmd_characters_5C", (1, 0x5D) : "Cmd_characters_5D", (1, 0x5E) : "Cmd_characters_5E", (1, 0x5F) : "Cmd_characters_5F",
    (1, 0x60) : "Cmd_characters_60", (1, 0x61) : "Cmd_characters_61", (1, 0x62) : "Cmd_characters_62", (1, 0x63) : "Cmd_characters_63",
    (1, 0x64) : "Cmd_characters_64", (1, 0x65) : "Cmd_characters_65", (1, 0x66) : "Cmd_characters_66", (1, 0x67) : "Cmd_characters_67",
    (1, 0x68) : "Cmd_characters_68", (1, 0x69) : "Cmd_characters_69", (1, 0x6A) : "Cmd_characters_6A", (1, 0x6B) : "Cmd_characters_6B",
    (1, 0x6C) : "Cmd_characters_6C", (1, 0x6D) : "Cmd_characters_6D", (1, 0x6E) : "Cmd_characters_6E", (1, 0x6F) : "Cmd_characters_6F",
    (1, 0x70) : "Cmd_characters_70", (1, 0x71) : "Cmd_characters_71", (1, 0x72) : "Cmd_characters_72", (1, 0x73) : "Cmd_characters_73",
    (1, 0x74) : "Cmd_characters_74", (1, 0x75) : "Cmd_characters_75", (1, 0x76) : "Cmd_characters_76", (1, 0x77) : "Cmd_characters_77",
    (1, 0x78) : "Cmd_characters_78", (1, 0x79) : "Cmd_characters_79", (1, 0x7A) : "Cmd_characters_7A", (1, 0x7B) : "Cmd_characters_7B",
    (1, 0x7C) : "Cmd_characters_7C", (1, 0x7D) : "Cmd_characters_7D", (1, 0x7E) : "Cmd_characters_7E", (1, 0x7F) : "Cmd_characters_7F",
    (1, 0x80) : "Cmd_characters_80", (1, 0x81) : "Cmd_characters_81", (1, 0x82) : "Cmd_characters_82", (1, 0x83) : "Cmd_characters_83",
    (1, 0x84) : "Cmd_characters_84", (1, 0x85) : "Cmd_characters_85", (1, 0x86) : "Cmd_characters_86", (1, 0x87) : "Cmd_characters_87",
    (1, 0x88) : "Cmd_characters_88", (1, 0x89) : "Cmd_characters_89", (1, 0x8A) : "Cmd_characters_8A", (1, 0x8B) : "Cmd_characters_8B",
    (1, 0x8C) : "Cmd_characters_8C", (1, 0x8D) : "Cmd_characters_8D", (1, 0x8E) : "Cmd_characters_8E", (1, 0x8F) : "Cmd_characters_8F",
    (1, 0x90) : "Cmd_characters_90", (1, 0x91) : "Cmd_characters_91", (1, 0x92) : "Cmd_characters_92", (1, 0x93) : "Cmd_characters_93",
    (1, 0x94) : "Cmd_characters_94", (1, 0x95) : "Cmd_characters_95", (1, 0x96) : "Cmd_characters_96", (1, 0x97) : "Cmd_characters_97",
    (1, 0x98) : "Cmd_characters_98", (1, 0x99) : "Cmd_characters_99", (1, 0x9A) : "Cmd_characters_9A", (1, 0x9B) : "Cmd_characters_9B",
    (1, 0x9C) : "Cmd_characters_9C", (1, 0x9D) : "Cmd_characters_9D", (1, 0x9E) : "Cmd_characters_9E", (1, 0x9F) : "Cmd_characters_9F",
    (1, 0xA0) : "Cmd_characters_A0", (1, 0xA1) : "Cmd_characters_A1", (1, 0xA2) : "Cmd_characters_A2", (1, 0xA3) : "Cmd_characters_A3",
    (1, 0xA4) : "Cmd_characters_A4", (1, 0xA5) : "Cmd_characters_A5", (1, 0xA6) : "Cmd_characters_A6", (1, 0xA7) : "Cmd_characters_A7",
    (1, 0xA8) : "Cmd_characters_A8", (1, 0xA9) : "Cmd_characters_A9", (1, 0xAA) : "Cmd_characters_AA", (1, 0xAB) : "Cmd_characters_AB",
    (1, 0xAC) : "Cmd_characters_AC", (1, 0xAD) : "Cmd_characters_AD", (1, 0xAE) : "Cmd_characters_AE", (1, 0xAF) : "Cmd_characters_AF",
    (1, 0xB0) : "Cmd_characters_B0", (1, 0xB1) : "Cmd_characters_B1", (1, 0xB2) : "Cmd_characters_B2", (1, 0xB3) : "Cmd_characters_B3",
    (1, 0xB4) : "Cmd_characters_B4", (1, 0xB5) : "Cmd_characters_B5", (1, 0xB6) : "Cmd_characters_B6", (1, 0xB7) : "Cmd_characters_B7",
    (1, 0xB8) : "Cmd_characters_B8", (1, 0xB9) : "Cmd_characters_B9", (1, 0xBA) : "Cmd_characters_BA", (1, 0xBB) : "Cmd_characters_BB",
    (1, 0xBC) : "Cmd_characters_BC", (1, 0xBD) : "Cmd_characters_BD", (1, 0xBE) : "Cmd_characters_BE", (1, 0xBF) : "Cmd_characters_BF",
    (1, 0xC0) : "Cmd_characters_C0", (1, 0xC1) : "Cmd_characters_C1", (1, 0xC2) : "Cmd_characters_C2", (1, 0xC3) : "Cmd_characters_C3",
    (1, 0xC4) : "Cmd_characters_C4", (1, 0xC5) : "Cmd_characters_C5", (1, 0xC6) : "Cmd_characters_C6", (1, 0xC7) : "Cmd_characters_C7",
    (1, 0xC8) : "Cmd_characters_C8", (1, 0xC9) : "Cmd_characters_C9", (1, 0xCA) : "Cmd_characters_CA", (1, 0xCB) : "Cmd_characters_CB",
    (1, 0xCC) : "Cmd_characters_CC", (1, 0xCD) : "Cmd_characters_CD", (1, 0xCE) : "Cmd_characters_CE", (1, 0xCF) : "Cmd_characters_CF",
    (1, 0xD0) : "Cmd_characters_D0", (1, 0xD1) : "Cmd_characters_D1", (1, 0xD2) : "Cmd_characters_D2", (1, 0xD3) : "Cmd_characters_D3",
    (1, 0xD4) : "Cmd_characters_D4", (1, 0xD5) : "Cmd_characters_D5", (1, 0xD6) : "Cmd_characters_D6", (1, 0xD7) : "Cmd_characters_D7",
    (1, 0xD8) : "Cmd_characters_D8", (1, 0xD9) : "Cmd_characters_D9", (1, 0xDA) : "Cmd_characters_DA", (1, 0xDB) : "Cmd_characters_DB",
    (1, 0xDC) : "Cmd_characters_DC", (1, 0xDD) : "Cmd_characters_DD", (1, 0xDE) : "Cmd_characters_DE", (1, 0xDF) : "Cmd_characters_DF",
    (1, 0xE0) : "Cmd_characters_E0", (1, 0xE1) : "Cmd_characters_E1",

    # Категория 2 (Camera)
    (2, 0x00) : "Cmd_camera_00", (2, 0x01) : "Cmd_camera_01", (2, 0x02) : "Cmd_camera_02", (2, 0x03) : "Cmd_camera_03",
    (2, 0x04) : "Cmd_camera_04", (2, 0x05) : "Cmd_camera_05", (2, 0x06) : "Cmd_camera_06", (2, 0x07) : "Cmd_camera_07",
    (2, 0x08) : "Cmd_camera_08", (2, 0x09) : "Cmd_camera_09", (2, 0x0A) : "Cmd_camera_0A", (2, 0x0B) : "Cmd_camera_0B",
    (2, 0x0C) : "Cmd_camera_0C", (2, 0x0D) : "Cmd_camera_0D", (2, 0x0E) : "Cmd_camera_0E", (2, 0x0F) : "Cmd_camera_0F",
    (2, 0x10) : "Cmd_camera_10", (2, 0x11) : "Cmd_camera_11", (2, 0x12) : "Cmd_camera_12", (2, 0x13) : "Cmd_camera_13",
    (2, 0x14) : "Cmd_camera_14", (2, 0x15) : "Cmd_camera_15", (2, 0x16) : "Cmd_camera_16", (2, 0x17) : "Cmd_camera_17",
    (2, 0x18) : "Cmd_camera_18", (2, 0x19) : "Cmd_camera_19", (2, 0x1A) : "Cmd_camera_1A", (2, 0x1B) : "Cmd_camera_1B",
    (2, 0x1C) : "Cmd_camera_1C", (2, 0x1D) : "Cmd_camera_1D", (2, 0x1E) : "Cmd_camera_1E", (2, 0x1F) : "Cmd_camera_1F",
    (2, 0x20) : "Cmd_camera_20", (2, 0x21) : "Cmd_camera_21", (2, 0x22) : "Cmd_camera_22", (2, 0x23) : "Cmd_camera_23",
    (2, 0x24) : "Cmd_camera_24", (2, 0x25) : "Cmd_camera_25", (2, 0x26) : "Cmd_camera_26", (2, 0x27) : "Cmd_camera_27",
    (2, 0x28) : "Cmd_camera_28", (2, 0x29) : "Cmd_camera_29", (2, 0x2A) : "Cmd_camera_2A", (2, 0x2B) : "Cmd_camera_2B",
    (2, 0x2C) : "Cmd_camera_2C", (2, 0x2D) : "Cmd_camera_2D", (2, 0x2E) : "Cmd_camera_2E", (2, 0x2F) : "Cmd_camera_2F",
    (2, 0x30) : "Cmd_camera_30", (2, 0x31) : "Cmd_camera_31", (2, 0x32) : "Cmd_camera_32", (2, 0x33) : "Cmd_camera_33",
    (2, 0x34) : "Cmd_camera_34", (2, 0x35) : "Cmd_camera_35", (2, 0x36) : "Cmd_camera_36", (2, 0x37) : "Cmd_camera_37",
    (2, 0x38) : "Cmd_camera_38", (2, 0x39) : "Cmd_camera_39", (2, 0x3A) : "Cmd_camera_3A", (2, 0x3B) : "Cmd_camera_3B",
    (2, 0x3C) : "Cmd_camera_3C", (2, 0x3D) : "Cmd_camera_3D", (2, 0x3E) : "Cmd_camera_3E", (2, 0x3F) : "Cmd_camera_3F",
    (2, 0x40) : "Cmd_camera_40", (2, 0x41) : "Cmd_camera_41",

    # Категория 3 (Event)
    (3, 0x00) : "Cmd_event_00", (3, 0x01) : "Cmd_event_01", (3, 0x02) : "Cmd_event_02", (3, 0x03) : "Cmd_event_03",
    (3, 0x04) : "Cmd_event_04", (3, 0x05) : "Cmd_event_05", (3, 0x06) : "Cmd_event_06", (3, 0x07) : "Cmd_event_07",
    (3, 0x08) : "Cmd_event_08", (3, 0x09) : "Cmd_event_09", (3, 0x0A) : "Cmd_event_0A", (3, 0x0B) : "Cmd_event_0B",
    (3, 0x0C) : "Cmd_event_0C", (3, 0x0D) : "Cmd_event_0D", (3, 0x0E) : "Cmd_event_0E", (3, 0x0F) : "Cmd_event_0F",
    (3, 0x10) : "Cmd_event_10", (3, 0x11) : "Cmd_event_11", (3, 0x12) : "Cmd_event_12", (3, 0x13) : "Cmd_event_13",
    (3, 0x14) : "Cmd_event_14", (3, 0x15) : "Cmd_event_15", (3, 0x16) : "Cmd_event_16", (3, 0x17) : "Cmd_event_17",
    (3, 0x18) : "Cmd_event_18", (3, 0x19) : "Cmd_event_19", (3, 0x1A) : "Cmd_event_1A", (3, 0x1B) : "Cmd_event_1B",
    (3, 0x1C) : "Cmd_event_1C", (3, 0x1D) : "Cmd_event_1D", (3, 0x1E) : "Cmd_event_1E", (3, 0x1F) : "Cmd_event_1F",
    (3, 0x20) : "Cmd_event_20", (3, 0x21) : "Cmd_event_21", (3, 0x22) : "Cmd_event_22", (3, 0x23) : "Cmd_event_23",
    (3, 0x24) : "Cmd_event_24", (3, 0x25) : "Cmd_event_25", (3, 0x26) : "Cmd_event_26", (3, 0x27) : "Cmd_event_27",
    (3, 0x28) : "Cmd_event_28", (3, 0x29) : "Cmd_event_29", (3, 0x2A) : "Cmd_event_2A", (3, 0x2B) : "Cmd_event_2B",
    (3, 0x2C) : "Cmd_event_2C", (3, 0x2D) : "Cmd_event_2D", (3, 0x2E) : "Cmd_event_2E", (3, 0x2F) : "Cmd_event_2F",
    (3, 0x30) : "Cmd_event_30", (3, 0x31) : "Cmd_event_31", (3, 0x32) : "Cmd_event_32", (3, 0x33) : "Cmd_event_33",
    (3, 0x34) : "Cmd_event_34", (3, 0x35) : "Cmd_event_35", (3, 0x36) : "Cmd_event_36", (3, 0x37) : "Cmd_event_37",
    (3, 0x38) : "Cmd_event_38", (3, 0x39) : "Cmd_event_39", (3, 0x3A) : "Cmd_event_3A", (3, 0x3B) : "Cmd_event_3B",
    (3, 0x3C) : "Cmd_event_3C", (3, 0x3D) : "Cmd_event_3D", (3, 0x3E) : "Cmd_event_3E", (3, 0x3F) : "Cmd_event_3F",
    (3, 0x40) : "Cmd_event_40", (3, 0x41) : "Cmd_event_41", (3, 0x42) : "Cmd_event_42", (3, 0x43) : "Cmd_event_43",
    (3, 0x44) : "Cmd_event_44", (3, 0x45) : "Cmd_event_45", (3, 0x46) : "Cmd_event_46", (3, 0x47) : "Cmd_event_47",
    (3, 0x48) : "Cmd_event_48", (3, 0x49) : "Cmd_event_49", (3, 0x4A) : "Cmd_event_4A", (3, 0x4B) : "Cmd_event_4B",
    (3, 0x4C) : "Cmd_event_4C", (3, 0x4D) : "Cmd_event_4D",

    # Категория 4 (Unknown_1)
    (4, 0x00) : "Cmd_unknown_1_00", (4, 0x01) : "Cmd_unknown_1_event_01", (4, 0x02) : "Cmd_unknown_1_event_02",
    (4, 0x03) : "Cmd_unknown_1_event_03", (4, 0x04) : "Cmd_unknown_1_event_04", (4, 0x05) : "Cmd_unknown_1_event_05",
    (4, 0x06) : "Cmd_unknown_1_event_06",

    # Категория 5 (Text)
    (5, 0x00) : "Cmd_text_00", (5, 0x01) : "Cmd_text_01", (5, 0x02) : "Cmd_text_02", (5, 0x03) : "Cmd_text_03",
    (5, 0x04) : "Cmd_text_04", (5, 0x05) : "Cmd_text_05", (5, 0x06) : "Cmd_text_06", (5, 0x07) : "Cmd_text_07",
    (5, 0x08) : "Cmd_text_08", (5, 0x09) : "Cmd_text_09", (5, 0x0A) : "Cmd_text_0A", (5, 0x0B) : "Cmd_text_0B",
    (5, 0x0C) : "Cmd_text_0C", (5, 0x0D) : "Cmd_text_0D", (5, 0x0E) : "Cmd_text_0E", (5, 0x0F) : "Cmd_text_0F",
    (5, 0x10) : "Cmd_text_10", (5, 0x11) : "Cmd_text_11", (5, 0x12) : "Cmd_text_12", (5, 0x13) : "Cmd_text_13",
    (5, 0x14) : "Cmd_text_14", (5, 0x15) : "Cmd_text_15", (5, 0x16) : "Cmd_text_16", (5, 0x17) : "Cmd_text_17",
    (5, 0x18) : "Cmd_text_18", (5, 0x19) : "Cmd_text_19", (5, 0x1A) : "Cmd_text_1A", (5, 0x1B) : "Cmd_text_1B",
    (5, 0x1C) : "Cmd_text_1C", (5, 0x1D) : "Cmd_text_1D", (5, 0x1E) : "Cmd_text_1E", (5, 0x1F) : "Cmd_text_1F",
    (5, 0x20) : "Cmd_text_20", (5, 0x21) : "Cmd_text_21",

    # Категория 6 (Sound)
    (6, 0x00) : "Cmd_sound_00", (6, 0x01) : "Cmd_sound_01", (6, 0x02) : "Cmd_sound_02", (6, 0x03) : "Cmd_sound_03",
    (6, 0x04) : "Cmd_sound_04", (6, 0x05) : "Cmd_sound_05", (6, 0x06) : "Cmd_sound_06", (6, 0x07) : "Cmd_sound_07",
    (6, 0x08) : "Cmd_sound_08", (6, 0x09) : "Cmd_sound_09", (6, 0x0A) : "Cmd_sound_0A", (6, 0x0B) : "Cmd_sound_0B",
    (6, 0x0C) : "Cmd_sound_0C", (6, 0x0D) : "Cmd_sound_0D", (6, 0x0E) : "Cmd_sound_0E", (6, 0x0F) : "Cmd_sound_0F",
    (6, 0x10) : "Cmd_sound_10", (6, 0x11) : "Cmd_sound_11", (6, 0x12) : "Cmd_sound_12", (6, 0x13) : "Cmd_sound_13",
    (6, 0x14) : "Cmd_sound_14", (6, 0x15) : "Cmd_sound_15", (6, 0x16) : "Cmd_sound_16", (6, 0x17) : "Cmd_sound_17",
    (6, 0x18) : "Cmd_sound_18", (6, 0x19) : "Cmd_sound_19", (6, 0x1A) : "Cmd_sound_1A", (6, 0x1B) : "Cmd_sound_1B",
    (6, 0x1C) : "Cmd_sound_1C", (6, 0x1D) : "Cmd_sound_1D", (6, 0x1E) : "Cmd_sound_1E", (6, 0x1F) : "Cmd_sound_1F",
    (6, 0x20) : "Cmd_sound_20", (6, 0x21) : "Cmd_sound_21", (6, 0x22) : "Cmd_sound_22", (6, 0x23) : "Cmd_sound_23",
    (6, 0x24) : "Cmd_sound_24", (6, 0x25) : "Cmd_sound_25", (6, 0x26) : "Cmd_sound_26", (6, 0x27) : "Cmd_sound_27",
    (6, 0x28) : "Cmd_sound_28", (6, 0x29) : "Cmd_sound_29", (6, 0x2A) : "Cmd_sound_2A", (6, 0x2B) : "Cmd_sound_2B",
    (6, 0x2C) : "Cmd_sound_2C",

    # Категория 7 (Unknown_2)
    (7, 0x00) : "Cmd_unknown_2_00",

    # Категория 8 (Movies)
    (8, 0x00) : "Cmd_movies_00", (8, 0x01) : "Cmd_movies_01", (8, 0x02) : "Cmd_movies_02", (8, 0x03) : "Cmd_movies_03",

    # Категория 9 (Unknown_3)
    (9, 0x00) : "Cmd_unknown_3_00",

    # Категория 10 (Unknown_4)
    (10, 0x00) : "Cmd_unknown_4_00", (10, 0x01) : "Cmd_unknown_4_01", (10, 0x02) : "Cmd_unknown_4_02",
    (10, 0x03) : "Cmd_unknown_4_03", (10, 0x04) : "Cmd_unknown_4_04", (10, 0x05) : "Cmd_unknown_4_05",
    (10, 0x06) : "Cmd_unknown_4_06", (10, 0x07) : "Cmd_unknown_4_07", (10, 0x08) : "Cmd_unknown_4_08",
    (10, 0x09) : "Cmd_unknown_4_09", (10, 0x0A) : "Cmd_unknown_4_0A", (10, 0x0B) : "Cmd_unknown_4_0B",
    (10, 0x0C) : "Cmd_unknown_4_0C", (10, 0x0D) : "Cmd_unknown_4_0D", (10, 0x0E) : "Cmd_unknown_4_0E",
    (10, 0x0F) : "Cmd_unknown_4_0F", (10, 0x10) : "Cmd_unknown_4_10",

    # Категория 0xB (11) (Map)
    (0xB, 0x00) : "Cmd_map_00", (0xB, 0x01) : "Cmd_map_01", (0xB, 0x02) : "Cmd_map_02", (0xB, 0x03) : "Cmd_map_03",
    (0xB, 0x04) : "Cmd_map_04", (0xB, 0x05) : "Cmd_map_05", (0xB, 0x06) : "Cmd_map_06", (0xB, 0x07) : "Cmd_map_07",
    (0xB, 0x08) : "Cmd_map_08", (0xB, 0x09) : "Cmd_map_09", (0xB, 0x0A) : "Cmd_map_0A", (0xB, 0x0B) : "Cmd_map_0B",
    (0xB, 0x0C) : "Cmd_map_0C", (0xB, 0x0D) : "Cmd_map_0D", (0xB, 0x0E) : "Cmd_map_0E", (0xB, 0x0F) : "Cmd_map_0F",
    (0xB, 0x10) : "Cmd_map_10", (0xB, 0x11) : "Cmd_map_11", (0xB, 0x12) : "Cmd_map_12", (0xB, 0x13) : "Cmd_map_13",
    (0xB, 0x14) : "Cmd_map_14", (0xB, 0x15) : "Cmd_map_15", (0xB, 0x16) : "Cmd_map_16", (0xB, 0x17) : "Cmd_map_17",
    (0xB, 0x18) : "Cmd_map_18", (0xB, 0x19) : "Cmd_map_19", (0xB, 0x1A) : "Cmd_map_1A", (0xB, 0x1B) : "Cmd_map_1B",
    (0xB, 0x1C) : "Cmd_map_1C", (0xB, 0x1D) : "Cmd_map_1D", (0xB, 0x1E) : "Cmd_map_1E", (0xB, 0x1F) : "Cmd_map_1F",
    (0xB, 0x20) : "Cmd_map_20", (0xB, 0x21) : "Cmd_map_21", (0xB, 0x22) : "Cmd_map_22", (0xB, 0x23) : "Cmd_map_23",
    (0xB, 0x24) : "Cmd_map_24", (0xB, 0x25) : "Cmd_map_25", (0xB, 0x26) : "Cmd_map_26", (0xB, 0x27) : "Cmd_map_27",
    (0xB, 0x28) : "Cmd_map_28", (0xB, 0x29) : "Cmd_map_29", (0xB, 0x2A) : "Cmd_map_2A", (0xB, 0x2B) : "Cmd_map_2B",
    (0xB, 0x2C) : "Cmd_map_2C", (0xB, 0x2D) : "Cmd_map_2D", (0xB, 0x2E) : "Cmd_map_2E", (0xB, 0x2F) : "Cmd_map_2F",
    (0xB, 0x30) : "Cmd_map_30", (0xB, 0x31) : "Cmd_map_31", (0xB, 0x32) : "Cmd_map_32", (0xB, 0x33) : "Cmd_map_33",
    (0xB, 0x34) : "Cmd_map_34", (0xB, 0x35) : "Cmd_map_35", (0xB, 0x36) : "Cmd_map_36", (0xB, 0x37) : "Cmd_map_37",
    (0xB, 0x38) : "Cmd_map_38", (0xB, 0x39) : "Cmd_map_39", (0xB, 0x3A) : "Cmd_map_3A", (0xB, 0x3B) : "Cmd_map_3B",
    (0xB, 0x3C) : "Cmd_map_3C", (0xB, 0x3D) : "Cmd_map_3D", (0xB, 0x3E) : "Cmd_map_3E", (0xB, 0x3F) : "Cmd_map_3F",
    (0xB, 0x40) : "Cmd_map_40", (0xB, 0x41) : "Cmd_map_41", (0xB, 0x42) : "Cmd_map_42", (0xB, 0x43) : "Cmd_map_43",
    (0xB, 0x44) : "Cmd_map_44", (0xB, 0x45) : "Cmd_map_45", (0xB, 0x46) : "Cmd_map_46", (0xB, 0x47) : "Cmd_map_47",
    (0xB, 0x48) : "Cmd_map_48", (0xB, 0x49) : "Cmd_map_49", (0xB, 0x4A) : "Cmd_map_4A", (0xB, 0x4B) : "Cmd_map_4B",
    (0xB, 0x4C) : "Cmd_map_4C", (0xB, 0x4D) : "Cmd_map_4D", (0xB, 0x4E) : "Cmd_map_4E", (0xB, 0x4F) : "Cmd_map_4F",
    (0xB, 0x50) : "Cmd_map_50", (0xB, 0x51) : "Cmd_map_51", (0xB, 0x52) : "Cmd_map_52", (0xB, 0x53) : "Cmd_map_53",
    (0xB, 0x54) : "Cmd_map_54", (0xB, 0x55) : "Cmd_map_55", (0xB, 0x56) : "Cmd_map_56", (0xB, 0x57) : "Cmd_map_57",
    (0xB, 0x58) : "Cmd_map_58", (0xB, 0x59) : "Cmd_map_59", (0xB, 0x5A) : "Cmd_map_5A", (0xB, 0x5B) : "Cmd_map_5B",
    (0xB, 0x5C) : "Cmd_map_5C", (0xB, 0x5D) : "Cmd_map_5D", (0xB, 0x5F) : "Cmd_map_5F", (0xB, 0x60) : "Cmd_map_60",
    (0xB, 0x61) : "Cmd_map_61", (0xB, 0x62) : "Cmd_map_62", (0xB, 0x63) : "Cmd_map_63", (0xB, 0x64) : "Cmd_map_64",
    (0xB, 0x65) : "Cmd_map_65", (0xB, 0x66) : "Cmd_map_66", (0xB, 0x67) : "Cmd_map_67", (0xB, 0x68) : "Cmd_map_68",
    (0xB, 0x69) : "Cmd_map_69", (0xB, 0x6A) : "Cmd_map_6A", (0xB, 0x6B) : "Cmd_map_6B", (0xB, 0x6C) : "Cmd_map_6C",
    (0xB, 0x6D) : "Cmd_map_6D", (0xB, 0x6E) : "Cmd_map_6E", (0xB, 0x6F) : "Cmd_map_6F", (0xB, 0x70) : "Cmd_map_70",
    (0xB, 0x71) : "Cmd_map_71", (0xB, 0x72) : "Cmd_map_72", (0xB, 0x73) : "Cmd_map_73", (0xB, 0x74) : "Cmd_map_74",
    (0xB, 0x75) : "Cmd_map_75", (0xB, 0x76) : "Cmd_map_76", (0xB, 0x77) : "Cmd_map_77", (0xB, 0x78) : "Cmd_map_78",
    (0xB, 0x79) : "Cmd_map_79", (0xB, 0x7A) : "Cmd_map_7A", (0xB, 0x7B) : "Cmd_map_7B", (0xB, 0x7C) : "Cmd_map_7C",
    (0xB, 0x7D) : "Cmd_map_7D", (0xB, 0x7E) : "Cmd_map_7E", (0xB, 0x7F) : "Cmd_map_7F", (0xB, 0x80) : "Cmd_map_80",
    (0xB, 0x81) : "Cmd_map_81", (0xB, 0x82) : "Cmd_map_82", (0xB, 0x83) : "Cmd_map_83", (0xB, 0x84) : "Cmd_map_84",
    (0xB, 0x85) : "Cmd_map_85", (0xB, 0x86) : "Cmd_map_86", (0xB, 0x87) : "Cmd_map_87", (0xB, 0x88) : "Cmd_map_88",
    (0xB, 0x89) : "Cmd_map_89", (0xB, 0x8A) : "Cmd_map_8A", (0xB, 0x8B) : "Cmd_map_8B", (0xB, 0x8C) : "Cmd_map_8C",
    (0xB, 0x8D) : "Cmd_map_8D", (0xB, 0x8F) : "Cmd_map_8F", (0xB, 0x90) : "Cmd_map_90", (0xB, 0x91) : "Cmd_map_91",
    (0xB, 0x92) : "Cmd_map_92", (0xB, 0x93) : "Cmd_map_93", (0xB, 0x94) : "Cmd_map_94", (0xB, 0x95) : "Cmd_map_95",
    (0xB, 0x96) : "Cmd_map_96", (0xB, 0x97) : "Cmd_map_97", (0xB, 0x98) : "Cmd_map_98",

    # Категория 0xC (12) (Party)
    (0xC, 0x00) : "Cmd_party_00", (0xC, 0x01) : "Cmd_party_01", (0xC, 0x02) : "Cmd_party_02", (0xC, 0x03) : "Cmd_party_03",
    (0xC, 0x04) : "Cmd_party_04", (0xC, 0x05) : "Cmd_party_05", (0xC, 0x06) : "Cmd_party_06", (0xC, 0x07) : "Cmd_party_07",
    (0xC, 0x08) : "Cmd_party_08", (0xC, 0x09) : "Cmd_party_09", (0xC, 0x0A) : "Cmd_party_0A", (0xC, 0x0B) : "Cmd_party_0B",
    (0xC, 0x0C) : "Cmd_party_0C", (0xC, 0x0D) : "Cmd_party_0D", (0xC, 0x0E) : "Cmd_party_0E", (0xC, 0x0F) : "Cmd_party_0F",
    (0xC, 0x10) : "Cmd_party_10", (0xC, 0x11) : "Cmd_party_11", (0xC, 0x12) : "Cmd_party_12", (0xC, 0x13) : "Cmd_party_13",
    (0xC, 0x14) : "Cmd_party_14", (0xC, 0x15) : "Cmd_party_15", (0xC, 0x16) : "Cmd_party_16", (0xC, 0x17) : "Cmd_party_17",
    (0xC, 0x18) : "Cmd_party_18", (0xC, 0x19) : "Cmd_party_19", (0xC, 0x1A) : "Cmd_party_1A", (0xC, 0x1B) : "Cmd_party_1B",
    (0xC, 0x1C) : "Cmd_party_1C", (0xC, 0x1D) : "Cmd_party_1D", (0xC, 0x1E) : "Cmd_party_1E", (0xC, 0x1F) : "Cmd_party_1F",
    (0xC, 0x20) : "Cmd_party_20", (0xC, 0x21) : "Cmd_party_21", (0xC, 0x22) : "Cmd_party_22", (0xC, 0x23) : "Cmd_party_23",
    (0xC, 0x24) : "Cmd_party_24", (0xC, 0x25) : "Cmd_party_25", (0xC, 0x26) : "Cmd_party_26", (0xC, 0x27) : "Cmd_party_27",
    (0xC, 0x28) : "Cmd_party_28", (0xC, 0x29) : "Cmd_party_29", (0xC, 0x2A) : "Cmd_party_2A", (0xC, 0x2B) : "Cmd_party_2B",
    (0xC, 0x2C) : "Cmd_party_2C", (0xC, 0x2D) : "Cmd_party_2D", (0xC, 0x2E) : "Cmd_party_2E", (0xC, 0x2F) : "Cmd_party_2F",
    (0xC, 0x30) : "Cmd_party_30", (0xC, 0x31) : "Cmd_party_31", (0xC, 0x32) : "Cmd_party_32", (0xC, 0x33) : "Cmd_party_33",
    (0xC, 0x34) : "Cmd_party_34", (0xC, 0x35) : "Cmd_party_35",

    # Категория 0xD (13) (Battle)
    (0xD, 0x00) : "Cmd_btl_00", (0xD, 0x01) : "Cmd_btl_01", (0xD, 0x02) : "Cmd_btl_02", (0xD, 0x03) : "Cmd_btl_03",
    (0xD, 0x04) : "Cmd_btl_04", (0xD, 0x05) : "Cmd_btl_05", (0xD, 0x06) : "Cmd_btl_06", (0xD, 0x07) : "Cmd_btl_07",
    (0xD, 0x08) : "Cmd_btl_08", (0xD, 0x09) : "Cmd_btl_09", (0xD, 0x0A) : "Cmd_btl_0A", (0xD, 0x0B) : "Cmd_btl_0B",
    (0xD, 0x0C) : "Cmd_btl_0C", (0xD, 0x0D) : "Cmd_btl_0D", (0xD, 0x0E) : "Cmd_btl_0E", (0xD, 0x0F) : "Cmd_btl_0F",
    (0xD, 0x10) : "Cmd_btl_10", (0xD, 0x11) : "Cmd_btl_11", (0xD, 0x12) : "Cmd_btl_12", (0xD, 0x13) : "Cmd_btl_13",
    (0xD, 0x14) : "Cmd_btl_14", (0xD, 0x15) : "Cmd_btl_15", (0xD, 0x16) : "Cmd_btl_16", (0xD, 0x17) : "Cmd_btl_17",
    (0xD, 0x18) : "Cmd_btl_18", (0xD, 0x19) : "Cmd_btl_19", (0xD, 0x1A) : "Cmd_btl_1A", (0xD, 0x1B) : "Cmd_btl_1B",
    (0xD, 0x1C) : "Cmd_btl_1C", (0xD, 0x1D) : "Cmd_btl_1D", (0xD, 0x1E) : "Cmd_btl_1E", (0xD, 0x1F) : "Cmd_btl_1F",
    (0xD, 0x20) : "Cmd_btl_20", (0xD, 0x21) : "Cmd_btl_21", (0xD, 0x22) : "Cmd_btl_22", (0xD, 0x23) : "Cmd_btl_23",
    (0xD, 0x24) : "Cmd_btl_24", (0xD, 0x25) : "Cmd_btl_25", (0xD, 0x26) : "Cmd_btl_26", (0xD, 0x27) : "Cmd_btl_27",
    (0xD, 0x28) : "Cmd_btl_28", (0xD, 0x29) : "Cmd_btl_29", (0xD, 0x2A) : "Cmd_btl_2A", (0xD, 0x2B) : "Cmd_btl_2B",
    (0xD, 0x2C) : "Cmd_btl_2C", (0xD, 0x2D) : "Cmd_btl_2D", (0xD, 0x2E) : "Cmd_btl_2E", (0xD, 0x2F) : "Cmd_btl_2F",
    (0xD, 0x30) : "Cmd_btl_30", (0xD, 0x31) : "Cmd_btl_31", (0xD, 0x32) : "Cmd_btl_32", (0xD, 0x33) : "Cmd_btl_33",
    (0xD, 0x34) : "Cmd_btl_34", (0xD, 0x35) : "Cmd_btl_35", (0xD, 0x36) : "Cmd_btl_36", (0xD, 0x37) : "Cmd_btl_37",
    (0xD, 0x38) : "Cmd_btl_38", (0xD, 0x39) : "Cmd_btl_39", (0xD, 0x3A) : "Cmd_btl_3A", (0xD, 0x3B) : "Cmd_btl_3B",
    (0xD, 0x3C) : "Cmd_btl_3C", (0xD, 0x3D) : "Cmd_btl_3D", (0xD, 0x3E) : "Cmd_btl_3E", (0xD, 0x3F) : "Cmd_btl_3F",
    (0xD, 0x40) : "Cmd_btl_40", (0xD, 0x41) : "Cmd_btl_41", (0xD, 0x42) : "Cmd_btl_42", (0xD, 0x43) : "Cmd_btl_43",
    (0xD, 0x44) : "Cmd_btl_44", (0xD, 0x45) : "Cmd_btl_45", (0xD, 0x46) : "Cmd_btl_46", (0xD, 0x47) : "Cmd_btl_47",
    (0xD, 0x48) : "Cmd_btl_48", (0xD, 0x49) : "Cmd_btl_49", (0xD, 0x4A) : "Cmd_btl_4A", (0xD, 0x4B) : "Cmd_btl_4B",
    (0xD, 0x4C) : "Cmd_btl_4C", (0xD, 0x4D) : "Cmd_btl_4D", (0xD, 0x4E) : "Cmd_btl_4E", (0xD, 0x4F) : "Cmd_btl_4F",
    (0xD, 0x50) : "Cmd_btl_50", (0xD, 0x51) : "Cmd_btl_51", (0xD, 0x52) : "Cmd_btl_52", (0xD, 0x53) : "Cmd_btl_53",
    (0xD, 0x54) : "Cmd_btl_54", (0xD, 0x55) : "Cmd_btl_55", (0xD, 0x56) : "Cmd_btl_56", (0xD, 0x57) : "Cmd_btl_57",
    (0xD, 0x58) : "Cmd_btl_58", (0xD, 0x59) : "Cmd_btl_59", (0xD, 0x5A) : "Cmd_btl_5A", (0xD, 0x5B) : "Cmd_btl_5B",
    (0xD, 0x5C) : "Cmd_btl_5C", (0xD, 0x5D) : "Cmd_btl_5D", (0xD, 0x5E) : "Cmd_btl_5E", (0xD, 0x5F) : "Cmd_btl_5F",
    (0xD, 0x60) : "Cmd_btl_60", (0xD, 0x61) : "Cmd_btl_61", (0xD, 0x62) : "Cmd_btl_62", (0xD, 0x63) : "Cmd_btl_63",
    (0xD, 0x64) : "Cmd_btl_64", (0xD, 0x65) : "Cmd_btl_65", (0xD, 0x67) : "Cmd_btl_67", (0xD, 0x68) : "Cmd_btl_68",
    (0xD, 0x69) : "Cmd_btl_69", (0xD, 0x6A) : "Cmd_btl_6A", (0xD, 0x6B) : "Cmd_btl_6B", (0xD, 0x6E) : "Cmd_btl_6E",
    (0xD, 0x6F) : "Cmd_btl_6F", (0xD, 0x70) : "Cmd_btl_70", (0xD, 0x71) : "Cmd_btl_71", (0xD, 0x72) : "Cmd_btl_72",
    (0xD, 0x73) : "Cmd_btl_73", (0xD, 0x74) : "Cmd_btl_74", (0xD, 0x75) : "Cmd_btl_75", (0xD, 0x76) : "Cmd_btl_76",
    (0xD, 0x77) : "Cmd_btl_77", (0xD, 0x78) : "Cmd_btl_78", (0xD, 0x79) : "Cmd_btl_79", (0xD, 0x7A) : "Cmd_btl_7A",
    (0xD, 0x7B) : "Cmd_btl_7B", (0xD, 0x7C) : "Cmd_btl_7C", (0xD, 0x7D) : "Cmd_btl_7D", (0xD, 0x7E) : "Cmd_btl_7E",
    (0xD, 0x7F) : "Cmd_btl_7F", (0xD, 0x80) : "Cmd_btl_80", (0xD, 0x81) : "Cmd_btl_81", (0xD, 0x83) : "Cmd_btl_83",
    (0xD, 0x84) : "Cmd_btl_84",

    # Категория 0xE (14) (Unknown_5)
    (0xE, 0x00) : "Cmd_unknown_5_00", (0xE, 0x01) : "Cmd_unknown_5_01", (0xE, 0x02) : "Cmd_unknown_5_02",
    (0xE, 0x03) : "Cmd_unknown_5_03", (0xE, 0x04) : "Cmd_unknown_5_04", (0xE, 0x05) : "Cmd_unknown_5_05",
    (0xE, 0x06) : "Cmd_unknown_5_06", (0xE, 0x07) : "Cmd_unknown_5_07", (0xE, 0x08) : "Cmd_unknown_5_08",
    (0xE, 0x09) : "Cmd_unknown_5_09", (0xE, 0x0A) : "Cmd_unknown_5_0A", (0xE, 0x0B) : "Cmd_unknown_5_0B",
    (0xE, 0x0C) : "Cmd_unknown_5_0C", (0xE, 0x0D) : "Cmd_unknown_5_0D", (0xE, 0x0E) : "Cmd_unknown_5_0E",
    (0xE, 0x0F) : "Cmd_unknown_5_0F", (0xE, 0x10) : "Cmd_unknown_5_10", (0xE, 0x11) : "Cmd_unknown_5_11",
    (0xE, 0x12) : "Cmd_unknown_5_12", (0xE, 0x13) : "Cmd_unknown_5_13", (0xE, 0x14) : "Cmd_unknown_5_14",
    (0xE, 0x15) : "Cmd_unknown_5_15", (0xE, 0x16) : "Cmd_unknown_5_16", (0xE, 0x17) : "Cmd_unknown_5_17",
    (0xE, 0x18) : "Cmd_unknown_5_18", (0xE, 0x19) : "Cmd_unknown_5_19", (0xE, 0x1A) : "Cmd_unknown_5_1A",
    (0xE, 0x1B) : "Cmd_unknown_5_1B", (0xE, 0x1C) : "Cmd_unknown_5_1C", (0xE, 0x1D) : "Cmd_unknown_5_1D",
    (0xE, 0x1E) : "Cmd_unknown_5_1E", (0xE, 0x1F) : "Cmd_unknown_5_1F", (0xE, 0x20) : "Cmd_unknown_5_20",
    (0xE, 0x21) : "Cmd_unknown_5_21", (0xE, 0x22) : "Cmd_unknown_5_22", (0xE, 0x23) : "Cmd_unknown_5_23",
    (0xE, 0x24) : "Cmd_unknown_5_24", (0xE, 0x25) : "Cmd_unknown_5_25", (0xE, 0x26) : "Cmd_unknown_5_26",
    (0xE, 0x28) : "Cmd_unknown_5_28", (0xE, 0x29) : "Cmd_unknown_5_29", (0xE, 0x2A) : "Cmd_unknown_5_2A",
    (0xE, 0x2B) : "Cmd_unknown_5_2B", (0xE, 0x2C) : "Cmd_unknown_5_2C", (0xE, 0x30) : "Cmd_unknown_5_30",

    # Категория 0xF (15) (Menu)
    (0xF, 0x00) : "Cmd_menu_00", (0xF, 0x01) : "AddItemToMenu", (0xF, 0x02) : "OpenMenu", (0xF, 0x03) : "CloseMenu",
    (0xF, 0x04) : "Cmd_menu_04", (0xF, 0x05) : "Cmd_menu_05", (0xF, 0x06) : "Cmd_menu_06", (0xF, 0x07) : "Cmd_menu_07",
    (0xF, 0x08) : "Cmd_menu_08", (0xF, 0x09) : "Cmd_menu_09", (0xF, 0x0A) : "Cmd_menu_0A", (0xF, 0x0B) : "Cmd_menu_0B",
    (0xF, 0x0C) : "Cmd_menu_0C", (0xF, 0x0D) : "Cmd_menu_0D", (0xF, 0x0E) : "Cmd_menu_0E", (0xF, 0x0F) : "Cmd_menu_0F",
    (0xF, 0x10) : "Cmd_menu_10", (0xF, 0x11) : "Cmd_menu_11", (0xF, 0x12) : "Cmd_menu_12", (0xF, 0x13) : "Cmd_menu_13",
    (0xF, 0x14) : "Cmd_menu_14", (0xF, 0x16) : "Cmd_menu_16", (0xF, 0x17) : "Cmd_menu_17", (0xF, 0x18) : "Cmd_menu_18",
    (0xF, 0x19) : "Cmd_menu_19", (0xF, 0x1A) : "Cmd_menu_1A", (0xF, 0x1B) : "Cmd_menu_1B", (0xF, 0x1C) : "Cmd_menu_1C",
    (0xF, 0x1D) : "Cmd_menu_1D", (0xF, 0x1E) : "Cmd_menu_1E", (0xF, 0x1F) : "Cmd_menu_1F", (0xF, 0x20) : "Cmd_menu_20",
    (0xF, 0x21) : "Cmd_menu_21", (0xF, 0x22) : "Cmd_menu_22", (0xF, 0x23) : "Cmd_menu_23", (0xF, 0x25) : "Cmd_menu_25",
    (0xF, 0x26) : "Cmd_menu_26", (0xF, 0x27) : "Cmd_menu_27", (0xF, 0x28) : "Cmd_menu_28", (0xF, 0x29) : "Cmd_menu_29",
    (0xF, 0x2A) : "Cmd_menu_2A", (0xF, 0x2B) : "Cmd_menu_2B", (0xF, 0x2C) : "Cmd_menu_2C", (0xF, 0x2D) : "Cmd_menu_2D",
    (0xF, 0x2E) : "Cmd_menu_2E", (0xF, 0x2F) : "Cmd_menu_2F", (0xF, 0x30) : "Cmd_menu_30", (0xF, 0x31) : "Cmd_menu_31",
    (0xF, 0x32) : "Cmd_menu_32", (0xF, 0x33) : "Cmd_menu_33", (0xF, 0x34) : "Cmd_menu_34", (0xF, 0x35) : "Cmd_menu_35",
    (0xF, 0x36) : "Cmd_menu_36", (0xF, 0x37) : "Cmd_menu_37", (0xF, 0x38) : "Cmd_menu_38", (0xF, 0x39) : "Cmd_menu_39",
    (0xF, 0x3A) : "Cmd_menu_3A", (0xF, 0x3B) : "Cmd_menu_3B", (0xF, 0x3C) : "Cmd_menu_3C", (0xF, 0x3D) : "Cmd_menu_3D",
    (0xF, 0x3E) : "Cmd_menu_3E", (0xF, 0x3F) : "Cmd_menu_3F", (0xF, 0x40) : "Cmd_menu_40", (0xF, 0x41) : "Cmd_menu_41",
    (0xF, 0x42) : "Cmd_menu_42", (0xF, 0x43) : "Cmd_menu_43", (0xF, 0x44) : "Cmd_menu_44", (0xF, 0x45) : "Cmd_menu_45",
    (0xF, 0x46) : "Cmd_menu_46", (0xF, 0x47) : "Cmd_menu_47", (0xF, 0x48) : "Cmd_menu_48", (0xF, 0x49) : "Cmd_menu_49",
    (0xF, 0x4A) : "Cmd_menu_4A",

    # Категория 0x10 (16) (Unknown_6)
    (0x10, 0x00) : "Cmd_unknown_6_00", (0x10, 0x01) : "Cmd_unknown_6_01", (0x10, 0x02) : "Cmd_unknown_6_02",
    (0x10, 0x03) : "Cmd_unknown_6_03", (0x10, 0x04) : "Cmd_unknown_6_04", (0x10, 0x05) : "Cmd_unknown_6_05",
    (0x10, 0x06) : "Cmd_unknown_6_06", (0x10, 0x07) : "Cmd_unknown_6_07", (0x10, 0x08) : "Cmd_unknown_6_08",
    (0x10, 0x09) : "Cmd_unknown_6_09", (0x10, 0x0A) : "Cmd_unknown_6_0A", (0x10, 0x0B) : "Cmd_unknown_6_0B",
    (0x10, 0x0C) : "Cmd_unknown_6_0C", (0x10, 0x0D) : "Cmd_unknown_6_0D", (0x10, 0x0E) : "Cmd_unknown_6_0E",
    (0x10, 0x0F) : "Cmd_unknown_6_0F", (0x10, 0x10) : "Cmd_unknown_6_10", (0x10, 0x11) : "Cmd_unknown_6_11",
    (0x10, 0x12) : "Cmd_unknown_6_12", (0x10, 0x13) : "Cmd_unknown_6_13", (0x10, 0x14) : "Cmd_unknown_6_14",
    (0x10, 0x15) : "Cmd_unknown_6_15", (0x10, 0x16) : "Cmd_unknown_6_16", (0x10, 0x17) : "Cmd_unknown_6_17",
    (0x10, 0x1A) : "Cmd_unknown_6_1A",

    # Категория 0x11 (17) (UI?)
    (0x11, 0x00) : "Cmd_unknown_7_00", (0x11, 0x01) : "Cmd_unknown_7_01", (0x11, 0x02) : "Cmd_unknown_7_02",
    (0x11, 0x03) : "Cmd_unknown_7_03", (0x11, 0x04) : "Cmd_unknown_7_04", (0x11, 0x05) : "Cmd_unknown_7_05",
    (0x11, 0x06) : "Cmd_unknown_7_06", (0x11, 0x07) : "Cmd_unknown_7_07", (0x11, 0x08) : "Cmd_unknown_7_08",
    (0x11, 0x09) : "Cmd_unknown_7_09", (0x11, 0x0A) : "Cmd_unknown_7_0A", (0x11, 0x0B) : "Cmd_unknown_7_0B",
    (0x11, 0x0C) : "Cmd_unknown_7_0C", (0x11, 0x0D) : "Cmd_unknown_7_0D", (0x11, 0x0E) : "Cmd_unknown_7_0E",
    (0x11, 0x0F) : "Cmd_unknown_7_0F", (0x11, 0x10) : "Cmd_unknown_7_10", (0x11, 0x11) : "Cmd_unknown_7_11",
    (0x11, 0x12) : "Cmd_unknown_7_12", (0x11, 0x13) : "Cmd_unknown_7_13", (0x11, 0x14) : "Cmd_unknown_7_14",
    (0x11, 0x15) : "Cmd_unknown_7_15", (0x11, 0x16) : "Cmd_unknown_7_16", (0x11, 0x17) : "Cmd_unknown_7_17",
    (0x11, 0x18) : "Cmd_unknown_7_18", (0x11, 0x19) : "Cmd_unknown_7_19", (0x11, 0x1A) : "Cmd_unknown_7_1A",
    (0x11, 0x1B) : "Cmd_unknown_7_1B", (0x11, 0x1C) : "Cmd_unknown_7_1C", (0x11, 0x1D) : "Cmd_unknown_7_1D",
    (0x11, 0x1E) : "Cmd_unknown_7_1E", (0x11, 0x1F) : "Cmd_unknown_7_1F", (0x11, 0x20) : "Cmd_unknown_7_20",
    (0x11, 0x21) : "Cmd_unknown_7_21", (0x11, 0x22) : "Cmd_unknown_7_22", (0x11, 0x23) : "Cmd_unknown_7_23",
    (0x11, 0x24) : "Cmd_unknown_7_24", (0x11, 0x25) : "Cmd_unknown_7_25", (0x11, 0x26) : "Cmd_unknown_7_26",
    (0x11, 0x27) : "Cmd_unknown_7_27", (0x11, 0x28) : "Cmd_unknown_7_28", (0x11, 0x29) : "Cmd_unknown_7_29",
    (0x11, 0x2A) : "Cmd_unknown_7_2A", (0x11, 0x2B) : "Cmd_unknown_7_2B", (0x11, 0x2C) : "Cmd_unknown_7_2C",
    (0x11, 0x2D) : "Cmd_unknown_7_2D", (0x11, 0x30) : "Cmd_unknown_7_30", (0x11, 0x31) : "Cmd_unknown_7_31",
    (0x11, 0x32) : "Cmd_unknown_7_32", (0x11, 0x33) : "Cmd_unknown_7_33", (0x11, 0x34) : "Cmd_unknown_7_34",
    (0x11, 0x35) : "Cmd_unknown_7_35", (0x11, 0x36) : "Cmd_unknown_7_36", (0x11, 0x37) : "Cmd_unknown_7_37",
    (0x11, 0x38) : "Cmd_unknown_7_38", (0x11, 0x39) : "Cmd_unknown_7_39", (0x11, 0x3A) : "Cmd_unknown_7_3A",
    (0x11, 0x3B) : "Cmd_unknown_7_3B", (0x11, 0x3C) : "Cmd_unknown_7_3C", (0x11, 0x3D) : "Cmd_unknown_7_3D",

    # Категория 0x12 (18) (Portraits)
    (0x12, 0x00) : "Cmd_portraits_00", (0x12, 0x01) : "Cmd_portraits_01", (0x12, 0x02) : "Cmd_portraits_02",
    (0x12, 0x03) : "Cmd_portraits_03", (0x12, 0x04) : "Cmd_portraits_04", (0x12, 0x05) : "Cmd_portraits_05",
    (0x12, 0x06) : "Cmd_portraits_06", (0x12, 0x07) : "Cmd_portraits_07", (0x12, 0x08) : "Cmd_portraits_08",
    (0x12, 0x09) : "Cmd_portraits_09", (0x12, 0x0A) : "Cmd_portraits_0A", (0x12, 0x0B) : "Cmd_portraits_0B",
    (0x12, 0x0C) : "Cmd_portraits_0C", (0x12, 0x0D) : "Cmd_portraits_0D", (0x12, 0x0E) : "Cmd_portraits_0E",
    (0x12, 0x0F) : "Cmd_portraits_0F",

    # Категория 0x13 (19) (BattleStatus)
    (0x13, 0x00) : "Cmd_unknown_8_00", (0x13, 0x01) : "Cmd_unknown_8_01", (0x13, 0x02) : "Cmd_unknown_8_02",
    (0x13, 0x03) : "Cmd_unknown_8_03", (0x13, 0x04) : "Cmd_unknown_8_04", (0x13, 0x05) : "Cmd_unknown_8_05",
    (0x13, 0x06) : "Cmd_unknown_8_06", (0x13, 0x07) : "Cmd_unknown_8_07", (0x13, 0x08) : "Cmd_unknown_8_08",
    (0x13, 0x09) : "Cmd_unknown_8_09", (0x13, 0x0A) : "Cmd_unknown_8_0A", (0x13, 0x0B) : "Cmd_unknown_8_0B",
    (0x13, 0x0C) : "Cmd_unknown_8_0C", (0x13, 0x0D) : "Cmd_unknown_8_0D", (0x13, 0x0E) : "Cmd_unknown_8_0E",
    (0x13, 0x0F) : "Cmd_unknown_8_0F", (0x13, 0x10) : "Cmd_unknown_8_10", (0x13, 0x11) : "Cmd_unknown_8_11",
    (0x13, 0x12) : "Cmd_unknown_8_12", (0x13, 0x13) : "Cmd_unknown_8_13", (0x13, 0x14) : "Cmd_unknown_8_14",
    (0x13, 0x15) : "Cmd_unknown_8_15", (0x13, 0x16) : "Cmd_unknown_8_16", (0x13, 0x17) : "Cmd_unknown_8_17",
    (0x13, 0x18) : "Cmd_unknown_8_18", (0x13, 0x19) : "Cmd_unknown_8_19", (0x13, 0x1A) : "Cmd_unknown_8_1A",
    (0x13, 0x1B) : "Cmd_unknown_8_1B", (0x13, 0x1C) : "Cmd_battlestatus_1C_Dup", (0x13, 0x1D) : "Cmd_unknown_8_1D",
    (0x13, 0x1E) : "Cmd_unknown_8_1E", (0x13, 0x1F) : "Cmd_unknown_8_1F", (0x13, 0x20) : "Cmd_unknown_8_20",

    # Категория 0x14 (20) (ActiveVoice)
    (0x14, 0x00) : "Cmd_activevoice_00", (0x14, 0x01) : "Cmd_activevoice_01", (0x14, 0x02) : "Cmd_activevoice_02",
    (0x14, 0x03) : "Cmd_activevoice_03", (0x14, 0x04) : "Cmd_activevoice_04", (0x14, 0x05) : "Cmd_activevoice_05",

    # Категория 0x15 (21) (Unknown_9)
    (0x15, 0x00) : "Cmd_unknown_9_00", (0x15, 0x01) : "Cmd_unknown_9_01", (0x15, 0x02) : "Cmd_unknown_9_02",
    (0x15, 0x04) : "Cmd_unknown_9_04", (0x15, 0x05) : "Cmd_unknown_9_05", (0x15, 0x06) : "Cmd_unknown_9_06",
    (0x15, 0x07) : "Cmd_unknown_9_07", (0x15, 0x08) : "Cmd_unknown_9_08", (0x15, 0x09) : "Cmd_unknown_9_09",
    (0x15, 0x0A) : "Cmd_unknown_9_0A", (0x15, 0x0B) : "Cmd_unknown_9_0B", (0x15, 0x0C) : "Cmd_unknown_9_0C",
    (0x15, 0x0D) : "Cmd_unknown_9_0D", (0x15, 0x0E) : "Cmd_unknown_9_0E",

    # Категория 0x16 (22) (MapJump)
    (0x16, 0x00) : "Cmd_mapjump_00", (0x16, 0x01) : "Cmd_mapjump_01", (0x16, 0x02) : "Cmd_mapjump_02",
    (0x16, 0x03) : "Cmd_mapjump_03", (0x16, 0x04) : "Cmd_mapjump_04", (0x16, 0x05) : "Cmd_mapjump_05",
    (0x16, 0x06) : "Cmd_mapjump_06", (0x16, 0x07) : "Cmd_mapjump_07", (0x16, 0x08) : "Cmd_mapjump_08",
    (0x16, 0x09) : "Cmd_mapjump_09", (0x16, 0x0A) : "Cmd_mapjump_0A", (0x16, 0x0B) : "Cmd_mapjump_0B",
    (0x16, 0x0C) : "Cmd_mapjump_0C", (0x16, 0x0D) : "Cmd_mapjump_0D", (0x16, 0x0E) : "Cmd_mapjump_0E",
    (0x16, 0x0F) : "Cmd_mapjump_0F", (0x16, 0x10) : "Cmd_mapjump_10",

    # Категория 0x17 (23) (UI)
    (0x17, 0x00) : "Cmd_ui_00", (0x17, 0x01) : "Cmd_ui_01", (0x17, 0x02) : "Cmd_ui_02", (0x17, 0x03) : "Cmd_ui_03",
    (0x17, 0x04) : "Cmd_ui_04", (0x17, 0x05) : "Cmd_ui_05", (0x17, 0x06) : "Cmd_ui_06", (0x17, 0x07) : "Cmd_ui_07",
    (0x17, 0x08) : "Cmd_ui_08", (0x17, 0x09) : "Cmd_ui_09", (0x17, 0x0A) : "Cmd_ui_0A", (0x17, 0x0B) : "Cmd_ui_0B",
    (0x17, 0x0C) : "Cmd_ui_0C", (0x17, 0x0D) : "Cmd_ui_0D", (0x17, 0x0E) : "Cmd_ui_0E", (0x17, 0x0F) : "Cmd_ui_0F",
    (0x17, 0x10) : "Cmd_ui_10", (0x17, 0x11) : "Cmd_ui_11", (0x17, 0x12) : "Cmd_ui_12", (0x17, 0x13) : "Cmd_ui_13",
    (0x17, 0x14) : "Cmd_ui_14", (0x17, 0x15) : "Cmd_ui_15", (0x17, 0x16) : "Cmd_ui_16", (0x17, 0x17) : "Cmd_ui_17",
    (0x17, 0x18) : "Cmd_ui_18", (0x17, 0x19) : "Cmd_ui_19", (0x17, 0x1A) : "Cmd_ui_1A", (0x17, 0x1B) : "Cmd_ui_1B",
    (0x17, 0x1C) : "Cmd_ui_1C", (0x17, 0x1D) : "Cmd_ui_1D", (0x17, 0x1E) : "Cmd_ui_1E", (0x17, 0x1F) : "Cmd_ui_1F",
    (0x17, 0x20) : "Cmd_ui_20", (0x17, 0x21) : "Cmd_ui_21", (0x17, 0x22) : "Cmd_ui_22", (0x17, 0x23) : "Cmd_ui_23",
    (0x17, 0x24) : "Cmd_ui_24", (0x17, 0x25) : "Cmd_ui_25", (0x17, 0x26) : "Cmd_ui_26", (0x17, 0x27) : "Cmd_ui_27",
    (0x17, 0x28) : "Cmd_ui_28", (0x17, 0x29) : "Cmd_ui_29", (0x17, 0x2A) : "Cmd_ui_2A", (0x17, 0x2B) : "Cmd_ui_2B",
    (0x17, 0x30) : "Cmd_ui_30", (0x17, 0x31) : "Cmd_ui_31", (0x17, 0x34) : "Cmd_ui_34", (0x17, 0x35) : "Cmd_ui_35",

    # Категория 0x18 (24) (Unknown_10)
    (0x18, 0x00) : "Cmd_unknown_10_00", (0x18, 0x01) : "Cmd_unknown_10_01", (0x18, 0x02) : "Cmd_unknown_10_02",
    (0x18, 0x03) : "Cmd_unknown_10_03", (0x18, 0x04) : "Cmd_unknown_10_04", (0x18, 0x05) : "Cmd_unknown_10_05",
    (0x18, 0x06) : "Cmd_unknown_10_06", (0x18, 0x07) : "Cmd_unknown_10_07", (0x18, 0x08) : "Cmd_unknown_10_08",
    (0x18, 0x09) : "Cmd_unknown_10_09", (0x18, 0x0A) : "Cmd_unknown_10_0A", (0x18, 0x0B) : "Cmd_unknown_10_0B",
    (0x18, 0x0C) : "Cmd_unknown_10_0C", (0x18, 0x0D) : "Cmd_unknown_10_0D", (0x18, 0x0E) : "Cmd_unknown_10_0E",
    (0x18, 0x0F) : "Cmd_unknown_10_0F", (0x18, 0x10) : "Cmd_unknown_10_10",
    (18, 13)     : "Cmd_unknown_10_13", # Original typo

    # Категория 0x19 (25) (BattleStatus)
    (0x19, 0x00) : "Cmd_battlestatus_00", (0x19, 0x01) : "Cmd_battlestatus_01", (0x19, 0x02) : "Cmd_battlestatus_02",
    (0x19, 0x03) : "Cmd_battlestatus_03", (0x19, 0x04) : "Cmd_battlestatus_04", (0x19, 0x05) : "Cmd_battlestatus_05",
    (0x19, 0x06) : "Cmd_battlestatus_06", (0x19, 0x07) : "Cmd_battlestatus_07", (0x19, 0x08) : "SetEquip",
    (0x19, 0x09) : "Cmd_battlestatus_09", (0x19, 0x0A) : "Cmd_battlestatus_0A", (0x19, 0x0B) : "Cmd_battlestatus_0B",
    (0x19, 0x0C) : "Cmd_battlestatus_0C", (0x19, 0x0D) : "Cmd_battlestatus_0D", (0x19, 0x0E) : "Cmd_battlestatus_0E",
    (0x19, 0x0F) : "Cmd_battlestatus_0F", (0x19, 0x10) : "Cmd_battlestatus_10", (0x19, 0x11) : "Cmd_battlestatus_11",
    (0x19, 0x12) : "Cmd_battlestatus_12", (0x19, 0x13) : "Cmd_battlestatus_13", (0x19, 0x14) : "Cmd_battlestatus_14",
    (0x19, 0x15) : "Cmd_battlestatus_15", (0x19, 0x16) : "Cmd_battlestatus_16", (0x19, 0x17) : "Cmd_battlestatus_17",
    (0x19, 0x18) : "Cmd_battlestatus_18", (0x19, 0x19) : "Cmd_battlestatus_19", (0x19, 0x1A) : "Cmd_battlestatus_1A",
    (0x19, 0x1B) : "Cmd_battlestatus_1B", (0x19, 0x1C) : "Cmd_battlestatus_1C_Dup", (0x19, 0x1D) : "Cmd_battlestatus_1D",
    (0x19, 0x1E) : "Cmd_battlestatus_1E", (0x19, 0x1F) : "Cmd_battlestatus_1F", (0x19, 0x20) : "Cmd_battlestatus_20",
    (0x19, 0x21) : "Cmd_battlestatus_21", (0x19, 0x22) : "Cmd_battlestatus_22_New", (0x19, 0x23) : "Cmd_battlestatus_22",
    (0x19, 0x24) : "Cmd_battlestatus_23", (0x19, 0x25) : "Cmd_battlestatus_25", (0x19, 0x26) : "Cmd_battlestatus_26",

    # Категория 0x1A (26) (Shop)
    (0x1A, 0x00) : "Cmd_shop_00", (0x1A, 0x01) : "Cmd_shop_01", (0x1A, 0x02) : "Cmd_shop_02",
    (0x1A, 0x03) : "Cmd_shop_03", (0x1A, 0x04) : "Cmd_shop_04", (0x1A, 0x05) : "Cmd_shop_05",
    (0x1A, 0x06) : "Cmd_shop_06", (0x1A, 0x07) : "Cmd_shop_07", (0x1A, 0x0A) : "Cmd_shop_0A",

    # Категория 0x1B (27) (Unknown_11)
    (0x1B, 0x00) : "Cmd_unknown_11_00", (0x1B, 0x01) : "Cmd_unknown_11_01",

    # Категория 0x1C (28) (Achievements)
    (0x1C, 0x00) : "Cmd_achievements_00", (0x1C, 0x01) : "Cmd_achievements_01", (0x1C, 0x02) : "Cmd_achievements_02",
    (0x1C, 0x03) : "Cmd_achievements_03", (0x1C, 0x04) : "Cmd_achievements_04", (0x1C, 0x05) : "Cmd_achievements_05",
    (0x1C, 0x06) : "Cmd_achievements_06", (0x1C, 0x07) : "Cmd_achievements_07", (0x1C, 0x08) : "Cmd_achievements_08",
    (0x1C, 0x09) : "Cmd_achievements_09", (0x1C, 0x0A) : "Cmd_achievements_0A", (0x1C, 0x0B) : "Cmd_achievements_0B",
    (0x1C, 0x0C) : "Cmd_achievements_0C", (0x1C, 0x0D) : "Cmd_achievements_0D", (0x1C, 0x0E) : "Cmd_achievements_0E",
    (0x1C, 0x10) : "Cmd_achievements_10", (0x1C, 0x11) : "Cmd_achievements_11", (0x1C, 0x12) : "Cmd_achievements_12",
    (0x1C, 0x13) : "Cmd_achievements_13", (0x1C, 0x14) : "Cmd_achievements_14", (0x1C, 0x15) : "Cmd_achievements_15",
    (0x1C, 0x16) : "Cmd_achievements_16", (0x1C, 0x17) : "Cmd_achievements_17", (0x1C, 0x18) : "Cmd_achievements_18",
    (0x1C, 0x1A) : "Cmd_achievements_1A", (0x1C, 0x1C) : "Cmd_achievements_1C", (0x1C, 0x1D) : "Cmd_achievements_1D",
    (0x1C, 0x1F) : "Cmd_achievements_1F", (0x1C, 0x20) : "Cmd_achievements_20", (0x1C, 0x21) : "Cmd_achievements_21",
    (0x1C, 0x22) : "Cmd_achievements_22", (0x1C, 0x23) : "Cmd_achievements_23", (0x1C, 0x24) : "Cmd_achievements_24",
    (0x1C, 0x25) : "Cmd_achievements_25", (0x1C, 0x26) : "Cmd_achievements_26", (0x1C, 0x27) : "Cmd_achievements_27",
    (0x1C, 0x28) : "Cmd_achievements_28", (0x1C, 0x29) : "Cmd_achievements_29", (0x1C, 0x2A) : "Cmd_achievements_2A",
    (0x1C, 0x2B) : "Cmd_achievements_2B", (0x1C, 0x2D) : "Cmd_achievements_2D", (0x1C, 0x2E) : "Cmd_achievements_2E",
    (0x1C, 0x2F) : "Cmd_achievements_2F", (0x1C, 0x30) : "Cmd_achievements_30", (0x1C, 0x31) : "Cmd_achievements_31",
    (0x1C, 0x32) : "Cmd_achievements_32", (0x1C, 0x33) : "Cmd_achievements_33", (0x1C, 0x35) : "Cmd_achievements_35",

    # Категория 0x1D (29) (Unknown_12)
    (0x1D, 0x00) : "Cmd_unknown_12_00", (0x1D, 0x01) : "Cmd_unknown_12_01", (0x1D, 0x02) : "Cmd_unknown_12_02",
    (0x1D, 0x03) : "Cmd_unknown_12_03", (0x1D, 0x04) : "Cmd_unknown_12_04", (0x1D, 0x05) : "Cmd_unknown_12_05",
    (0x1D, 0x07) : "Cmd_unknown_12_07",
    }

    reverse_commands_dict =  {v: k for k, v in commands_dict.items()}


locations_dict = {} #Address, LocationName
location_counter = 0
smallest_data_ptr = sys.maxsize #big enough
commands_dict = {}
reverse_commands_dict = {}

init_command_names_dicts()




class operand:
    def __init__(self, value, MSB_encoded):
        self.value = value
        self.MSB_encoded = MSB_encoded


def OP_0(instr, stream):
    global smallest_data_ptr

    size = readint(stream, 1)
    value = readint(stream, size)
    if (size == 4):

        type = identifytype(value)
        if (type == "undefined"):
            instr.name = "PUSHUNDEFINED"
        elif (type == "integer"):
            instr.name = "PUSHINTEGER"
        elif (type == "float"):
            instr.name = "PUSHFLOAT"
        elif (type == "string"):
            instr.name = "PUSHSTRING"
            actual_value = remove2MSB(value)
            if actual_value > 0 and smallest_data_ptr > actual_value:
                 smallest_data_ptr = actual_value

    instr.operands.append(operand(value, True))

def OP_1(instr, stream):

    size = readint(stream, 1)
    instr.name = "POP"
    instr.operands.append(operand(size, False))

def OP_2(instr, stream):

    index = readint(stream, 4, signed=True)

    instr.name = "RETRIEVEELEMENTATINDEX"
    instr.operands.append(operand(index, False))

def OP_3(instr, stream):

    index = readint(stream, 4, signed=True)

    instr.name = "RETRIEVEELEMENTATINDEX2"
    instr.operands.append(operand(index, False))

def OP_4(instr, stream):

    index = readint(stream, 4, signed=True)

    instr.name = "PUSHCONVERTINTEGER"
    instr.operands.append(operand(index, False))

def OP_5(instr, stream):

    index = readint(stream, 4, signed=True)

    instr.name = "PUTBACKATINDEX"
    instr.operands.append(operand(index, False))

def OP_6(instr, stream):

    index = readint(stream, 4, signed=True)

    instr.name = "PUTBACK"
    instr.operands.append(operand(index, False))

def OP_7(instr, stream):

    index = readint(stream, 4, signed=True)

    instr.name = "LOAD32"
    instr.operands.append(operand(index, False))

def OP_8(instr, stream):

    index = readint(stream, 4, signed=True)

    instr.name = "STORE32"
    instr.operands.append(operand(index, False))

def OP_9(instr, stream):

    index = readint(stream, 1)

    instr.name = "LOADRESULT"
    instr.operands.append(operand(index, False))

def OP_A(instr, stream):

    index = readint(stream, 1)

    instr.name = "SAVERESULT"
    instr.operands.append(operand(index, False))

def OP_B(instr, stream):
    global location_counter, locations_dict
    addr = readint(stream, 4)
    instr.name = "JUMP"
    if addr not in locations_dict:
        label = "Loc_"+ str(location_counter)
        locations_dict[addr] = label
        location_counter = location_counter + 1
    else:
        label = locations_dict[addr]
    instr.operands.append(operand(label, False))

def OP_C(instr, stream):

    function_index = readint(stream, 2)

    instr.name = "CALL"

    instr.operands.append(operand(function_index, False))

def OP_D(instr, stream):

    instr.name = "EXIT"

def OP_E(instr, stream):
    global location_counter, locations_dict
    addr = readint(stream, 4)
    instr.name = "JUMPIFTRUE"
    if addr not in locations_dict:
        label = "Loc_"+ str(location_counter)
        locations_dict[addr] = label
        location_counter = location_counter + 1
    else:
        label = locations_dict[addr]
    instr.operands.append(operand(label, False))

def OP_F(instr, stream):
    global location_counter, locations_dict
    addr = readint(stream, 4)
    instr.name = "JUMPIFFALSE"
    if addr not in locations_dict:
        label = "Loc_"+ str(location_counter)
        locations_dict[addr] = label
        location_counter = location_counter + 1
    else:
        label = locations_dict[addr]
    instr.operands.append(operand(label, False))

def OP_10(instr, stream): instr.name = "ADD"
def OP_11(instr, stream): instr.name = "SUBTRACT"
def OP_12(instr, stream): instr.name = "MULTIPLY"
def OP_13(instr, stream): instr.name = "DIVIDE"
def OP_14(instr, stream): instr.name = "MODULO"
def OP_15(instr, stream): instr.name = "EQUAL"
def OP_16(instr, stream): instr.name = "NONEQUAL"
def OP_17(instr, stream): instr.name = "GREATERTHAN"
def OP_18(instr, stream): instr.name = "GREATEROREQ"
def OP_19(instr, stream): instr.name = "LOWERTHAN"
def OP_1A(instr, stream): instr.name = "LOWEROREQ"
def OP_1B(instr, stream): instr.name = "AND_"
def OP_1C(instr, stream): instr.name = "OR1"
def OP_1D(instr, stream): instr.name = "OR2"
def OP_1E(instr, stream): instr.name = "OR3"
def OP_1F(instr, stream): instr.name = "NEGATIVE"
def OP_20(instr, stream): instr.name = "ISFALSE"
def OP_21(instr, stream): instr.name = "XOR1"

def OP_22(instr, stream):
    global smallest_data_ptr
    value = readint(stream, 4); instr.operands.append(operand(value, True))
    actual_value = remove2MSB(value)
    if actual_value > 0 and smallest_data_ptr > actual_value: smallest_data_ptr = actual_value
    value = readint(stream, 4); instr.operands.append(operand(value, True))
    actual_value = remove2MSB(value)
    if actual_value > 0 and smallest_data_ptr > actual_value: smallest_data_ptr = actual_value
    nb_args = readint(stream, 1); instr.operands.append(operand(nb_args, False))
    instr.name = "CALLFROMANOTHERSCRIPT"

def OP_23(instr, stream):
    global smallest_data_ptr
    value = readint(stream, 4); instr.operands.append(operand(value, True))
    actual_value = remove2MSB(value)
    if actual_value > 0 and smallest_data_ptr > actual_value: smallest_data_ptr = actual_value
    value = readint(stream, 4); instr.operands.append(operand(value, True))
    actual_value = remove2MSB(value)
    if actual_value > 0 and smallest_data_ptr > actual_value: smallest_data_ptr = actual_value
    nb_args = readint(stream, 1); instr.operands.append(operand(nb_args, False))
    instr.name = "CALLFROMANOTHERSCRIPT2"

def OP_24(instr, stream):
    global commands_dict
    structID = readint(stream, 1)
    command_op_code = readint(stream, 1)
    nb_args = readint(stream, 1)
    instr.name = "RUNCMD"
    instr.operands.append(operand(nb_args, False))
    command_key = (structID, command_op_code)
    if command_key in commands_dict:
        instr.operands.append(operand(commands_dict[command_key], False))
    else:
        raise KeyError(command_key)

def OP_25(instr, stream):
    global location_counter, locations_dict
    addr = readint(stream, 4)
    instr.name = "PUSHRETURNADDRESSFROMANOTHERSCRIPT"
    if addr not in locations_dict:
        label = "Loc_"+ str(location_counter)
        locations_dict[addr] = label
        location_counter = location_counter + 1
    else:
        label = locations_dict[addr]
    instr.operands.append(operand(label, False))

def OP_26(instr, stream):
    value = readint(stream, 2); instr.operands.append(operand(value, False))
    instr.name = "ADDLINEMARKER"

def OP_27(instr, stream):
    value = readint(stream, 1); instr.operands.append(operand(value, False))
    instr.name = "POP2"

def OP_28(instr, stream):
    value = readint(stream, 4); instr.operands.append(operand(value, False))
    instr.name = "DEBUG"

instruction_set = {0 : OP_0,
                   1 : OP_1,
                   2 : OP_2,
                   3 : OP_3,
                   4 : OP_4,
                   5 : OP_5,
                   6 : OP_6,
                   7 : OP_7,
                   8 : OP_8,
                   9 : OP_9,
                   0xA : OP_A,
                   0xB : OP_B,
                   0xC : OP_C,
                   0xD : OP_D,
                   0xE : OP_E,
                   0xF : OP_F,
                   0x10 : OP_10,
                   0x11 : OP_11,
                   0x12 : OP_12,
                   0x13 : OP_13,
                   0x14 : OP_14,
                   0x15 : OP_15,
                   0x16 : OP_16,
                   0x17 : OP_17,
                   0x18 : OP_18,
                   0x19 : OP_19,
                   0x1A : OP_1A,
                   0x1B : OP_1B,
                   0x1C : OP_1C,
                   0x1D : OP_1D,
                   0x1E : OP_1E,
                   0x1F : OP_1F,
                   0x20 : OP_20,
                   0x21 : OP_21,
                   0x22 : OP_22,
                   0x23 : OP_23,
                   0x24 : OP_24,
                   0x25 : OP_25,
                   0x26 : OP_26,
                   0x27 : OP_27,
                   0x28 : OP_28
}



class instruction(object):
    """description of class"""
    def __init__(self, stream, op_code):
        self.addr = stream.tell() - 1 #minus opcode
        self.op_code = op_code
        self.operands = []
        self.name = ""
        self.text_before = ""

        # Вызываем обработчик опкода
        try:
            if op_code in instruction_set:
                 instruction_set[op_code](self, stream)
            else:
                 raise KeyError(f"Неизвестный опкод {op_code} (0x{op_code:X}) в instruction_set")
        except KeyError as e:
             if self.op_code == 0x24 and isinstance(e.args[0], tuple):
                 raise e
             else:
                 raise KeyError(f"Ошибка ключа при обработке опкода {op_code} (0x{op_code:X}) по адресу {hex(self.addr)}: {e}") from e
        except Exception as e:
             print(f"Ошибка при обработке опкода {op_code} (0x{op_code:X}) по адресу {hex(self.addr)}: {e}")
             raise e


    def to_string(self, stream)->str:
        result = self.text_before + self.name + "("
        for operand_id in range(len(self.operands)-1):
            value = self.operands[operand_id].value
            if (type(value) == str):
                escaped_value = value.replace('\\', '\\\\').replace('"', '\\"')
                result = result + "\"" + escaped_value + "\""
            else:
                if self.operands[operand_id].MSB_encoded == True:
                    result = result + get_actual_value_str(stream, value)
                else:
                    result = result + str(int(value))
            result = result + ", "
        if len(self.operands) > 0:
            value = self.operands[len(self.operands)-1].value
            if (type(value) == str):
                escaped_value = value.replace('\\', '\\\\').replace('"', '\\"')
                result = result + "\"" + escaped_value + "\""
            else:
                if self.operands[len(self.operands)-1].MSB_encoded == True:
                    result = result + get_actual_value_str(stream, value)
                else:
                    result = result + str(int(value))
        result = result + ")"
        return result

# --- END OF FILE ED9InstructionsSet.py ---