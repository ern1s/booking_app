# 🏨 Booking App — универсальное API для бронирования ресурсов

Это REST API-приложение на FastAPI для бронирования любых ресурсов: отели, кабинеты, столики в ресторанах, спортивные площадки и т.д.

## 🚀 Возможности

- 🔐 JWT-аутентификация пользователей
- 👤 Регистрация / вход в систему
- 🛠 CRUD-операции для ресурсов (создание, просмотр, удаление)
- 📅 Бронирование с проверкой занятости по времени
- 🔔 Уведомления через WebSocket при новых бронированиях
- 🧑‍💼 Админ-функции: просмотр и управление своими ресурсами
- 📄 OpenAPI-документация (`/docs`)

## ⚙️ Установка

```bash
git clone https://github.com/ern1s/booking_app.git
cd booking_app
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
