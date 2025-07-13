from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from crypto import CryptoMarketInterface

app = FastAPI()

# --- CORS Middleware ---
# This is crucial for development. It allows your React frontend (running on a
# different port) to make requests to this backend.
origins = [
    "http://localhost:5173",  # Default Vite dev server port
    "http://localhost:3000",  # Default Create React App port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Endpoints ---

market = CryptoMarketInterface()

@app.get("/api/price/{coin_id}")
def get_coin_price(coin_id: str, currency: str = "usd"):
    price = market.get_price(coin_id, currency)
    if price is None:
        raise HTTPException(status_code=404, detail=f"Price not found for {coin_id}")
    return {"coin_id": coin_id, "currency": currency, "price": price}

@app.get("/api/market_data/{coin_id}")
def get_coin_market_data(coin_id: str):
    data = market.get_market_data(coin_id)
    if data is None:
        raise HTTPException(status_code=404, detail=f"Market data not found for {coin_id}")
    # For a real app, you'd likely want to select and clean this data
    # before sending it to the frontend.
    return data