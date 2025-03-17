import json

my_dog = {
    "name": "billy",
    "age": 2,
    "sex": "m",
}

my_dog["fav_toy"] = "alien"

print(my_dog)

del my_dog["name"]

print(my_dog)