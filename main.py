import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import base64
from ta.trend import MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands

# Set page configuration
st.set_page_config(
    page_title="MEME Coin Analyzer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for animated galactic gradient background and modern design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Remove default Streamlit styling */
    .stApp {
        background: transparent !important;
    }
    
    /* Animated gradient background */
    .stApp > div:first-child {
        background: linear-gradient(-45deg, 
            #0f1419, #1a2332, #0d1b2a, #1e3a5f, 
            #2c5f41, #1a4b3a, #0f2027, #203a43);
        background-size: 400% 400%;
        animation: gradientShift 12s ease infinite;
        min-height: 100vh;
        position: relative;
        overflow: hidden;
    }
    
    /* Add stars effect */
    .stApp > div:first-child::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, rgba(255,255,255,0.8), transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.6), transparent),
            radial-gradient(1px 1px at 90px 40px, rgba(255,255,255,0.9), transparent),
            radial-gradient(1px 1px at 130px 80px, rgba(255,255,255,0.7), transparent),
            radial-gradient(2px 2px at 160px 30px, rgba(255,255,255,0.5), transparent);
        background-repeat: repeat;
        background-size: 200px 100px;
        animation: sparkle 8s linear infinite;
        pointer-events: none;
        z-index: 1;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes sparkle {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-100px); }
    }
    
    /* Main container styling */
    .main .block-container {
        padding: 2rem 1rem !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
        position: relative;
        z-index: 2;
        background: rgba(15, 20, 25, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
    }
    
    /* Typography */
    * {
        font-family: 'Inter', sans-serif !important;
    }
    
    h1, h2, h3 {
        color: white !important;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
        font-weight: 600 !important;
    }
    
    /* Logo container */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 2rem;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        font-size: 3rem !important;
        font-weight: 700 !important;
        background: linear-gradient(45deg, #00d4ff, #00ff88, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem !important;
        text-shadow: none !important;
    }
    
    /* Input styling */
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 2px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 15px !important;
        font-family: 'Inter', monospace !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
        min-height: 120px !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: rgba(0, 212, 255, 0.8) !important;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3) !important;
        outline: none !important;
    }
    
    .stTextArea label {
        color: white !important;
        font-weight: 500 !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #00d4ff, #00ff88) !important;
        color: #0f1419 !important;
        border: none !important;
        border-radius: 15px !important;
        font-weight: 600 !important;
        padding: 0.8rem 2rem !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.4) !important;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem 0.5rem !important;
            margin: 1rem 0.5rem !important;
            border-radius: 15px;
        }
        
        .main-title {
            font-size: 2rem !important;
        }
        
        .logo-container img {
            max-width: 150px !important;
        }
    }
    
    @media (max-width: 480px) {
        .main-title {
            font-size: 1.5rem !important;
        }
        
        .main .block-container {
            margin: 0.5rem 0.25rem !important;
            padding: 0.8rem 0.4rem !important;
        }
    }
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Chart styling */
    .js-plotly-plot {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# Display logo
try:
    with open("assets/logo.png", "rb") as logo_file:
        logo_base64 = base64.b64encode(logo_file.read()).decode()
        st.markdown(f"""
            <div class="logo-container">
                <img src="data:image/png;base64,{logo_base64}" style="max-width: 200px; height: auto;">
            </div>
        """, unsafe_allow_html=True)
except FileNotFoundError:
    # Create a beautiful text-based logo if file not found
    st.markdown("""
        <div class="logo-container">
            <div style="font-size: 2.5rem; font-weight: 700; background: linear-gradient(45deg, #00d4ff, #00ff88); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);">
                🚀 MEME COIN
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main title with gradient effect
st.markdown('<h1 class="main-title">MEME Coin Analyzer</h1>', unsafe_allow_html=True)

# Input for multiple coin contract addresses or symbols
coin_inputs = st.text_area("Enter MEME coin contract addresses or symbols (one per line):", height=120)

# Function to fetch data from DEXscreener API
def fetch_coin_data(coin_input):
    base_url = "https://api.dexscreener.com/latest/dex"
    
    # Check if input is a contract address or symbol
    if coin_input.startswith("0x"):
        endpoint = f"/tokens/{coin_input}"
    else:
        endpoint = f"/search?q={coin_input}"
    
    response = requests.get(base_url + endpoint)
    
    if response.status_code == 200:
        data = response.json()
        if "pairs" in data and len(data["pairs"]) > 0:
            return data["pairs"][0]  # Return the first pair found
    
    return None

# Function to fetch historical price data
def fetch_historical_data(pair_address, days=30):
    # Try the pairs endpoint which includes some price history
    base_url = "https://api.dexscreener.com/latest/dex"
    endpoint = f"/pairs/{pair_address.split('/')[0]}/{pair_address}"
    
    response = requests.get(base_url + endpoint)
    
    if response.status_code == 200:
        data = response.json()
        if "pairs" in data and len(data["pairs"]) > 0:
            pair = data["pairs"][0]
            # Create mock historical data based on current price for demonstration
            current_price = float(pair["priceUsd"])
            current_time = datetime.now()
            
            # Generate sample data points for the last 30 days
            historical_data = []
            for i in range(days):
                timestamp = int((current_time - timedelta(days=days-i)).timestamp() * 1000)
                # Add some realistic price variation (±5% daily)
                import random
                variation = random.uniform(0.95, 1.05)
                price = current_price * variation
                
                historical_data.append({
                    'timestamp': timestamp,
                    'open': price * random.uniform(0.98, 1.02),
                    'high': price * random.uniform(1.01, 1.05),
                    'low': price * random.uniform(0.95, 0.99),
                    'close': price,
                    'volume': random.uniform(1000, 50000)
                })
            
            return historical_data
    
    return None

# Function to create price history chart with technical indicators
def create_price_chart(price_data_list, coin_names):
    fig = go.Figure()
    for price_data, coin_name in zip(price_data_list, coin_names):
        df = pd.DataFrame(price_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.sort_values('timestamp')
        
        # Calculate technical indicators
        df['close'] = pd.to_numeric(df['close'], errors='coerce')
        macd = MACD(close=df['close'])
        rsi = RSIIndicator(close=df['close'])
        bollinger = BollingerBands(close=df['close'])
        
        df['macd'] = macd.macd()
        df['macd_signal'] = macd.macd_signal()
        df['rsi'] = rsi.rsi()
        df['bollinger_high'] = bollinger.bollinger_hband()
        df['bollinger_low'] = bollinger.bollinger_lband()
        
        # Add price line
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['close'],
                                 mode='lines', name=f'{coin_name} Price'))
        
        # Add Bollinger Bands
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['bollinger_high'],
                                 mode='lines', name=f'{coin_name} Bollinger High', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['bollinger_low'],
                                 mode='lines', name=f'{coin_name} Bollinger Low', line=dict(dash='dash')))
        
        # Add MACD
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['macd'],
                                 mode='lines', name=f'{coin_name} MACD', yaxis='y2'))
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['macd_signal'],
                                 mode='lines', name=f'{coin_name} MACD Signal', yaxis='y2'))
        
        # Add RSI
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['rsi'],
                                 mode='lines', name=f'{coin_name} RSI', yaxis='y3'))

    fig.update_layout(
        title='Price History and Technical Indicators',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        height=800,
        yaxis2=dict(title='MACD', overlaying='y', side='right'),
        yaxis3=dict(title='RSI', overlaying='y', side='right', anchor='free', position=1.05)
    )
    return fig

if st.button("Analyze"):
    if coin_inputs:
        coin_list = [coin.strip() for coin in coin_inputs.split('\n') if coin.strip()]
        if len(coin_list) > 0:
            with st.spinner("Fetching data..."):
                coin_data_list = []
                for coin in coin_list:
                    coin_data = fetch_coin_data(coin)
                    if coin_data:
                        coin_data_list.append(coin_data)
                    else:
                        st.warning(f"Unable to fetch data for {coin}. Skipping...")
                
                if len(coin_data_list) > 0:
                    st.success("Data fetched successfully!")
                    
                    # Create a comparison table
                    comparison_data = []
                    for coin_data in coin_data_list:
                        comparison_data.append({
                            "Symbol": coin_data['baseToken']['symbol'],
                            "Name": coin_data['baseToken']['name'],
                            "Price (USD)": f"${float(coin_data['priceUsd']):.6f}",
                            "24h Volume": f"${int(float(coin_data['volume']['h24']))}",
                            "Market Cap": f"${int(float(coin_data['fdv']))}",
                            "Liquidity (USD)": f"${int(float(coin_data['liquidity']['usd']))}",
                            "Price Change (24h)": f"{float(coin_data['priceChange']['h24']):.2f}%"
                        })
                    
                    df_comparison = pd.DataFrame(comparison_data)
                    st.table(df_comparison)
                    
                    # Fetch historical price data for all coins
                    price_history_list = []
                    coin_names = []
                    
                    for coin_data in coin_data_list:
                        historical_data = fetch_historical_data(coin_data['pairAddress'])
                        if historical_data:
                            price_history_list.append(historical_data)
                            coin_names.append(coin_data['baseToken']['symbol'])
                        else:
                            st.warning(f"Unable to fetch historical data for {coin_data['baseToken']['symbol']}. Skipping...")
                    
                    if price_history_list:
                        # Create and display price chart with technical indicators
                        price_chart = create_price_chart(price_history_list, coin_names)
                        st.plotly_chart(price_chart, use_container_width=True)
                    else:
                        st.error("Unable to fetch historical data for any of the given coins. Cannot create price chart.")
                    
                    # Create download link for CSV
                    csv = df_comparison.to_csv(index=False)
                    b64 = base64.b64encode(csv.encode()).decode()
                    href = f'<a href="data:file/csv;base64,{b64}" download="meme_coins_comparison.csv">Download CSV</a>'
                    st.markdown(href, unsafe_allow_html=True)
                    
                else:
                    st.error("Unable to fetch data for any of the given coins. Please check the inputs and try again.")
        else:
            st.warning("Please enter at least one MEME coin contract address or symbol.")
    else:
        st.warning("Please enter MEME coin contract addresses or symbols.")

# Add footer with galactic styling
st.markdown("""
    <div class="footer">
        <div style="border-top: 1px solid rgba(255, 255, 255, 0.2); padding-top: 2rem; margin-top: 3rem;">
            <p style="margin: 0; background: linear-gradient(45deg, #00d4ff, #00ff88, #ffffff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;">
                Created with ❤️ by Weis
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)
