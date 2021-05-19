from Klasser.product import Product # type: ignore
from Klasser.consumer import Consumer # type: ignore
from Klasser.producer import Producer # type: ignore
from Klasser.rekoring import RekoRing # type: ignore
from Klasser.event import Event # type: ignore

# skapa en .py fil för att initiera lite grund data

# - 2 producenter
#         self.__name = name
#         self.__email = email
#         self.__description = description
#         self.__presentation = presentation
producenter = []
# - 2 ringar
rekoringar = []
# - 2 användare
        # self.__name = name
        # self.__email = email
användare = []
# - 5 produkter för varje producent
#         self.__name = name
#         self.__price = price
#         self.__producer = producer
#         self.__description = description
#         self.__quantity = None
produkter = []

event = []

a = Producer("Håkans potatisar", "hakan@potatis.se", "Håkan odlar potatisar","")
producenter.append(a)
a = Producer("Nettans kakor", "nettan@kakor.se", "Nettan bakar med kärlek","")
producenter.append(a)

c = Product("Potatisar", 9, producenter[0], "1 kg")
c.set_quantity(10)
produkter.append(c)
c = Product("Potatisar", 9, producenter[0], "2 kg")
c.set_quantity(5)
produkter.append(c)
c = Product("Potatisar", 9, producenter[0], "3 kg")
c.set_quantity(3)
produkter.append(c)
c = Product("Drömmar", 22, producenter[1], "20 stycken i en burk")
c.set_quantity(12)
produkter.append(c)
c = Product("Chokladboll", 7, producenter[1], "Säljes styckvis")
c.set_quantity(50)
produkter.append(c)
c = Product("Havreflarn", 35, producenter[1], "500gr")
c.set_quantity(25)
c.set_is_for_sale(False)
produkter.append(c)
c = Product("Kanelbullar", 20, producenter[1], "Fyra bullar per påse")
c.set_quantity(17)
produkter.append(c)
c = Product("Pepparkakor", 12, producenter[1], "250gr")
c.set_quantity(13)
produkter.append(c)


d = RekoRing("Chalmers", "Västra Götaland", "Chalmers parkering", "19.00")
rekoringar.append(d)
d = RekoRing("Backaplan", "Västra Götaland", "Backaplans parkering", "18.30")
rekoringar.append(d)
d = RekoRing("Floda", "Västra Götaland", "Floda centrum", "20.00")
rekoringar.append(d)

e = Event("13/5", rekoringar[0])
event.append(e)
e = Event("13/5", rekoringar[1])
event.append(e)
e = Event("20/5", rekoringar[2])
event.append(e)

b = Consumer("Bo Jansson", "bo.jansson@exempel.se")
användare.append(b)
b.add_x_products(produkter[0],3)
b.add_x_products(produkter[5],2)
b.make_purchase()

b = Consumer("Rita Karlsson", "rita.karlsson56@.com")
användare.append(b)
b.add_x_products(produkter[0],3)
b.make_purchase()