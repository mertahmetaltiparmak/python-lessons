# variable birden fazla degisken yazdirma

x = "Python"
y = "is"
z = "mid"
# ucunu boyle de yazdirabiliriz
print(x,y,z)
# veya boylede ama bu asagadakinden variable turu ayni olmali ve stringlerde arasindaki bosluk gidiyor. (+ icin gecerli ayni tur olmasi)
print(x+y+z)
# eger bu variable'imizin turu int veya float olsaydi bu sefer sayilarin toplamini yazardi mesela
a,b = 5,7
print(a+b) # cikti = 12