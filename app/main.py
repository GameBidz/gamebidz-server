from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.auction_routes import router as auction_router

app = FastAPI()

# Include the user router in the app.
app.include_router(user_router)
# Include the auction router in the app.
app.include_router(auction_router)
