from auth.jwt_auth.base.auth import JWTAuth
from jwt.exceptions import InvalidTokenError

def try_to_decode_token(jwt_auth: JWTAuth, token: str) -> dict | InvalidTokenError:
    try:
        payload = jwt_auth.verify_token(token)
        return payload
    except InvalidTokenError as e:
        return e