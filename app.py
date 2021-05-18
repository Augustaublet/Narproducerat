from flask import Flask, render_template, url_for, request, flash, redirect, session
from Klasser.product import Product
from testobjekt import produkter, rekoringar, användare, producenter
from Funktioner.return_object import get_object
import json

app = Flask(__name__)
app.secret_key= "dettaarentestnyckesomborandras"
current_user = None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form.get("user_select")
        for a in användare:
            name = a.get_name()
            stripped = name.split(" ", 1)[0]
            if user == stripped:
                session["current_user"]= a.get_id()
                return redirect(url_for("set_ring"))
        for p in producenter:
            name = p.get_name()
            stripped = name.split(" ", 1)[0]
            if user == stripped:
                session["current_user"] = p.get_id()
                return redirect(url_for("manage_product"))
    return render_template("index.html", consumers=användare, producers=producenter)

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")



@app.route("/set_ring", methods=["GET","POST"])
def set_ring():
    if request.method == "POST":
        session["current_ring"] = request.form.get("set_ring")
        return redirect(url_for("consumer_shopping"))
    return render_template("set_ring.html", ringar = rekoringar)


# Sida för att visa vilka produkter man har, länkt till lägga till ny produkt, länk till uppdatera befintilig produkt
@app.route("/manage_product", methods=["GET", "POST"])
def manage_product():    
    return render_template("manage_product.html", products=produkter, user=get_object(session["current_user"]))

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        namn = request.form.get("productName")
        pris = request.form.get("productPrice")
        description = request.form.get("productDescription")
        isForSale = request.form.get("isForSale")
        ny_produkt = Product(namn, pris,"Producent", description, isForSale)
        produkter.append(ny_produkt)
        return redirect(url_for("manage_product"))

    return render_template("add_product.html", producers = producenter)

#denna sida skall ta info från vald produkt och visa för justering
@app.route("/update-product", methods=["GET", "POST"])
def update_product():
    return render_template("update_product.html")

@app.route("/handla", methods=["GET", "POST"])
def consumer_shopping():
    if request.method == "POST":
        add_cart = request.form.get("add_cart")
        product = get_object(add_cart)
        user = get_object(session["current_user"])
        user.add_one_product(product)
    if request.form.get("set_ring"):
        session["current_ring"] = request.form.get("set_ring")
        return redirect(url_for("consumer_shopping"))
    return render_template("consumer_shopping.html", products=produkter, producers=producenter, ringar=rekoringar, current_ring=session["current_ring"])

@app.route("/varukorg", methods=["GET", "POST"])
def shoppingCart():
    user = get_object(session["current_user"])
    return render_template("shoppingCart.html", user=user)

@app.route("/my_order", methods=["GET","POST"])
def my_order():
    if request.method == "POST":
        pass
    user=get_object(session["current_user"])
    return render_template("my_order.html", user=user, orders=user.get_order_history())

if __name__ == "__main__":
    app.run(debug=True)