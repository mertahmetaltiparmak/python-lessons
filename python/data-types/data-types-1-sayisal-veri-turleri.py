name = "mert" # string - str data type
age = 25 # integer - int data type
weight = 84.3 # float data type 
comp = 3j # complex data type

# eger bunlarin hepsini + isareti ile yazmak isteseydik o zaman tur donusumu yapmamiz lazimdi ornek:
print("Name: ", name, " Age: ", age, " Weight: ", weight, " Complex Number: ", comp) 
#print("Name: " + name + " Age: " + str(age) + " Weight: " + str(weight) + " Complex Number: " + str(comp))

# type() functionu ile turunu yazdirabiliriz

print(type(name))
print(type(age))
print(type(weight))
print(type(comp))