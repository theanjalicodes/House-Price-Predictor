from flask import Flask, render_template, request

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    form_data = {
        "area": "",
        "bedrooms": "",
        "bathrooms": "",
        "city": "",
        "house_type": "Apartment"
    }

    if request.method == "POST":

        area = int(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        city = request.form["city"]
        house_type = request.form["house_type"]

        form_data = {
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "city": city,
            "house_type": house_type
        }

        price = area * 3000
        price += bedrooms * 500000
        price += bathrooms * 300000

        if house_type == "Villa":
            price += 2000000
        elif house_type == "Independent House":
            price += 1000000

        if price < 5000000:
            category = "Budget House"
        elif price < 10000000:
            category = "Premium House"
        else:
            category = "Luxury House"

        loan_amount = int(price * 0.8)
        emi = int(loan_amount * 0.0085)

        result = {
            "price": f"{price:,}",
            "category": category,
            "loan_amount": f"{loan_amount:,}",
            "emi": f"{emi:,}",
            "city": city,
            "house_type": house_type
        }

        history.insert(0, {
            "city": city,
            "price": f"₹ {price:,}"
        })

        if len(history) > 5:
            history.pop()

    return render_template(
        "index.html",
        result=result,
        history=history,
        form_data=form_data
    )

if __name__ == "__main__":
    app.run(debug=True)