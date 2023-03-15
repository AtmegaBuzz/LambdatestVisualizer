from pydantic import BaseModel


class MimeTypePost(BaseModel):
    mimeType:str

class StatusCodePost(BaseModel):
    statusCode:int
