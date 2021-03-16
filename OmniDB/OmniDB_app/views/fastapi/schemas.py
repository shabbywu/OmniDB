from pydantic import BaseModel


class Credential(BaseModel):
    host: str
    port: int
    username: str
    password: str
    db_name: str

    def __str__(self):
        return f"{self.username}:****@{self.host}:{self.port}/{self.db_name}"


class LoginWithDatabasePayload(BaseModel):
    username: str
    type: str
    credential: Credential


class Token(BaseModel):
    access_token: str
    token_type: str
