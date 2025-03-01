def recurse():
    opt = int(input(f"Press 1: to print: 'Hello' \n Press 2: to print 'Great choice!' \n Press 3: to end the function. "))
    if opt == 1:
        print("hello")
    if opt == 2:
        print("Great choice!")
    if opt == 3:
        return
    recurse()

recurse()
    