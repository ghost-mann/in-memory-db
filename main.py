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

# Accessing items

x = my_car["Model"]
y = my_car.get("Model")
print(x)
print(y)

z = my_ride.keys()
print(z)

# changing items

my_car["Year"] = 2018
print(my_car)

my_car.update({"Year": 2020})
print(my_car)

# add items
my_car.update({"Petrol":True})
print(my_car)

# removing items 
my_car.pop("Diesel")
print(my_car)

my_car.popitem()
print(my_car)

# adding items
my_car.update({"colour":"Grey"})
my_car["rims"] = "Black" 
print(my_car)

# # empties the dictionary
# my_car.clear()
# print(my_car)

del my_car["rims"]
print(my_car)


# loop - dictionaries

operator = dict(name = "Kamau", age = 23, build = "skinny", skills = "none")

for x in operator:
    print(x)
    
# print out values
for x in operator.values():
    print(x)

# looping through keys and values
for x,y in operator.items():
    print(x,y)
    
# copying dictionaries 
main_operator = operator.copy()
print(f"This is{main_operator}")


side_operator = dict(main_operator)
print(side_operator)


# nested dictionaries

my_students = {
    "student1": {
        "name":"Julius",
        "school": "infill",
        "grade": 8
    },
    "student2": {
        "name": "Silvia",
        "school": "Newlight",
        "grade":5
    },
    "student3": {
        "name":"Kinderman",
        "school": "Tendercare",
        "grade": 6
    }
}

print(my_students["student1"])

# add all dictionaries to a new dictionary 

kid1 = {
  "name" : "Emil",
  "year" : 2004
}
kid2 = {
  "name" : "Tobias",
  "year" : 2007
}
kid3 = {
  "name" : "Linus",
  "year" : 2011
}

my_school = {
    "kid1":kid1,
    "kid2":kid2,
    "kid3":kid3
}

print(my_school["kid1"]["name"])

# accessing items in nested dictionaries 

for x, obj in my_school.items():
    print(x)
    
for y in obj:
    print(y + ':', obj[y])