import logging
import ssl
import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from .database import engine
from . import models
from .routers import personal_loans, mortgage_loans

# Note: Normally we should use migrations
models.Base.metadata.create_all(bind=engine)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add HTTPS redirect middleware only in production
if os.getenv("ENV") == "production":
    app.add_middleware(HTTPSRedirectMiddleware)


# Middleware to log requests
@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response


# Health API
@app.get("/health")
async def root():
    logger.info("Health check endpoint called")
    return {"message": "the application is running"}


# Include routers
app.include_router(personal_loans.router)
app.include_router(mortgage_loans.router)

if __name__ == "__main__":
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain("c:/cert.pem", keyfile="c:/key.pem")
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_context=ssl_context)
