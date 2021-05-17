from Klasser.producer import Producer # type: ignore
from Klasser.consumer import Consumer # type: ignore
from Klasser.product import Product # type: ignore
from Klasser.rekoring import RekoRing # type: ignore
from Klasser.event import Event # type: ignore

#skapa producent
August = Producer("August", "august@mail.com", "hej", "hejsan") 
Linnea = Producer("Linnea", "linnea@mail.com", "hej", "hejsan")

#skapa konsument
Mårten = Consumer("Mårten", "mårten@mail.com") 

#skapa produkter
gurka = Product("Gurka", "20", August)
gurka.set_quantity(20)
potatis = Product("Potatis", "15", August)
potatis.set_quantity(15)

lammfile = Product("Lammfile", 150, Linnea)
lammfile.set_quantity(0)

print("")
print("")
print(gurka)
print(potatis)
print(lammfile)

#köp tre gurkor
#Mårten.add_x_products(gurka, "3")
print(Mårten.print_cart_products())

Mårten.add_one_product(lammfile)

#köp 3 till gurkor, och 7 potatisar
#Mårten.add_x_products(gurka, "6")
Mårten.add_x_products(potatis, "7")
Mårten.add_x_products(lammfile, "3")
print("")
print("")

Mårten.add_one_product(lammfile)
Mårten.add_one_product(gurka)
Mårten.add_one_product(gurka)
Mårten.add_one_product(gurka)
Mårten.add_one_product(gurka)
Mårten.add_one_product(gurka)

print(Mårten.print_cart_products())
print(Mårten.get_producers())
print("")
print("")
print(gurka)
print(potatis)
print(lammfile)
#skapa rekoring
# chalmers = RekoRing("Chalmers", "Västra Götaland", "Chalmers parkering", "19.00")
# #lägg till august i ringen
# chalmers.add_producer(August)
# chalmers.add_producer(Linnea)
# print(chalmers.get_joined_producers())

# chalmers_torsdag = Event("13/5", chalmers)

# chalmers_torsdag.add_attending_producer(August)
# chalmers_torsdag.add_attending_producer(Linnea)

# l = chalmers_torsdag.get_attending_producers()
# for producer in l:
#     print(producer.get_name())



