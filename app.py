from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="REKO")

# Sida för att visa vilka produkter man har, länkt till lägga till ny produkt, länk till uppdatera befintilig produkt
@app.route("/manage_product", methods=["GET", "POST"])
def manage_product():
    return render_template("manage_product.html", title="Hantera produkt")


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    return render_template("add_product.html")

#denna sida skall ta info från vald produkt och visa för justering
@app.route("/update-product", methods=["GET", "POST"])
def update_product():
    return render_template("update_product.html", title="Uppdatera till produkt")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", title="Login")

if __name__ == "__main__":
    app.run(debug=True)