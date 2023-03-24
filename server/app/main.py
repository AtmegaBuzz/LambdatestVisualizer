import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import GlobalRouter,MimeRouter,StatusRouter

# Load .env variables 
load_dotenv()

app = FastAPI()


app.debug = os.getenv("DEBUG")=="True"

if os.getenv("CORSMiddleware")=="True":
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"], # Allows all origins
        allow_credentials = ["*"],
        allow_methods = ["*"], # Allows all methods
        allow_headers = ["*"]
    )


# Include all routes
app.include_router(GlobalRouter.router)
app.include_router(MimeRouter.router)
app.include_router(StatusRouter.router)