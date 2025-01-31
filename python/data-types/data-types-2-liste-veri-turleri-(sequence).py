# Sequence Types = list, tuple, range (siralama veri turleri)

myList = ["Apple", "Grappe", "Cherry", "Lemon", "Banana"] # list veri turu boyle kullanilir syntax'i boyledir.
myTuple = ("Red", "Blue", "Green") # aslinda bu da bir liste turudur ama icindeki veriler degistirelemez. Degistirmek icin tuple list veri turune cevirebiliriz.
myRange = range(7) # yazdigimiz sayinin bir azi kadar sayiyi listeler.

print(myList)
print(type(myList))

print(myTuple)
print(type(myTuple))

print(myRange) # boyle yazarsak sayinin araligini verir ama alttaki gibi yazarsak sayilari o zaman siralar
print(*myRange)
print(type(myRange))