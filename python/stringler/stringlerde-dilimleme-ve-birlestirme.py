# stringlerde dilimleme

text = "Python is weird"
print(text[1:5]) # 1.den baslatip 4'u karaktere kadar yazdiriyor. Cikti: ytho
# eger baslangic degeri verilmezse en bastan baslar. son deger verilmessede sonuna kadar gider.

# sonundan baslamak icinse - kullanilir ornek:
# bu sefer sondan saymaya baslar sondaki ilk karakter 0 sonra -1 diye devam eder
print(text[-5:]) # son bes karakteri aldi cikti: weird ; eger basina -1 yazsaydik -5'ten -1 kadar yani d'yi yazmazdi.

# stringlerde birlestirme

txt = "Python"
txt2 = "is weird"

result = txt + " " + txt2

print(result)