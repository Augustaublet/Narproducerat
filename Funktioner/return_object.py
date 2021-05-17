from Klasser.consumer import Consumer # type: ignore
from Klasser.event import Event # type: ignore
from Klasser.producer import Producer # type: ignore
from Klasser.product import Product # type: ignore
from Klasser.rekoring import RekoRing # type: ignore
from Klasser.shopping_cart import ShoppingCart # type: ignore

from testobjekt import produkter, rekoringar, användare, producenter

object_list = []
object_list.append(produkter)
object_list.append(rekoringar)
object_list.append(användare)
object_list.append(producenter)

def return_object(id):
    for list in object_list:
        for object in list:
            if int(object.get_id()) == int(id):
                return object

