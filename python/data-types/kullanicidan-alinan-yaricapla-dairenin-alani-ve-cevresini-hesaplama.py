# dairenin cevresi = 2 * pi * r
# dairenin alani = pi * r * r
# pi = 3.14159

pi = 3.14159
# kullanicadan girdi almak icin input() fonksiyonunu kullaniyoruz.
radius_of_circle = float(input("Yari Cap: ")) # dairenin alanini ondalikli sayi girme ihtimalimize karsi float icinde yazdik yoksa float'siz yazardik.

area_of_circle = pi * radius_of_circle * radius_of_circle
circumference_of_circle = 2 * pi * radius_of_circle

print("Alan: ", area_of_circle)
print("Cevre: ", circumference_of_circle)