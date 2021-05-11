from Klasser.product import Product
from Klasser.consumer import Consumer
from Klasser.producer import Producer

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

a = Producer("Håkans potatisar", "hakan@potatis.se", "Håkan odlar potatisar","")
producenter.append(a)
a = Producer("Nettans kakor", "nettan@kakor.se", "Nettan bakar med kärlek","")
producenter.append(a)

b = Consumer("Bo Jansson", "bo.jansson@telia.se")
användare.append(b)
b = Consumer("Rita Karlsson", "rita.karlsson56@gmail.com")
användare.append(b)

c = Product("Potatisar", 9, "Håkans potatisar", "1 kg")
c.set_quantity(10)
produkter.append(c)
c = Product("Potatisar", 9, "Håkans potatisar", "2 kg")
c.set_quantity(5)
produkter.append(c)
c = Product("Potatisar", 9, "Håkans potatisar", "3 kg")
c.set_quantity(3)
produkter.append(c)
c = Product("Drömmar", 22, "Nettans kakor", "20 stycken i en burk")
c.set_quantity(12)
produkter.append(c)
c = Product("Chokladboll", 7, "Nettans kakor", "Säljes styckvis")
c.set_quantity(50)
produkter.append(c)
c = Product("Havreflarn", 35, "Nettans kakor", "500gr")
c.set_quantity(25)
produkter.append(c)
c = Product("Kanelbullar", 20, "Nettans kakor", "Fyra bullar per påse")
c.set_quantity(17)
produkter.append(c)
c = Product("Pepparkakor", 12, "Nettans kakor", "250gr")
c.set_quantity(13)
produkter.append(c)