# '' tek tirnagin icinde yazarken tek tirnak kullanmak icin escape sequance kullanilir asagidaki ornekte oldugu gibi
# hatirlatma ctrl k + c coklu komut satirana alma 
print('He is called \'big boy\'')

# stringler birer arraydir. ornek:
text = "Python"
# ayni arraylerde oldugu gibi 0. indeksten baslar.
print(text[0])

# stringler array oldugu icin bunlarla for dongusu kurabiliriz. ornek:,
txt = "Python is weird"
for x in txt:
    print(x)
# string'in uzunlugunu almak icin len() functionu kullanilir.
print("\n",len(text))

# belirli bir karakterin stringde bulunup bulunmadigini kontrol etmek icin in kullanilir.

# eger varsa True yazdiracak
print("Python" in text)
# veya baska bi variable ile de kontrol edebilirdik
search = "weird"
print(search in txt)
# icinde olmayani aramak icinde not in kullanilir. 

if search not in text:
    print("Garip")