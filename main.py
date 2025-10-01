my_dict = {
    "Toyota" : "corolla",
    "Mitsubishi": "Gallant",
    "Subaru": "imprezza"
}

my_car = {
    "Make": "Toyota",
    "Model": "Auris",
    "Year": 2017,
    "Diesel": False
}

my_ride = dict(make = "toyota", model = "corolla", age=22)

print(len(my_dict))
print(len(my_car))
print(len(my_ride))


x = my_car["Model"]
y = my_car.get("Model")
print(x)
print(y)

