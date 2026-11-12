# Лабораторная работа 3: CI для Flask-приложения

Цель: настроить GitHub Actions для установки зависимостей, проверки синтаксиса,
инициализации SQLite и проверки HTTP-ответа Flask-приложения.

Исходное учебное приложение: https://github.com/aixiamomo/flask-todo-app.
Импорты, зависимости и запуск адаптированы для Python 3.

## Локальный запуск

Из корня репозитория:

```bash
cd lab3
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python - <<'PY'
from application import create_app
from application.extensions import db
from application.models import Todo

app = create_app("production")
with app.app_context():
    db.create_all()
PY
python manage.py
```

Приложение доступно по адресу http://127.0.0.1:7345/.
Остановка сервера: Ctrl+C.

## CI

Файл: `../.github/workflows/ci-native.yml`.
Pipeline выполняется при изменениях `lab3/` или своего YAML-файла в ветках
`master` и `main`, а также доступен для ручного запуска.
Команды выполняются из папки `lab3`, база создаётся во временной папке runner.

Шаги:

1. Получение кода и установка Python 3.12.
2. Установка зависимостей и проверка их совместимости.
3. Проверка синтаксиса Python.
4. Создание таблицы `todo` в SQLite.
5. Запуск сервера и запрос `curl` к главной странице.

Для проверки результата откройте Actions → Lab 3 - Flask CI → ci →
Smoke test Flask server. Успешный запуск содержит `HTTP 200` и
`Smoke test passed`.
