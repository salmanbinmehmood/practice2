import random


# b = input("Enter any number : ")
# items = ["snake","water","gun"]
items = [1,2,3]
while True:
    instructions = """
snake : 1
water : 2
gun : 3"""

    print(instructions)
    com = random.choice(items)
    
    player = int(input("Enter any nummber :"))
    print(type(player))
    if player== 1:
        if com == 2 :

            print("player win")
        elif com == 3 :
            print("com win")
        else:
            print("match draw")
        
        
    elif player== 2:
        if com == 1:
            print("com win")

        elif com == 3:
            print("player win")
        else:
            print("match draw")
        
    elif player == 3:
        if com == 1:
            print("player win")
        elif com == 2 :
         
            print("com win")
        else:
            print("match draw")

    
    print(f" your answer was {player} computer answer was{com}")
