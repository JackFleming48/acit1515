
def vowels(name):
    vow = "aeiouy"
    count = 0

    for i in name:
        for x in vow:
            if i == x:
                count +=1
    print(f"There is {count} vowels in that name! ")
    

nom = input("what is your name? ")
vowels(nom)