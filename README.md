# KuroTranslate-Tools ![GitHub repo size](https://img.shields.io/github/repo-size/Stamir36/KuroTranslate-Tools?style=flat-square) ![GitHub last commit](https://img.shields.io/github/last-commit/Stamir36/KuroTranslate-Tools?style=flat-square)

![Banner](https://i.postimg.cc/v8jVKQwg/banner.png)

**Форк KuroTools, предназначенный для работы с файлами `.tbl` и `.dat` с целью создания переводов игр от Nihon Falcom.**<br>
Основано на <a href="https://github.com/nnguyen259/KuroTools">nnguyen259/KuroTools</a><br><br>
Этот набор инструментов предоставляет удобные средства для извлечения, редактирования и внедрения текста в игровые ресурсы, значительно упрощая процесс локализации.

---

## ✨ Особенности

*   🖥️ **Графический интерфейс:** Интуитивно понятный лаунчер для запуска основных функций.
*   ⌨️ **Режим терминала:** Возможность запуска скриптов напрямую из командной строки (см. папку `Start`).
*  **Работа с `.dat` (скрипты):**
    *   **Дизассемблер:** Преобразование бинарных `.dat` файлов в читаемый Python-код (`.py`).
    *   **Экспорт текста:** Автоматическое извлечение потенциально переводимых строк из `.py` файлов в стандартный формат `.xliff`.
    *   **Импорт перевода:** Внедрение переведенного текста из `.xliff` обратно в `.py` файлы.
    *   **Ассемблер:** Сборка модифицированных `.py` файлов обратно в рабочие `.dat` файлы.
*   📑 **Работа с `.tbl` (таблицы):**
    *   **Парсер:** Основан на наработках **Trevor\_**, позволяет извлекать данные из `.tbl` файлов (предположительно в JSON/XLIFF).
*   ✏️ **Встроенный XLIFF Редактор:**
    *   Удобное редактирование извлеченного текста.
    *   Функция **пагинации** для работы с большими файлами.
    *   **Интеграция с автопереводчиком** (DeepL/Google Translate) для ускорения процесса.

## 🖼️ Скриншоты

**Лаунчер:**
![Launcher Screenshot](https://i.ibb.co/7N2jmqyQ/banner1.png)

**Редактор XLIFF:**
![Editor Screenshot](https://i.ibb.co/YxV2HVg/banner2.png)

## 🚀 Начало работы

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/Stamir36/KuroTranslate-Tools.git
    cd KuroTranslate-Tools
    ```

2.  **Установите зависимости:**
   *(Создайте файл `requirements.txt` со следующим содержимым):*
    ```txt
    colorama
    astunparse
    lxml
    customtkinter
    pygments
    deep_translator
    ```
    Убедитесь, что у вас установлен Python 3.x и pip. Затем выполните:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Запустите лаунчер:**
    Дважды кликните по файлу `KuroTranslate.bat` (для Windows) или запустите соответствующий скрипт лаунчера через Python.

## 🛠️ Использование (Терминал)

Основные скрипты для работы из командной строки находятся в папке `Start` (или в корне на прямую).

*   **Декомпиляция `.dat` в `.py` (пакетно):**
    ```bash
    python dat2py_batch.py
    # Скрипт запросит путь к папке с .dat файлами
    ```
*   **Экспорт строк из `.py` в `.xliff`:**
    ```bash
    python py_to_xliff.py
    ```
*   **Импорт перевода из `.xliff` в `.py`:**
    ```bash
    python xliff_to_py.py
    ```
*   **Компиляция `.py` в `.dat` (пакетно):**
    ```bash
    python py2dat_batch.py
    ```
*   **Работа с `.tbl`:**
    ```bash
    # Добавьте примеры для TBL
    ```

## 🤝 Участие и поддержка

*   Об ошибках и предложениях сообщайте через [Issues](https://github.com/Stamir36/KuroTranslate-Tools/issues).
*   Пул-реквесты приветствуются!
