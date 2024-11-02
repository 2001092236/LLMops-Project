from contextlib import asynccontextmanager

from app.api import auth, chat, metrics
from app.db.database import database
from app.middleware.auth_middleware import AuthMiddleware
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.rate_limit_middleware import RateLimitMiddleware
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await database.connect()
    yield
    # Shutdown logic
    await database.disconnect()


# lifespan calls twice: at the beginning and at the end
app = FastAPI(lifespan=lifespan)

# Include routers from different modules
# they are different endpoints (url adresses) to call
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(metrics.router)

# Apply middlewares
# They have to be executed before calling endpoint functions (the 3 above)
app.add_middleware(RateLimitMiddleware)
app.add_middleware(AuthMiddleware)
app.add_middleware(LoggingMiddleware)
