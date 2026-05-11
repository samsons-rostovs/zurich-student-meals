import requests
from datetime import datetime


ETH_MENSAS = {
    "ETH Polyterrasse": 9,
    "Food&Lab": 7,
    "Archimedes": 8
}


def scrape_eth_mensas():

    meals = []

    today = datetime.today().isoweekday()

    for mensa_name, facility_id in ETH_MENSAS.items():

        url = (
            "https://idapps.ethz.ch/cookpit-pub-services/v1/weeklyrotas"
            f"?client-id=ethz-wcms"
            f"&lang=de"
            f"&rs-first=0"
            f"&rs-size=50"
            f"&valid-after=2026-05-11"
            f"&valid-before=2026-05-18"
            f"&facility={facility_id}"
        )

        response = requests.get(url)

        data = response.json()

        weekly_rotas = data["weekly-rota-array"]

        for rota in weekly_rotas:

            days = rota.get("day-of-week-array", [])

            for day in days:

                if day["day-of-week-code"] != today:
                    continue

                opening_hours = day.get(
                    "opening-hour-array",
                    []
                )

                for opening in opening_hours:

                    meal_times = opening.get(
                        "meal-time-array",
                        []
                    )

                    for meal_time in meal_times:
                        meal_time_name = meal_time.get(
                            "name",
                            ""
                        ).lower()

                        # skip evening meals
                        if "abend" in meal_time_name:
                            continue

                        lines = meal_time.get(
                            "line-array",
                            []
                        )

                        for line in lines:

                            meal = line.get("meal")

                            if not meal:
                                continue

                            name = meal.get(
                                "name",
                                "Unknown"
                            )

                            # filter spam entries
                            lower_name = name.lower()

                            if "dessert" in lower_name:
                                continue

                            if "buffet" in lower_name:
                                continue

                            prices = meal.get(
                                "meal-price-array",
                                []
                            )

                            student_price = None

                            for price_info in prices:

                                if (
                                    price_info.get(
                                        "customer-group-desc-short"
                                    ) == "Stud."
                                ):

                                    student_price = float(
                                        price_info["price"]
                                    )

                                    break

                            if student_price is None:
                                continue

                            meals.append({
                                "mensa": mensa_name,
                                "category": line.get(
                                    "name",
                                    "Unknown"
                                ),
                                "name": name,
                                "price": student_price
                            })

    return meals