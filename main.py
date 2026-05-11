from scrapers.uzh import scrape_uzh_mensa
from scrapers.eth import scrape_eth_mensas
from emailer import send_email

MENSAS = {
    "Untere Mensa UZH":
        "https://app.food2050.ch/de/v2/zfv/universitat-zurich,campus-zentrum/untere-mensa/mittagsverpflegung/menu/daily",

    "Obere Mensa UZH":
        "https://app.food2050.ch/de/v2/zfv/universitat-zurich,campus-zentrum/obere-mensa/mittagsverpflegung/menu/daily"
}

all_meals = []

for mensa_name, url in MENSAS.items():

    meals = scrape_uzh_mensa(mensa_name, url)

    all_meals.extend(meals)
eth_meals = scrape_eth_mensas()
all_meals.extend(eth_meals)

all_meals.sort(key=lambda x: x["price"])

print("\nCHEAPEST MEALS IN ZURICH:\n")

for meal in all_meals:
    print(
        f"{meal['price']} CHF | "
        f"{meal['mensa']} | "
        f"{meal['category']} | "
        f"{meal['name']}"
    )

send_email(all_meals)