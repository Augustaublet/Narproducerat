from flask import Flask, render_template, url_for, request, flash
from Klasser.product import Product
from testobjekt import produkter, rekoringar
from testobjekt import producenter
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

# Sida för att visa vilka produkter man har, länkt till lägga till ny produkt, länk till uppdatera befintilig produkt
@app.route("/manage_product", methods=["GET", "POST"])
def manage_product():
    return render_template("manage_product.html", products=produkter)

@app.route("/set_ring", methods=["GET","POST"])
def set_ring():
    if request.method == "POST":
        current_ring = request.form.get("set_ring")
        return render_template("consumer_shopping.html",products=produkter, producers=producenter, current_ring=current_ring)

    return render_template("set_ring.html", ringar = rekoringar)

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        namn = request.form.get("productName")
        pris = request.form.get("productPrice")
        description = request.form.get("productDescription")
        isForSale = request.form.get("isForSale")
        ny_produkt = Product(namn, pris,"Producent", description, isForSale)
        produkter.append(ny_produkt)
        return render_template("manage_product.html", products=produkter)

    return render_template("add_product.html", producers = producenter)

#denna sida skall ta info från vald produkt och visa för justering
@app.route("/update-product", methods=["GET", "POST"])
def update_product():
    return render_template("update_product.html")

@app.route("/handla", methods=["GET", "POST"])
def consumer_shopping():
    if request.method == "POST":
        current_ring = request.form.get("set_ring")
        return render_template("consumer_shopping.html",products=produkter, producers=producenter, current_ring=current_ring)

    current_ring= "Välj en ring"
    return render_template("consumer_shopping.html", products=produkter, producers=producenter, ringar=rekoringar, current_ring=current_ring)

@app.route("/buy-product", methods=["POST"])
def buy_product():
    productjson = json.loads(request.data)
    product_info = productjson["test"]
    print(product_info)
    print("hej")

@app.route("/varukorg", methods=["GET", "POST"])
def shoppingCart():
    return render_template("shoppingCart.html", products=produkter)

if __name__ == "__main__":
    app.run(debug=True)