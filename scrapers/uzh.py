import requests
import json
import re


def scrape_uzh_mensa(mensa_name, url):

    meals = []

    response = requests.get(url)

    html = response.text

    match = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
        html
    )

    if not match:
        print(f"NO DATA FOUND FOR {mensa_name}")
        return meals

    data = json.loads(match.group(1))

    menu_items = (
        data["props"]["pageProps"]
        ["organisation"]["outlet"]["menuCategory"]
        ["categoryChildren"][0]["calendar"]["day"]["menuItems"]
    )

    for item in menu_items:

        category = item["category"]["name"]

        detail_url = item["detailUrl"]

        detail_response = requests.get(detail_url)

        detail_html = detail_response.text

        detail_match = re.search(
            r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
            detail_html
        )

        if not detail_match:
            continue

        detail_data = json.loads(detail_match.group(1))

        try:
            menu_item = (
                detail_data["props"]["pageProps"]
                ["organisation"]["outlet"]["menuCategory"]
                ["menuItem"]
            )

            dish = menu_item["dish"]

            name = dish["name"].split(",")[0]

            prices = menu_item["prices"]

            student_price = None

            for price in prices:
                category_name = price["priceCategory"]["name"]

                if "Stud" in category_name:
                    student_price = float(price["amount"])
                    break

            if student_price is not None:
                meals.append({
                    "mensa": mensa_name,
                    "category": category,
                    "name": name,
                    "price": student_price
                })

        except Exception as e:
            print("ERROR:", e)

    return meals