import json

from scrapers.uzh import scrape_uzh_mensa
from scrapers.eth import scrape_eth_mensas


MENSAS = {
    "Untere Mensa UZH":
        "https://app.food2050.ch/de/v2/zfv/universitat-zurich,campus-zentrum/untere-mensa/mittagsverpflegung/menu/daily",

    "Obere Mensa UZH":
        "https://app.food2050.ch/de/v2/zfv/universitat-zurich,campus-zentrum/obere-mensa/mittagsverpflegung/menu/daily"
}


all_meals = []


for mensa_name, url in MENSAS.items():

    meals = scrape_uzh_mensa(
        mensa_name,
        url
    )

    all_meals.extend(meals)


eth_meals = scrape_eth_mensas()

all_meals.extend(eth_meals)


all_meals.sort(
    key=lambda x: x["price"]
)


with open(
    "data/meals.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        all_meals,
        file,
        ensure_ascii=False,
        indent=4
    )


print("CACHE UPDATED!")