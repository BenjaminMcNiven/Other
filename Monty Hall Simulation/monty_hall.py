# Simulate the Monty Hall problem 
import random as rand

# Mode Selection
mode=input("Computer Simulation or User Input? (c for computer, u for user): ").strip()
if mode=="c":
    switch=input("Should the Computer always switch or keep its choice? (s for switch, k for keep): ").strip()
    iterations=int(input("How many iterations should the computer do? "))

iteration,wins=0,0
while True:
    if mode =='c':
        if iteration>=iterations:
            break
    else: print("Iteration ",iteration)
    doors={
        1:"goat",
        2:"goat",
        3:"goat"}

    car=rand.randint(1,3)
    doors[car]="car"

    # User Guess
    if mode != "c":
        guess=input("Choose a door: \n[1] [2] [3]\n")
        if guess=="":
            break
        guess=int(guess)

    # Computer Simulation
    else:
        guess=rand.randint(1,3)

    while True:
        reveal=rand.randint(1,3)
        if reveal != guess and doors[reveal]!='car':
            if mode != "c":
                print("Door ",reveal,f" is a {doors[reveal]}") 
            break
        
    # # User Chooses to Switch
    if mode != 'c':
        guess=int(input("You may choose to switch. Please enter your final guess: \n"))

    # # Computer Chooses automatically to switch
    elif switch == "s":
        guess=[option for option in [1,2,3] if option not in (guess, reveal)][0]

    # # Computer Chooses to stay
    else:
        guess = guess

    if doors[guess] == "car":
        wins+=1
        if mode!="c":
            print("You just won a car!!!")
    else: 
        if mode!="c":
            print("Wrong choice, you just lost a car!")
    if mode!="c":
        print('Door 1  Door 2  Door 3')
        print(doors[1],"  ",doors[2],"  ",doors[3],"\n")
    iteration+=1

# # User winrate
if mode!="c":
    iterations=iteration

print("Total Wins: ",wins)
print("Total Losses: ",iterations-wins)
print("Win Rate: ",(wins/iterations)*100, "%")