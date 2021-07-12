import random


# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#


dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)

#def dice_roller(min, max):
while True:
    value = input("how many dice would you like 1,2, or 3: ")
    value = int(value)
        
    #input ("would you like to roll again? 'y' for 'yes' or 'n' for 'no'  :")

    if value == 3:
        print(f" your numbers are" , random.randint(1,6),random.randint(1,6),random.randint(1,6))
        input ("would you like to roll again? 'y' for 'yes' or 'n' for 'no' :")
                
    elif value == 2:
        print (f"you numbers are " , random.randint(1,6),random.randint(1,6))
        input ("would you like to roll again? 'y' for 'yes' or 'n' for 'no' :")
    elif value == 1:
        print(f"your number is ", random.randint(1,6))
        input ("would you like to roll again? 'y' for 'yes' or 'n' for 'no' :")

    else: 
        value ==
        print(f"game over")
    break
        
    

        
        
        #print ("rolling dice.... ")
        #number1 = random.int(min,max)
        #print("you number is")
        #chioce = input("would you like to roll again ? ("y/n)")
        #if choice() == "y"
            
#dice_roller(1,6)

