# Crypto Stats Web Application

This is a web application that obtains the price of Bitcoin and displays stats and analysis. It is built with a Python/FastAPI backend and a React frontend.

## Features

*   Fetches the current price of Bitcoin.
*   Displays the price in a modern web interface.
*   (Future) Plots historical data and shows detailed market analysis.

## Architecture

This project is a monorepo containing two separate applications:
*   `backend/`: A Python application using FastAPI to serve cryptocurrency data from the CoinGecko API.
*   `frontend/`: A JavaScript application using React (and Vite) to display the data in the browser.

## Setup and Installation

1.  Clone this repository or download the source code.
2.  **Setup the Backend:**
    *   Navigate to the backend directory: `cd backend`
    *   Create and activate a virtual environment:
        ```bash
        python -m venv .venv
        source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
        ```
    *   Install Python dependencies:
        ```bash
        pip install -r requirements.txt
        ```
3.  **Setup the Frontend:**
    *   Make sure you have Node.js and npm installed.
    *   Navigate to the frontend directory: `cd frontend`
    *   Install JavaScript dependencies:
        ```bash
        npm install
        ```

## How to Run

You will need to run the backend and frontend servers in two separate terminals.

1.  **Run the Backend Server:**
    ```bash
    # In the backend/ directory
    uvicorn main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

2.  **Run the Frontend Development Server:**
    ```bash
    # In the frontend/ directory
    npm run dev
    ```
    Open your browser to `http://localhost:5173` to view the application.