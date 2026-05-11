import requests
import json
import re

url = "https://app.food2050.ch/de/v2/zfv/universitat-zurich,campus-zentrum/untere-mensa/mittagsverpflegung/menu/daily"

response = requests.get(url)

html = response.text

match = re.search(
    r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
    html
)

if not match:
    print("NO DATA FOUND")
    exit()

data = json.loads(match.group(1))

menu_items = (
    data["props"]["pageProps"]
    ["organisation"]["outlet"]["menuCategory"]
    ["categoryChildren"][0]["calendar"]["day"]["menuItems"]
)

meals = []

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

        name = dish["name"]

        prices = menu_item["prices"]

        student_price = None

        for price in prices:
            category_name = price["priceCategory"]["name"]

            if "Stud" in category_name:
                student_price = float(price["amount"])
                break

        meals.append({
            "category": category,
            "name": name,
            "price": student_price
        })

    except Exception as e:
        print("ERROR:", e)

# sort cheapest first
meals.sort(key=lambda x: x["price"])

print("\nCHEAPEST MEALS TODAY:\n")

for meal in meals:
    print(
        f"{meal['price']} CHF | "
        f"{meal['category']} | "
        f"{meal['name']}"
    )