# Django, rq и стыдливая параллельность

Материал к докладу. Идти по порядку папок

Чтобы повторить

```
python -m venv venv
source ./venv/bin/activate
pip install django rq markdown rq-dashboard
```

Папки/шаги:

## 00-presentation

Презентация перед демо. По сути это "стыдливая параллельность, rq, django"

## 10-our-basic-app

Примитивная отправная точка: формочка и маркдаун всё такое. Уже можно запускать

```
(venv) ./manage.py runserver
```

## 20-our-basic-app-sends-fake-emails

Отправляем емейлы. Понадобится сервер для почты, можно подрять локальный SMTPd. Для этого примера мы можем использовать встроенный fake smptd (хотя модуль сам по себе deprecated, он то что нам надо сделает)
```
python -m smtpd -c DebuggingServer -n 0.0.0.0:5525
```

В `settings.py` соответствующие настройки ожидают этот же порт

## 21-saving-emails-as-models

Уходим от формочек к моделям, сохраняем их в базе, начинаем показывать реальные данные а не заглушки.

## 22-saving-emails-psql-artificial-delay

Начинем хранить рассылки в постгре и добавляем искуственную задержку при отправке формы. Теперь должно быть заметно, как мы ждём.

Постгрес удобно поднять в контейнере
```
docker run --name demo-postgres -p 5432:5432 -e POSTGRES_PASSWORD=moscowpythonweek2020 -d postgres
```

В `settings.py` соответствующие настройки ожидают этот же и пароль. Для нашего демо можно и остаться на sqlite конечно.

## 30-emails-with-rq

Добавляем ко всему rq. Поднимаем для него редис:
```
docker run --name demo-redis -p 6379:6379 -d redis
```

Не забываем запустить воркер:
```
(venv) rq worker
```
