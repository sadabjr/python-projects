name= input("Inter Your Name:\n")
print("Hello"+ name)
print("Welcome to Treasure Island!")
print("________ ________")
print("________ ________")
print("________ ________")
print("________ ________")
print("________ ________")
print("________ ________")

choose=input("Assume there are two path. Choose one of them -left or right:\n")

choosen=choose.lower()

if choosen=="left":
    b=input("Now you have to condition 'swim' or 'wait'. Choose one of them:\n " )
    c=b.lower()
    if b=="wait":
        d=input("now after waiting you have three doors Red, Yellow and Blue")
        e=d.lower()
        if e=="red" or e=="blue":
            print("Game Over!")
        else:
            print("Congo!")
            print("You win!")
    else:
        print("Game Over!")
else:
    print("Game Over!")