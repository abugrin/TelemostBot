Яндекс Мессенджер бот.

Создает встречу Телемосте.
Нужно создать файл ```.env``` в папке с файлом bot.py содержащий:

```env
BOT_KEY = "API ключ бота"
TELEMOST_KEY = "API ключ доступа к Телемосту"
```

* Как создать бота в организации: https://yandex.ru/support/yandex-360/business/admin/ru/bot-platform.html#bot-create
* Как получить ключ API Телемоста: https://yandex.ru/dev/telemost/doc/ru/access

Установить зависимости
```pip install -r requirements.txt```

Запустить бота
```python bot.py```