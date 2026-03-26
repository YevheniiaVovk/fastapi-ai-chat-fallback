from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.db_models import User, Message
from app.api.deps import get_current_user
from app.schemas.user import UserResponse
from app.services.ai_service import ask_me  
from app.services.openai_service import ask_chatgpt  
from pydantic import BaseModel

router = APIRouter()

class AIRequest(BaseModel):
    user_input: str
    model_type: str = "gemini" 

@router.post("/chat")
def get_ai_chat(
    data: AIRequest, 
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    
    history = db.query(Message).filter(Message.user_id == current_user.id).order_by(Message.id.desc()).limit(10).all()
    history = history[::-1]
    
    chat_context = ""
    for msg in history:
        role_label = "User" if msg.role == "user" else "AI"
        chat_context += f"{role_label}: {msg.content}\n"
    
    full_prompt = f"{chat_context}User: {data.user_input}\nAI:"

   
    model_used = data.model_type.lower()
    
    if model_used == "gpt":
        response_data = ask_chatgpt(full_prompt)
       
        if "OpenAI Error" in response_data.get("response", ""):
            print("GPT failed (quota?), switching to Gemini fallback...")
            response_data = ask_me(full_prompt, current_user.username)
            model_used = "gemini (fallback)"
    else:
        response_data = ask_me(full_prompt, current_user.username)

    ai_text = response_data.get("response") if isinstance(response_data, dict) else str(response_data)


    db.add(Message(content=data.user_input, role="user", user_id=current_user.id))
    db.add(Message(content=ai_text, role="assistant", user_id=current_user.id))
    db.commit()
    
    return {"model_used": model_used, "response": ai_text}

@router.get("/history")
def get_chat_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    messages = db.query(Message).filter(Message.user_id == current_user.id).order_by(Message.id.asc()).all()
    return [
        {"role": msg.role, "content": msg.content, "timestamp": msg.create_at} 
        for msg in messages
    ]
@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user