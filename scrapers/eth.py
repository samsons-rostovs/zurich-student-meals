import requests
from datetime import datetime, timedelta


ETH_MENSAS = {
    "ETH Polyterrasse": 9,
    "Food&Lab": 7,
    "Archimedes": 8
}


def scrape_eth_mensas():

    meals = []

    current_date = datetime.today()

    valid_after = current_date.strftime("%Y-%m-%d")

    valid_before = (
        current_date + timedelta(days=7)
    ).strftime("%Y-%m-%d")

    for mensa_name, facility_id in ETH_MENSAS.items():

        url = (
            "https://idapps.ethz.ch/cookpit-pub-services/v1/weeklyrotas"
            f"?client-id=ethz-wcms"
            f"&lang=de"
            f"&rs-first=0"
            f"&rs-size=50"
            f"&valid-after={valid_after}"
            f"&valid-before={valid_before}"
            f"&facility={facility_id}"
        )

        response = requests.get(url)

        data = response.json()

        weekly_rotas = data["weekly-rota-array"]

        for rota in weekly_rotas:

            rota_valid_from = rota.get("valid-from")
            rota_valid_to = rota.get("valid-to")

            if not (
                rota_valid_from <= valid_after <= rota_valid_to
            ):
                continue

            days = rota.get("day-of-week-array", [])

            for day in days:

                today_weekday = datetime.today().isoweekday()

                if day.get("day-of-week-code") != today_weekday:
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

                        if "abend" in meal_time_name:
                            continue

                        if "smoothie" in meal_time_name:
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

                            category_name = line.get(
                                "name",
                                "Unknown"
                            )

                            lower_name = name.lower()
                            lower_category = category_name.lower()

                            if "smoothie" in lower_name:
                                continue

                            if "smoothie" in lower_category:
                                continue

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
                                "category": category_name,
                                "name": name,
                                "price": student_price
                            })

    return meals