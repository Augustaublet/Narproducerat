from Klasser.producer import * 
from Klasser.consumer import * 
from Klasser.product import * 
from Klasser.rekoring import * 
from Klasser.event import * 

#skapa producent
August = Producer("August", "august@mail.com", "hej", "hejsan") 

#skapa konsument
Mårten = Consumer("Mårten", "mårten@mail.com") 

#skapa produkter
gurka = Product("Gurka", "20", August)
potatis = Product("Potatis", "15", August)

print(gurka)
print(potatis)


#köp tre gurkor
Mårten.buy_product(gurka, "3")
print(Mårten.get_cart_list())


#köp 3 till gurkor, och 7 potatisar
Mårten.buy_product(gurka, "6")
Mårten.buy_product(potatis, "7")

print(Mårten.print_cart_products())

#skapa rekoring
chalmers = RekoRing("Chalmers", "Västra Götaland", "Chalmers parkering", "19.00")
#lägg till august i ringen
chalmers.add_producer(August)
print(chalmers.get_joined_producers())

chalmers_torsdag = Event("13/5", chalmers)

chalmers_torsdag.add_attending_producer(August)

l = chalmers_torsdag.get_attending_producers()
print(l[0].get_name())



