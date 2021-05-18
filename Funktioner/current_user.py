from Klasser.consumer import Consumer # type: ignore
from Klasser.event import Event # type: ignore
from Klasser.producer import Producer # type: ignore
from Klasser.product import Product # type: ignore
from Klasser.rekoring import RekoRing # type: ignore
from Klasser.shopping_cart import ShoppingCart # type: ignore

from testobjekt import produkter, rekoringar, användare, producenter

def user_type(user_id):
    for objekt in användare:
        if objekt.get_id() == user_id:
            return "consumer"
    for objekt in producenter:
        if objekt.get_id() == user_id:
            return "producer"

