countries = [
    {"country": "America", "continent": "North America"},
    {"country": "Australia", "continent": "Oceania"},
    {"country": "Canada", "continent": "North America"},
    {"country": "Egypt", "continent": "Africa"}
]

continent_set = set()

count = 0
for x in countries:
    continent_set.add(x["continent"])
    
    # print(x["continent"])
    # if x["continent"] != "":
    #     count += 1
    
print(len(continent_set))


demo = {
    "ids": {
        "classes":{
            "languages":[
                "java",
                "python",
                "html"
            ]
        }
    },
    "names": [
        "jack",
        "dave",
        "steve"
    ]
}

for x in demo:
    print()

'''
Task 1


'''