from Motocicleta import Motocicleta
mymotorbike = Motocicleta("white", "qwe123")
mymotorbike.start()
mymotorbike.stop()
mymotorbike2 = Motocicleta(wheels=2, fuel=10)
mymotorbike.start()
mymotorbike2.start()
mymotorbike.stop()
mymotorbike2.stop()
mymotorbike.price = "$1000000"
mymotorbike.showprice()
mymotorbike2.showprice()