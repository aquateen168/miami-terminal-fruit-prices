import requests
from datetime import datetime
import os
import pdfplumber
import pandas as pd

def download_latest_miami_fruit_prices():
    url = "https://www.ams.usda.gov/mnreports/mh_fv010.pdf"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        reports_dir = "reports"
        os.makedirs(reports_dir, exist_ok=True)
        
        filename = f"{reports_dir}/miami_fruit_prices_{date_str}.pdf"
        
        with open(filename, "wb") as f:
            f.write(response.content)
        
        print(f"✅ Downloaded: {filename}")
        return filename
        
    except Exception as e:
        print(f"❌ Error downloading report: {e}")
        return None

def extract_key_prices(pdf_path):
    """Optional: Extract banana & other fruit prices to CSV"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
        
        # Simple keyword search for bananas and common items
        lines = text.split("\n")
        relevant = [line for line in lines if any(kw in line.upper() for kw in 
                   ["BANANA", "PLANTAIN", "BERRY", "BLUEBERRY", "STRAWBERRY", "CITRUS", "MANGO"])]
        
        if relevant:
            df = pd.DataFrame({"Price_Line": relevant})
            csv_name = pdf_path.replace(".pdf", "_prices.csv")
            df.to_csv(csv_name, index=False)
            print(f"📊 Extracted key prices to: {csv_name}")
            
    except Exception as e:
        print(f"Note: Could not parse PDF (still saved): {e}")

if __name__ == "__main__":
    pdf_file = download_latest_miami_fruit_prices()
    if pdf_file:
        extract_key_prices(pdf_file)
