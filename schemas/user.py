from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    email: str
    encrypted_password: str
