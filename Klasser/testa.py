from producer import *
from consumer import *
from product import *

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