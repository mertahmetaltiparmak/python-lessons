# bytearray ile bytes arasindaki fark bytearray degistirilebilirken bytes degistirilemez.

# bytes tanimlama islemi asagadaki halde olur.
name = b"Mert" # icine sadece ASCII karakter tablosundaki karakterler girilebilir.
# eger turkce karakter veya ASCII'de olmayana bir karakter girmek istersek asagadaki gibi yapabiliriz.
Name = bytes("ş", "utf-8")

print(Name)
print(type(name))

print(name)
print(type(name))