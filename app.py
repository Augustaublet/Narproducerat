from flask import Flask, render_template, url_for, request, flash, redirect, session
from Klasser.product import Product
from testobjekt import produkter, rekoringar, användare, producenter
from Funktioner.return_object import get_object
import json
import time

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
    return render_template("sign_up.html", user=get_object(session["current_user"]))

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", user=get_object(session["current_user"]))



@app.route("/set_ring", methods=["GET","POST"])
def set_ring():
    if request.method == "POST":
        session["current_ring"] = request.form.get("set_ring")
        return redirect(url_for("consumer_shopping"))
    return render_template("set_ring.html", ringar = rekoringar, user=get_object(session["current_user"]))


# Sida för att visa vilka produkter man har, länkt till lägga till ny produkt, länk till uppdatera befintilig produkt
@app.route("/manage_product", methods=["GET", "POST"])
def manage_product():    
    return render_template("manage_product.html", products=produkter, user=get_object(session["current_user"]))

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    user=get_object(session["current_user"])
    if request.method == "POST":
        namn = request.form.get("productName")
        pris = request.form.get("productPrice")
        description = request.form.get("productDescription")
        isForSale = request.form.get("isForSale")
        ny_produkt = Product(namn, pris, user.get_name(), description, isForSale)
        produkter.append(ny_produkt)
        return redirect(url_for("manage_product"))

    return render_template("add_product.html", producers = producenter, user=user)

#denna sida skall ta info från vald produkt och visa för justering
@app.route("/update-product", methods=["GET", "POST"])
def update_product():
    return render_template("update_product.html", user=get_object(session["current_user"]))

@app.route("/handla", methods=["GET", "POST"])
def consumer_shopping() :
    current_ring=session["current_ring"]     
    if request.method == "POST":
        if request.form.get("add_cart"):
            add_cart = request.form.get("add_cart")
            product = get_object(add_cart)
            user = get_object(session["current_user"])
            user.add_one_product(product)
        if request.form.get("set_ring"):
            session["current_ring"] = request.form.get("set_ring")
            current_ring= session["current_ring"]
            return redirect(url_for("consumer_shopping"))
    return render_template("consumer_shopping.html", products=produkter, producers=producenter, ringar=rekoringar, current_ring=current_ring, user=get_object(session["current_user"]))

@app.route("/varukorg", methods=["GET", "POST"])
def shoppingCart():
    user = get_object(session["current_user"])
    if request.method == "POST":
        if request.form.get("buy_cart"):
            user.make_purchase()
            flash('Tack för din beställning!', category='success')
    return render_template("shoppingCart.html", current_ring=session["current_ring"], user=user)
            

@app.route("/my_order", methods=["GET","POST"])
def my_order():
    if request.method == "POST":
        test= request.form.get("test")
        print(test)
    user=get_object(session["current_user"])
    return render_template("my_order.html", current_ring=session["current_ring"], user=user)

@app.route("/beställningar")
def incoming_orders():
    user=get_object(session["current_user"])
    orders={}
    for consumer in användare:
        orders[consumer]=consumer.get_last_order()
    # print(orders.items())
    
    # orders=get_ordered_from_producer(user,användare)
    
    return render_template("incoming_orders.html", user=user, orders=orders, consumer=användare)

if __name__ == "__main__":
    app.run(debug=True)