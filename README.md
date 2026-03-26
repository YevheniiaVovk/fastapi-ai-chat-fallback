# AI Chat API (FastAPI + JWT + Hybrid AI)

This is a high-performance Backend API built with **FastAPI**. It features a robust user authentication system and a smart AI chat interface with an **Intelligent Fallback Mechanism**.

## 🌟 Key Features
* **Hybrid AI Strategy**: Seamlessly integrates both OpenAI GPT and Google Gemini.
* **Intelligent Fallback**: If OpenAI hits a quota limit (429), the system automatically reroutes to Gemini.
* **Secure JWT Authentication**: Full registration and login flow using JSON Web Tokens.
* **Persistent History**: All messages are stored in a SQLite database via SQLAlchemy ORM.
* **Modern Tooling**: Managed with `uv` for fast and reproducible environments.

## 📸 Preview

### 1. API Documentation (Swagger UI)
![Swagger UI Screenshot](assets/swagger_ui.png)

### 2. Smart AI Response
![AI Response Screenshot](assets/ai_response.png)

## 🛠 Tech Stack
* **Framework**: FastAPI
* **Database**: SQLite & SQLAlchemy (ORM)
* **Security**: JWT (python-jose), Passlib (bcrypt)
* **AI SDKs**: OpenAI SDK, Google-GenAI
* **Environment**: Pydantic Settings
* **Package Manager**: uv

## 🔒 Security & Authorization
This project follows the **OAuth2** standard. 
1. Users register via `/auth/registration`.
2. Users receive a **JWT Access Token** upon login at `/auth/login`.
3. The token is required for all `/api/` endpoints to access private chat history.

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YevheniiaVovk/fastapi-ai-chat-fallback.git
   cd fastapi-ai-chat-fallback
Install dependencies:

Bash
uv sync
Environment Configuration:
Create a .env file in the root directory:

Code snippet
GEMINI_API_KEY=your_key
CHAT_GPT_API_KEY=your_key
SECRET_KEY=your_secret
ALGORITHM=HS256
Run the application:

Bash
uvicorn app.main:app --reload
