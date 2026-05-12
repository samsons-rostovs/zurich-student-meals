import json
import os
import time

from flask import Flask, render_template

from scrapers.uzh import scrape_uzh_mensa
from scrapers.eth import scrape_eth_mensas


app = Flask(__name__)


CACHE_FILE = "data/meals.json"

CACHE_DURATION = 900


MENSAS = {
    "Untere Mensa UZH":
        "https://app.food2050.ch/de/v2/zfv/universitat-zurich,campus-zentrum/untere-mensa/mittagsverpflegung/menu/daily",

    "Obere Mensa UZH":
        "https://app.food2050.ch/de/v2/zfv/universitat-zurich,campus-zentrum/obere-mensa/mittagsverpflegung/menu/daily"
}


def generate_cache():

    print("UPDATING CACHE...")

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

    os.makedirs(
        "data",
        exist_ok=True
    )

    with open(
        CACHE_FILE,
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


def cache_expired():

    if not os.path.exists(CACHE_FILE):
        return True

    modified_time = os.path.getmtime(
        CACHE_FILE
    )

    age = time.time() - modified_time

    return age > CACHE_DURATION


@app.route("/")
def home():

    if cache_expired():
        generate_cache()

    with open(
        CACHE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        meals = json.load(file)

    return render_template(
        "index.html",
        meals=meals
    )


if __name__ == "__main__":
    app.run(debug=True)