import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // You can add styles here

const API_BASE_URL = 'http://localhost:8000';

function App() {
  const [btcPrice, setBtcPrice] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPrice = async () => {
      try {
        setLoading(true);
        setError(null);
        const response = await axios.get(`${API_BASE_URL}/api/price/bitcoin`);
        setBtcPrice(response.data.price);
      } catch (err) {
        setError('Failed to fetch data. Is the backend server running?');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchPrice();
  }, []); // The empty dependency array means this effect runs once on mount

  return (
    <div className="App">
      <header className="App-header">
        <h1>Crypto Stats Dashboard</h1>
        <div className="price-display">
          <h2>Bitcoin (BTC) Price</h2>
          {loading && <p>Loading...</p>}
          {error && <p className="error">{error}</p>}
          {btcPrice !== null && (
            <p className="price">${btcPrice.toLocaleString()}</p>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;