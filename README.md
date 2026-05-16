# Ekantipur Scraper

A Python web scraping project that uses Playwright to extract the latest entertainment news from Ekantipur and save the results in JSON format.

The scraper collects:

- Top 5 entertainment news articles from Ekantipur
- Cartoon of the Day

---

## 📌 Features

- Automated browser scraping using Playwright
- Extracts latest entertainment news headlines
- Extracts Cartoon of the Day
- Saves structured output to `output.json`
- Lightweight and beginner-friendly project

---

## 🛠 Tech Stack

- Python
- Playwright

---

## 📂 Project Structure

```bash
ekantipur-scraper/
│
├── scraper.py          # Main scraping script
├── output.json         # Extracted output data
├── requirements.txt    # Project dependencies
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ekantipur-scraper.git
cd ekantipur-scraper
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Usage

Run the scraper using:

```bash
python scraper.py
```

After successful execution, the extracted data will be saved to:

```bash
output.json
```

---

## 📄 Example Output

```json
{
    "entertainment_news": [
        {
            "title": "‘गरिबको चमेली’ : बालेनले गाए, बालेनतिरै फर्कियो",
            "image_url": "https://assets-cdn-api.ekantipur.com/thumb.php?src=https://assets-cdn.ekantipur.com/uploads/source/news/kantipur/2026/miscellaneous/sukumbashiprotestatmaitighar202605084266-1252026110024-1000x0.jpg&w=701&h=0",
            "category": "मनोरञ्जन",
            "author": "रीना मोक्तान"
        },
  ],
    "cartoon_of_the_day": {
        "title": null,
        "image_url_cartoon": "https://assets-cdn-api.ekantipur.com/thumb.php?src=https://assets-cdn.ekantipur.com/uploads/source/news/kantipur/2022/third-party/gajab-chha-ba-830128-copy-1252026050359-1000x0.jpg&w=601&h=0",
        "author": null
    }
}
```

---

## 🎯 Learning Objectives

This project demonstrates:

- Web scraping with Playwright
- Extracting structured data from websites
- Working with JSON files in Python
- Automating browser interactions

---

## ⚠️ Disclaimer

This project is created for educational purposes only. Please respect the website's Terms of Service and robots.txt policies before scraping.

---

## 👨‍💻 Author

Developed by Rabin Dhakal
