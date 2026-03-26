from pydantic import BaseModel, Field

class AIRequest(BaseModel):
    user_input: str = Field(min_length=1, max_length=1000, description="Message from user")

