from classCat import Cat, Dog, Client

cat1 = Cat("Снежа", "female", "1.5 year")
cat2 = Cat("Абби", "male", "1 year")
cat3 = Cat("Ницца", "female", "10 months")

dog1 = Dog("Бутуз", "male", "3.5 year")
dog2 = Dog("Слим", "male", "6 year")
dog3 = Dog("Гром", "male", "10 months")

client1 = Client("Иван", "Иванов", "Москва", 50)
client2 = Client("Сергей", "Петров", "Кострома", 145)
client3 = Client("Олег", "Сидоров", "Курск", 90)

print(f"Кошка {cat1.get_name()}, {cat1.get_gender()}, возраст {cat1.get_age()}")
print(f"Кошка {cat2.get_name()}, {cat2.get_gender()}, возраст {cat2.get_age()}")
print(f"Кошка {cat3.get_name()}, {cat3.get_gender()}, возраст {cat3.get_age()}")
print()
print(f"Собака {dog1.get_pet()[0]}, возраст {dog1.get_pet()[1]}")
print(f"Собака {dog2.get_pet()[0]}, возраст {dog2.get_pet()[1]}")
print(f"Собака {dog3.get_pet()[0]}, возраст {dog3.get_pet()[1]}")
print()
print(client1)
print(client2)
print(client3)
print()
List_for_party = [client1.for_party(), client2.for_party(), client3.for_party()]
for client in List_for_party:
    print(" ".join(client))