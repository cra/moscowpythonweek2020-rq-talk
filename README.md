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

Дашборд ставится с помощью `pip install rq-dashboard` и запускается так же:
```
(venv) rq-dashboard
```

### Кастомный воркер

Для работы воркеру нужны все переменные окружения и работающая django, и просто так скорее всего `rq worker` не запустится. Поэтому нужно сделать простую обёртку над ним:

```
#!/usr/bin/env python
import os
import sys

import django

from rq import Connection, Worker

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailsender.settings')
    django.setup()

    with Connection():
        qs = sys.argv[1:] or ['default']

        w = Worker(qs)
        w.work()
```

(этот скрипт лежит рядом с `manage.py` под названием `rq_worker.py`)

Пример вывода:
```
(venv) $ python rq_worker.py
10:35:14 Worker rq:worker:ccc4d972c7fe4e65a06b8bded83e7db4: started, version 1.5.2
10:35:14 *** Listening on default...
10:35:23 default: pochta_badger.mail_tools.slow_mail_send(<Campaign: Campaign object (4)>) (d7836d00-78d2-49cb-b9dd-dddb3ad320f8)
Got email with test
10:35:26 default: Job OK (d7836d00-78d2-49cb-b9dd-dddb3ad320f8)
10:35:26 Result is kept for 500 seconds
```

