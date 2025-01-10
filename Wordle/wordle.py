# Wordle Game
import random as rand
import sys
import time
import shutil
import re

def print_centered(text):
    ansi_escape_pattern = re.compile(r'\x1b\[.*?m')
    cleaned_text = ansi_escape_pattern.sub('', text)
    # Get the terminal size
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns
    
    # Calculate the padding needed for centering
    padding_left = (terminal_width - len(cleaned_text)) // 2
    padding_right = terminal_width - len(cleaned_text) - padding_left
 
    
    # Print the centered text
    centered_text = ' ' * padding_left + text + ' ' * padding_right
    print(centered_text)

def unicode_loading_bar(iterations, length=80):
    for i in range(iterations):
        percent = (i + 1) / iterations
        filled_length = int(length * percent)
        bar = '█' * filled_length + '░' * (length - filled_length)
        sys.stdout.write(f'\r[{bar}] {percent*100:.1f}%')
        sys.stdout.flush()
        time.sleep(0.1)  # Simulate work

    sys.stdout.write('\r' + ' ' * (length + 10) + '\r')
    sys.stdout.flush()
    # sys.stdout.write('\n')  # Newline at the end

def clear_input_line():
    """Clears the current input line in the terminal."""
    # Move the cursor up one line (assumes the input is on a new line)
    sys.stdout.write('\033[F')
    # Move the cursor to the beginning of the line
    sys.stdout.write('\r')
    # Get the width of the terminal
    terminal_width = shutil.get_terminal_size().columns
    # Overwrite the entire line with spaces
    sys.stdout.write(' ' * terminal_width)
    # Move the cursor back to the beginning of the line
    sys.stdout.write('\r')
    sys.stdout.flush()

def get_input_with_clear(prompt=""):
    """Gets user input and clears the input line after."""
    # Print the prompt and get the user input
    user_input = input(prompt)
    
    # Clear the input line
    clear_input_line()
    
    return user_input


def main():
    # ANSI escape codes for colors
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BOLD = '\033[1m'
    WHITE = '\033[37m'
    BLACK = '\033[40m'
    RESET = '\033[0m'  # Reset to default color

    # Fake Loading Bar for the lols
    unicode_loading_bar(50)

    # Save the file of words
    word_file=sys.argv[1]
    attempts=int(sys.argv[2])

    # Load the words into a list
    file=open(word_file)
    unformatted=file.readlines()
    words=list(map(str.strip,unformatted))

    # Create a Loop for multiple repetitions of the Wordle Game
    while True:
        print_centered(f"{BOLD}WELCOME to WORDLE!{RESET}")
        secret_word_pos=rand.randint(0,len(words)-1)
        secret_word=words[secret_word_pos]
        guesses=0
        # print(secret_word)
        # Loop for the guess of the current game
        while True:
            # Get the New Guess
            new_guess=""
            while True:
                new_guess=get_input_with_clear().strip().lower()
                if new_guess in words:
                    break
                else:
                    print("Not in Word List".center(160),end='',flush=True)
                    time.sleep(3)
                    sys.stdout.write('\r' + ' ' * (80 + 10) + '\r')
                    sys.stdout.flush()
            # Check the new Guess
            result=''
            for letter,check in zip(new_guess,secret_word):
                if letter.lower() == check:
                    result+="^"
                elif letter.lower() in secret_word:
                    result+="-"
                else:
                    result+="x"
            # Finalize Results ^ is correct, - is maybe yellow, x is wrong, * is def yellow
            for num in range(len(secret_word)):
                if result[num]=="-":
                    # Count the letter in the guess and the right word
                    guess_count=new_guess.count(new_guess[num])
                    correct_count=secret_word.count(new_guess[num])
                    if guess_count<=correct_count:
                        result=result[:num]+"*"+result[num+1:]
                    else:
                        # Find how many greens are from this letter
                        green_count=0
                        for num2 in range(len(new_guess)):
                            if new_guess[num2]==new_guess[num] and (result[num2]=="^" or result[num2]=="*"):
                                green_count+=1
                        yellow=correct_count-green_count
                        if yellow>0:
                            result=result[:num]+"*"+result[num+1:]
                        else:
                            result=result[:num]+"x"+result[num+1:]
            # Decode the results
            final=''
            for num in range(len(result)):
                if result[num] == "^":
                    final+=f'{GREEN}{WHITE}{new_guess[num].upper()}{RESET}'
                elif result[num] == "*":
                    final+=f'{YELLOW}{WHITE}{new_guess[num].upper()}{RESET}'
                elif result[num] == "x":
                    final+=f'{BLACK}{new_guess[num].upper()}{RESET}'
            print_centered(final)

            if new_guess.lower()==secret_word:
                words.pop(secret_word_pos)
                print_centered("CORRECT!!\n")
                break
            guesses+=1
            if not guesses<attempts:
                print_centered("FAILED!\nSECRET WORD: ",secret_word.upper())
                words.pop(secret_word_pos)
                print()
                break

if __name__ == '__main__':
    main()