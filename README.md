# Zurich Student Meals

A full-stack meal aggregation platform that collects, ranks, caches, and serves the cheapest student lunch options across ETH Zürich and UZH cafeterias.

## Live Demo

🌐 Deployed web app:

Zurich Student Meals – https://zurich-student-meals.onrender.com

## Features

- Aggregates meals from multiple ETH Zürich and UZH mensas
- Automatically extracts student pricing information
- Sorts meals by cheapest price
- Fast cached backend architecture using JSON caching
- Interactive Flask web dashboard
- Live meal search and filtering
- Clickable meal cards linking to official ETH/UZH pages
- Automated email notifications
- Scheduled GitHub Actions automation
- Reverse-engineered APIs and structured JSON extraction
- Modern responsive UI using Tailwind CSS

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

## Web Dashboard

The project now includes a deployed Flask web application with:

- Real-time meal search
- Category badges and icons
- Responsive card-based UI
- Automatic cache invalidation
- Official mensa links
- ETH + UZH integration

## Project Structure

```text
zurich-student-meals/
├── app.py
├── main.py
├── update_cache.py
├── emailer.py
├── data/
│   └── meals.json
├── scrapers/
│   ├── eth.py
│   └── uzh.py
├── templates/
│   └── index.html
├── .github/workflows/
│   └── daily_meals.yml
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
RECEIVER_EMAIL=email1@gmail.com,email2@gmail.com
```

## Running the Web App

```bash
python update_cache.py
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Deployment

The project is deployed using:

- Render (Flask hosting)
- GitHub Actions (scheduled automation)
- Gunicorn (production WSGI server)

## Technical Highlights

- Reverse-engineered undocumented ETH Zürich and UZH menu APIs
- Built a modular multi-source scraping architecture
- Implemented automatic cache invalidation for performance optimization
- Designed a responsive Tailwind-powered frontend
- Added live client-side filtering with JavaScript
- Automated scheduled scraping and notifications using GitHub Actions
- Implemented cloud deployment using Render and Gunicorn

## Future Improvements

- Telegram bot integration
- Historical meal price tracking
- Nutrition/protein ranking
- Public JSON API endpoint
- Interactive charts and statistics
- Additional Zurich food providers
- Personalized meal recommendations
