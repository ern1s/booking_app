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


🔑 Аутентификация
Используется OAuth2 с паролем (JWT):

Зарегистрируйтесь: POST /users/register

Получите токен: POST /users/token

Используйте Bearer <token> для авторизации в запросах

📬 Примеры API
Создать ресурс:

json
Копировать
Редактировать
POST /resources/
{
  "name": "Конференц-зал",
  "description": "Уютный кабинет",
  "location": "Бишкек, пр. Чуй"
}
Забронировать:

json
Копировать
Редактировать
POST /bookings/
{
  "resource_id": 1,
  "start_time": "2025-06-27T10:00:00Z",
  "end_time": "2025-06-27T11:00:00Z"
}
📡 WebSocket
Подключитесь к /ws/notify чтобы получать уведомления о новых бронированиях.

javascript
Копировать
Редактировать
const ws = new WebSocket("ws://localhost:8000/ws/notify");
ws.onmessage = (msg) => console.log(msg.data);
🛠 Технологии
FastAPI

SQLAlchemy

Pydantic

SQLite (по умолчанию)

WebSocket

JWT
