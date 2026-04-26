# Miami Terminal Market Fruit Prices Scraper

Automatically downloads the latest daily **Miami Terminal Market Fruit Prices** report (MH_FV010) from the official USDA source.

## Features
- Downloads the newest PDF every day
- Saves it with date stamp (`miami_fruit_prices_2026-04-26.pdf`)
- Optional: Extracts key prices (bananas, berries, citrus, etc.) to CSV
- Runs automatically via GitHub Actions (no server needed)
- Perfect for banana wholesalers & produce buyers monitoring Miami market

## Quick Start (Local)
```bash
git clone https://github.com/YOUR_USERNAME/miami-terminal-fruit-prices.git
cd miami-terminal-fruit-prices
pip install -r requirements.txt
python scraper.py
