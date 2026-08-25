# 📱 Wikipedia Mobile — UI Automation Test Framework

Проект по автоматизации UI-тестирования мобильного приложения **Wikipedia (Android)** с использованием **Python**, **Appium**, **Pytest** и **Allure Report**.

[![UI Mobile Automation Tests](https://github.com/CODE-DENYA/wikipedia-mobile-tests/actions/workflows/main.yml/badge.svg)](https://github.com/CODE-DENYA/wikipedia-mobile-tests/actions/workflows/main.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-brightgreen)](https://CODE-DENYA.github.io/wikipedia-mobile-tests/)

---

## 🛠 Технологический стек

* **Язык программирования:** Python 3.10+
* **Фреймворк автоматизации:** Appium Python Client (v3.0+)
* **Драйвер мобильных устройств:** UiAutomator2 (Android)
* **Фреймворк тестирования:** Pytest
* **Паттерн проектирования:** Page Object Model (POM)
* **Качество кода:** Flake8 (линтер)
* **Отчетность:** Allure Framework (`allure-pytest`) с аннотациями `@allure.epic`, `@allure.title`, детальными шагами `@allure.step` и автоматическим прикреплением скриншотов сбойных шагов
* **CI/CD:** GitHub Actions (автоматический прогон тестов на headless Android Emulator в облаке, проверка качества кода и публикация Allure-отчета на GitHub Pages)

---

## 🧪 Покрытие тестами

Тестовый набор охватывает ключевые пользовательские сценарии взаимодействия с мобильным приложением:

### 🚀 Онбординг (`tests/test_onboarding.py`)
* **Динамический проход:** Проверка отображения начального экрана и корректное сквозное прохождение всех страниц приветствия.

### 🔍 Поиск и навигация (`tests/test_search.py`, `tests/test_clear_search.py`, `tests/test_search_no_results.py`)
* **Базовый поиск:** Ввод запроса (`Python`) и проверка совпадения текста первого результата.
* **Сброс поиска:** Ввод запроса (`Appium`) и сброс текстового поля по кнопке «Очистить» (крестик).
* **Негативный сценарий:** Ввод несуществующего запроса (`qwertyuiop12345`) и проверка отображения экрана `No results`.

### 📜 История поиска (`tests/test_search_history.py`)
* **Полный цикл истории:** Ввод запроса, переход в статью, возврат на главный экран, проверка наличия статьи в истории поиска и ее полное удаление через системное подтверждение.

### 📖 Просмотр и сохранение статей (`tests/test_article.py`, `tests/test_save_article.py`, `tests/test_article_saved_status.py`, `tests/test_save_and_remove_article.py`)
* **Чтение статей:** Переход из поиска на страницу статьи и проверка совпадения заголовка.
* **Сохранение в коллекцию:** E2E-сохранение статьи по кнопке `Save` на нижней панели с валидацией выезжающей шторки (Bottom Sheet) и наличия статьи в разделе `Saved`.
* **Индикаторы UI:** Проверка изменения состояния закладки `Saved` во всплывающей шторке.
* **Отмена сохранения (E2E):** Добавление статьи в сохраненные, снятие флага сохранения прямо из шторки и проверка отсутствия статьи во вкладке `Saved`.

### 🧭 Навигация и Настройки (`tests/test_navigation.py`, `tests/test_settings_navigation.py`)
* **Нижняя панель (Bottom Navigation):** Переключение между ключевыми вкладками `Home`, `Saved` и `More`.
* **Раздел настроек:** Переход в экран `Settings` через меню `More` с проверкой заголовка экрана.

---

## 🏗 Архитектурные особенности фреймворка

* **Page Object Model (POM):** Разделение интерфейса на логические компоненты (`OnboardingPage`, `MainPage`, `ArticlePage`), что обеспечивает переиспользуемость локаторов и упрощает поддержку тестов.
* **Обработка всплывающих окон (`_dismiss_popups`):** Автоматическое уничтожение случайных модальных окон, подсказок («Got it») и акционных банеров во время прохождения сценариев.
* **Интеллектуальные ожидания:** Комбинация явных ожиданий (`WebDriverWait`) и циклов с ретраями для защиты тестов от флейкующих (flaky) анимаций интерфейса Android.
* **Кастомная фикстура `--slow`:** Возможность искусственного замедления прогона (`time.sleep(1.0)` перед командами Appium) для визуального отслеживания действий на эмуляторе при отладке.
* **Автоматические скриншоты в Allure:** Хук `pytest_runtest_makereport` автоматически делает скриншот экрана устройства в момент падения теста и прикрепляет его к Allure-отчету.

---

## 📁 Структура проекта

```text
wikipedia-mobile-tests/
├── .github/
│   └── workflows/
│       └── main.yml                  # CI/CD пайплайн GitHub Actions
├── app/
│   └── wikipedia.apk                 # Тестируемое Android-приложение
├── pages/                            # Page Object классы
│   ├── article_page.py               # Страница просмотра и сохранения статьи
│   ├── main_page.py                  # Главный экран, поиск, история и вкладки
│   └── onboarding_page.py            # Стартовые экраны онбординга
├── tests/                            # Набор автотестов (Pytest)
│   ├── test_article_saved_status.py  # Проверка иконки Saved в шторке
│   ├── test_article.py               # Проверка открытой статьи
│   ├── test_clear_search.py          # Сброс поля поиска
│   ├── test_navigation.py            # Переключение табов нижнего меню
│   ├── test_onboarding.py            # Прохождение онбординга
│   ├── test_save_and_remove_article.py# Добавление и удаление статьи из Saved
│   ├── test_save_article.py          # E2E сохранение статьи в список
│   ├── test_search_history.py        # Проверка и очистка истории поиска
│   ├── test_search_no_results.py     # Проверка отсутствия результатов
│   ├── test_search.py                # Поиск по ключевому слову
│   └── test_settings_navigation.py   # Навигация в экран Settings
├── .gitignore                        # Исключения Git
├── config.py                         # Конфигурация Appium и путей к файлам
├── conftest.py                       # Fixtures Appium, hook'и и аргументы CLI
├── pytest.ini                        # Конфигурация запуска Pytest и Allure
├── requirements.txt                  # Зависимости Python
└── README.md                         # Документация проекта
```

---

## 🚀 Локальный запуск

### 1. Предварительные требования
* **Python 3.10+**
* **Node.js & Appium Server (v2.x)**
* **Android SDK & Emulator** (например, Pixel 4, Android 10.0+ / API 29+)
* Driver **UiAutomator2**: `appium driver install uiautomator2`

### 2. Клонирование репозитория
```bash
git clone https://github.com/CODE-DENYA/wikipedia-mobile-tests.git
cd wikipedia-mobile-tests
```

### 3. Создание и активация виртуального окружения
```bash
python -m venv venv
```
* **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\activate
  ```
* **macOS / Linux / Git Bash:**
  ```bash
  source venv/bin/activate
  ```

### 4. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 5. Запуск Appium сервера
Запустите Appium в отдельном окне терминала:
```bash
appium
```

### 6. Запуск тестов
* **Запуск всех тестов:**
  ```bash
  pytest
  ```
* **Запуск в замедленном режиме (для визуального контроля):**
  ```bash
  pytest --slow
  ```
* **Запуск с генерацией Allure-результатов:**
  ```bash
  pytest --alluredir=allure-results
  ```
* **Просмотр Allure-отчета локально:**
  ```bash
  allure serve allure-results
  ```
* **Проверка качества кода (Flake8):**
  ```bash
  flake8 .
  ```

---

## 🔄 CI/CD Пайплайн

При каждом push или pull request в ветки `main` / `master` запускается автоматический CI/CD workflow в GitHub Actions:
1. Выполняется проверка стиля кода с помощью **Flake8**.
2. Поднимается виртуальное окружение с **KVM-ускорением** и подготавливается **Android Emulator (API 29)**.
3. Разворачивается сервер **Appium** и параллельно запускаются UI-автотесты.
4. При сбоях автоматически снимаются и сохраняются скриншоты.
5. Генерируется и публикуется актуальный **Allure Report** на GitHub Pages.