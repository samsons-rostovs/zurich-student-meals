# Zurich Student Meals

A Python-based meal aggregation system that collects and ranks the cheapest student lunch options across ETH Zürich and UZH cafeterias.

## Features

- Aggregates meals from multiple ETH Zürich and UZH mensas
- Automatically extracts student pricing information
- Sorts meals by cheapest price
- Sends automated email notifications
- Supports scheduled execution using cron
- Uses reverse-engineered APIs and structured JSON extraction

## Supported Mensas

### UZH
- Untere Mensa
- Obere Mensa

### ETH Zürich
- Polyterrasse
- Food&Lab
- Archimedes

## Example Output

```text
CHEAPEST MEALS IN ZURICH:

6.1 CHF | Untere Mensa UZH | garden | CURRYWURST
6.1 CHF | Obere Mensa UZH | farm | CANNELONI
7.0 CHF | ETH Polyterrasse | GARDEN | Spargel Risotto
7.9 CHF | Food&Lab | Pasta | PASTA PLAUSCH
```

## Project Structure

```text
zurich-student-meals/
├── main.py
├── emailer.py
├── scrapers/
│   ├── eth.py
│   └── uzh.py
├── .env
├── README.md
└── requirements.txt
```

## Installation

### Clone the repository

```bash
git clone https://github.com/samsons-rostovs/zurich-student-meals.git
cd zurich-student-meals
```

### Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_google_app_password
RECEIVER_EMAIL=your_email@gmail.com
```

## Running the Project

```bash
python3 main.py
```

## Cron Automation

Example cron configuration for weekday execution at 10:30:

```cron
30 10 * * 1-5 /path/to/venv/bin/python3 /path/to/zurich-student-meals/main.py
```

## Technical Highlights

- Reverse-engineered undocumented ETH Zürich and UZH menu APIs
- Extracted structured data from heterogeneous web systems
- Implemented modular scraping architecture
- Automated ranking and notification pipeline
- Built using Python, requests, BeautifulSoup, SMTP, and JSON parsing

## Future Improvements

- Telegram bot integration
- Dynamic date handling
- Web dashboard
- Historical meal price tracking
- Protein/calorie ranking
- Additional Zurich food providers
