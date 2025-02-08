# Aiogram mongodb template

- `Aiogram 2`
- `MongoDB`
- `Redis`
- `Motor`
- `i18n`

---

## 📥 Как установить?

### 1. Клонирование репозитория
Сначала клонируйте репозиторий и перейдите в его директорию:

```bash
git clone https://github.com/devvsima/aiogram-mongodb-template.git
cd tgbot
```

### 2. Настройка виртуального окружения ".venv"

#### Linux
Установите зависимости и активируйте виртуальное окружение:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

#### Windows
Похожие шаги для Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> 💡 Примечание: Имя `.venv` можно изменить на любое другое.

### 3. Настройка переменных окружения

Сначала скопируйте файл `.env.dist` и переименуйте его в `.env`:

```bash
cp .env.dist .env
```

Затем отредактируйте файл переменных окружения:

```bash
vim .env
# или
nano .env
```

### 4. Настройки бота

#### `ADMINS` - ID администраторов
Добавьте ID администраторов, разделяя их запятыми

```bash
# пример
ADMINS=12345678,12345677,12345676
```

#### `TOKEN` - Токен бота от [@BotFather](https://t.me/BotFather)
Добавьте токен вашего бота:

```bash
# пример
BOT_TOKEN=123452345243:Asdfasdfasf
```

### 5. Настройка базы данных MongoDB

Укажите параметры подключения к базе данных:

- `MONGO_NAME` - имя базы данных (по умолчанию = 'template')
- `MONGO_HOST` - хост базы данных (по умолчанию = 'localhost')
- `MONGO_PORT` - порт базы данных (по умолчанию = `27017`)
- `MONGO_USER` - пользователь базы данных
- `MONGO_PASS` - пароль базы данных
- `MONGO_URL` - полная ссылка подключения к MongoDB (необязательно)


### 6. Настройка Redis

Redis используется для кэширования и хранения данных сессий. Укажите параметры подключения Redis в файле `.env`:

- `REDIS_HOST` - хост сервера Redis (по умолчанию: `localhost`)
- `REDIS_PORT` - порт сервера Redis (по умолчанию: `6379`)
- `REDIS_DB` - индекс базы данных Redis (по умолчанию: `5`)
- `REDIS_URL` - URL подключения к Redis (необязательно)

Пример:
```bash
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=5
```

Убедитесь, что Redis установлен и запущен перед запуском бота. Вы можете запустить Redis с помощью команды:
```bash
redis-server
```

---

Теперь бот готов к запуску! 🎉
