from datetime import timedelta
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

jwt_secret = os.environ.get("JWT_SECRET")

@dataclass
class JWTConfig:
    secret: str = jwt_secret
    algorithm: str = "HS256"
    access_token_ttl: timedelta = timedelta(minutes=1)