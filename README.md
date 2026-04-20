# ⚡ LiveChat — Django WebSocket Chat

Real-time chat ilova. Django Channels + WebSocket + Railway deploy.

---

## 📁 Loyiha tuzilmasi

```
chatproject/
├── config/
│   ├── __init__.py
│   ├── asgi.py          ← WebSocket uchun ASGI
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chat/
│   ├── consumers.py     ← WebSocket logic
│   ├── routing.py       ← WebSocket URL
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── templates/
│   └── chat/
│       ├── index.html   ← Kirish sahifasi
│       └── room.html    ← Chat xonasi
├── static/
│   └── css/
│       └── style.css
├── manage.py
├── requirements.txt
├── Procfile             ← Railway uchun
├── railway.toml         ← Railway config
├── runtime.txt
└── .gitignore
```

---

## ⚙️ Local ishga tushirish

### 1. Virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows
```

### 2. Kutubxonalar

```bash
pip install -r requirements.txt
```

### 3. Migratsiya va static fayllar

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 4. Serverni ishga tushirish

```bash
daphne config.asgi:application
```

Brauzerda: http://127.0.0.1:8000

---

## 🚀 Railway Deploy

### 1. GitHub ga push

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

### 2. Railway sozlash

1. [railway.app](https://railway.app) → **New Project → GitHub repo** tanlang
2. **Variables** bo'limiga qo'shing:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | (pastdagi buyruq bilan generatsiya qiling) |
| `DEBUG` | `False` |

### 3. SECRET_KEY generatsiya

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Build Command (Railway → Settings)

```
python manage.py migrate && python manage.py collectstatic --noinput
```

> Railway `railway.toml` ni avtomatik o'qiydi — start command u yerda.

---

## 🔌 WebSocket qanday ishlaydi

```
Foydalanuvchi  →  /ws/chat/<room_name>/  →  ChatConsumer
                                              ↓
                                        group_send
                                              ↓
                                    Xonadagi hammaga
```

---

## ✍️ Muallif

Anonshack
