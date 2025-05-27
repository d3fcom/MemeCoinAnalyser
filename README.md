# 🚀Open Source,  MEME Coin Analyzer 

Visit the live demo: [MEME Coin Analyzer](https://memecoinanalyser.streamlit.app/)

A beautiful, modern web application for analyzing MEME cryptocurrency data with real-time price tracking, market metrics, and technical indicators. Built on Flask using Python.

![MEME Coin Analyzer](https://img.shields.io/badge/Status-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.11+-blue) ![FLASK](https://img.shields.io/badge/Flask_Python-green)

## ✨ Features

- **Real-time MEME coin data** from DEXscreener API
- **Beautiful Dark theme
- **Mobile-responsive design** that works on all devices
- **Multiple coin comparison** in a clean table format
- **Technical indicators** including MACD, RSI, and Bollinger Bands
- **CSV export functionality** for data analysis
- **Clean, modern UI** with glowing effects and smooth animations

## 📊 What You Can Track

- Current coin prices in USD
- 24-hour trading volume
- Market capitalization
- Liquidity data
- 24-hour price changes
- Symbol and coin name information

## 🚀 Quick Start

### Option 1: Try it Online
Visit the live demo: [MEME Coin Analyzer](https://memecoinanalyser.streamlit.app/)

### Option 2: Run Locally

#### Prerequisites
- Python 3.11 or higher
- pip package manager

#### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/d3fcom/MemeCoinAnalyser
   cd memecoinanalyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser**
    Navigate to `http://localhost:` (+ port number "if needed ") to view the app

## 📋 Requirements

Create a `requirements.txt` file with:
```
streamlit>=1.38.0
plotly>=5.24.1
requests>=2.32.3
pandas>=2.2.3
ta>=0.11.0
```

## 🎯 How to Use

1. **Enter coin data**: Input MEME coin contract addresses or symbols (one per line)
2. **Click "Analyze"**: The app will fetch real-time data from DEXscreener
3. **View results**: See a comprehensive comparison table with all key metrics
4. **Export data**: Download results as CSV for further analysis

### Example Input
```
PEPE COIN
0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE

```

## 🛠️ Built With

- **[Streamlit](https://streamlit.io/)** - Web app framework
- **[Plotly](https://plotly.com/)** - Interactive charts and graphs
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[TA-Lib](https://github.com/bukosabino/ta)** - Technical analysis indicators
- **[DEXscreener API](https://docs.dexscreener.com/)** - Real-time cryptocurrency data

## 🚀 Deployment

### Streamlit Community Cloud
1. Fork this repository
2. Connect your GitHub repo to [Streamlit Cloud](https://share.streamlit.io/)
3. Deploy with one click!

### Other Platforms
This app can be deployed on:
- Heroku
- Railway
- Vercel
- Any platform supporting Python apps

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Data provided by [DEXscreener](https://dexscreener.com/)
- Built with love using [Streamlit](https://streamlit.io/)
- Inspired by the vibrant MEME coin community

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/memecoinanalyzer/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your setup and the error

## ⭐ Show Your Support

If you found this project helpful, please give it a star! It helps others discover the project.

---

**Created with ❤️ by Weis**

*Bringing beautiful data visualization to the MEME coin universe!*
