### SMTPd

Для этого примера мы можем использовать встроенный fake smptd (хотя модуль сам по себе deprecated, он то что нам надо сделает)
```
python -m smtpd -c DebuggingServer -n 0.0.0.0:5525
```

Начиная с `20-our-basic-app-sends-fake-emails` подразумевается, что локальный сервер доступен по `0.0.0.0:5525` и так настроена джанга в `settings.py`

Постгрес удобно поднять в контейнере
```
docker run --name demo-postgres -p 5432:5432 -e POSTGRES_PASSWORD=moscowpythonweek2020 -d postgres
```

Редис:
```
docker run --name demo-redis -p 6379:6379 -d redis
```
