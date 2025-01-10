import random as rand

def Computer_Simulation(iterations,switch):
    iteration,wins=0,0
    while iteration<iterations:
        # Set the doors
        doors={1:"goat",2:"goat",3:"goat"}
        doors[rand.randint(1,3)]="car"
        # Computer Guess
        guess=rand.randint(1,3)
        # Reveal a door
        while True:
            reveal=rand.randint(1,3)
            if reveal != guess and doors[reveal]!='car':
                break
        # Switch the Guess or not
        if switch==1:
            guess=[option for option in [1,2,3] if option not in (guess, reveal)][0]
        if doors[guess]=="car":
            wins+=1
        iteration+=1
    return wins

def User_Input():
    iteration,wins=0,0
    while True:
        print("Iteration #",iteration+1)
        # Set the doors
        doors={1:"goat",2:"goat",3:"goat"}
        doors[rand.randint(1,3)]="car"
        # User Guesses
        while True:
            guess=input("Choose a door (Press Enter to quit): \n[1] [2] [3]\n").strip()
            if guess in ["1","2","3",""]:
                break
            else: 
                print("That is not one of the options")
        if guess=="":
            break
        guess=int(guess)
        # Reveal a door
        while True:
            reveal=rand.randint(1,3)
            if reveal != guess and doors[reveal]!='car':
                break
        print("Door ",reveal,f" is a {doors[reveal]}") 
        # Switch the Guess or not
        while True:
            guess=input("You may choose to switch. Please enter your final guess: \n").strip()
            if guess in ["1","2","3"]:
                guess=int(guess)
                break
            else: 
                print("That is not one of the options")
        print()
        if doors[guess]=="car":
            print("You just won a car!!!")
            wins+=1
        else:
            print("Wrong choice, you just lost a car!")
        print('Door 1  Door 2  Door 3')
        print(" ",doors[1],"  ",doors[2],"  ",doors[3],"\n\n")
        iteration+=1
    return wins,iteration

def main():
    # ANSI escape codes for colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    RESET = '\033[0m'  # Reset to default color

    print(f"{BOLD}{BLUE}Welcome to the Monty Hally Problem Simulator{RESET}")
    mode=0
    # Mode Selector
    while True:
        mode=input(f"Please choose a mode:\nPress {GREEN}1{RESET} for a User-simulated Problem\nPress {GREEN}2{RESET} for a Computer Generated Simulation\n{GREEN}").strip()
        print(f"{RESET}",end="")
        if not mode in ['1','2',""]:
            print(f"{RED}That wasn't one of the options\n{RESET}")
        elif mode == "":
            break
        else:
            mode=int(mode)
            break
    
    # Computer Simulation Selector
    if mode==2:
        print()
        switch,iterations=0,0
        # Choose whether or not to switch
        while True: 
            switch=input(f"Please choose a strategy for the computer simulation:\nPress {GREEN}1{RESET} to always switch\nPress {GREEN}2{RESET} to always stay\n{GREEN}").strip()
            print(f'{RESET}',end="")
            if not switch in ['1','2']:
                print(f"{RED}That wasn't one of the options\n{RESET}")
            else:
                switch=int(switch)
                print()
                break
        # Choose the number of iterations
        while True: 
            iterations=input(f"Please choose how many iterations that simulation should run:\n{GREEN}").strip()
            print(f'{RESET}',end='')
            if not iterations.isdigit():
                print(f"{RED}That isn't a whole number\n{RESET}")
            else:
                iterations=int(iterations)
                break
        # Run the simulation
        wins=Computer_Simulation(iterations,switch)
        if iterations!=0:
            print(f"\nThe Computer used the strategy {'Switching' if switch==1 else 'Keeping'} for {iterations} iterations.\nThe Computer won a total of {wins} times, giving it a winrate of {(wins/iterations)*100:.2f}%")

    # User Simulation
    if mode==1:
        print()
        wins,iterations=User_Input()
        if iterations!=0:
            print(f"You won a total of {wins} times, giving you a winrate of {(wins/iterations)*100:.0f}%")

if __name__ == "__main__":
    main()