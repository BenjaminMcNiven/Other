# ansi_escape_codes.py

# ANSI escape codes for text styles
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'
HIDDEN = '\033[8m'

# ANSI escape codes for text colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# ANSI escape codes for bright text colors
BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

# ANSI escape codes for background colors
BACKGROUND_BLACK = '\033[40m'
BACKGROUND_RED = '\033[41m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_YELLOW = '\033[43m'
BACKGROUND_BLUE = '\033[44m'
BACKGROUND_MAGENTA = '\033[45m'
BACKGROUND_CYAN = '\033[46m'
BACKGROUND_WHITE = '\033[47m'

# ANSI escape codes for bright background colors
BACKGROUND_BRIGHT_BLACK = '\033[48;5;8m'
BACKGROUND_BRIGHT_RED = '\033[48;5;9m'
BACKGROUND_BRIGHT_GREEN = '\033[48;5;10m'
BACKGROUND_BRIGHT_YELLOW = '\033[48;5;11m'
BACKGROUND_BRIGHT_BLUE = '\033[48;5;12m'
BACKGROUND_BRIGHT_MAGENTA = '\033[48;5;13m'
BACKGROUND_BRIGHT_CYAN = '\033[48;5;14m'
BACKGROUND_BRIGHT_WHITE = '\033[48;5;15m'

def print_colored_examples():
    print(f"{RESET}Reset")
    print(f"{BOLD}Bold{RESET}")
    print(f"{DIM}Dim{RESET}")
    print(f"{UNDERLINE}Underlined{RESET}")
    print(f"{BLINK}Blinking{RESET}")
    print(f"{REVERSE}Reverse{RESET}")
    print(f"{HIDDEN}Hidden{RESET}")
    
    print(f"{BLACK}Black Text{RESET}")
    print(f"{RED}Red Text{RESET}")
    print(f"{GREEN}Green Text{RESET}")
    print(f"{YELLOW}Yellow Text{RESET}")
    print(f"{BLUE}Blue Text{RESET}")
    print(f"{MAGENTA}Magenta Text{RESET}")
    print(f"{CYAN}Cyan Text{RESET}")
    print(f"{WHITE}White Text{RESET}")

    print(f"{BRIGHT_BLACK}Bright Black Text{RESET}")
    print(f"{BRIGHT_RED}Bright Red Text{RESET}")
    print(f"{BRIGHT_GREEN}Bright Green Text{RESET}")
    print(f"{BRIGHT_YELLOW}Bright Yellow Text{RESET}")
    print(f"{BRIGHT_BLUE}Bright Blue Text{RESET}")
    print(f"{BRIGHT_MAGENTA}Bright Magenta Text{RESET}")
    print(f"{BRIGHT_CYAN}Bright Cyan Text{RESET}")
    print(f"{BRIGHT_WHITE}Bright White Text{RESET}")

    print(f"{BACKGROUND_BLACK}{WHITE}Black Background with White Text{RESET}")
    print(f"{BACKGROUND_RED}{WHITE}Red Background with White Text{RESET}")
    print(f"{BACKGROUND_GREEN}{WHITE}Green Background with White Text{RESET}")
    print(f"{BACKGROUND_YELLOW}{BLACK}Yellow Background with Black Text{RESET}")
    print(f"{BACKGROUND_BLUE}{WHITE}Blue Background with White Text{RESET}")
    print(f"{BACKGROUND_MAGENTA}{WHITE}Magenta Background with White Text{RESET}")
    print(f"{BACKGROUND_CYAN}{BLACK}Cyan Background with Black Text{RESET}")
    print(f"{BACKGROUND_WHITE}{BLACK}White Background with Black Text{RESET}")

    print(f"{BACKGROUND_BRIGHT_BLACK}{WHITE}Bright Black Background with White Text{RESET}")
    print(f"{BACKGROUND_BRIGHT_RED}{WHITE}Bright Red Background with White Text{RESET}")
    print(f"{BACKGROUND_BRIGHT_GREEN}{WHITE}Bright Green Background with White Text{RESET}")
    print(f"{BACKGROUND_BRIGHT_YELLOW}{BLACK}Bright Yellow Background with Black Text{RESET}")
    print(f"{BACKGROUND_BRIGHT_BLUE}{WHITE}Bright Blue Background with White Text{RESET}")
    print(f"{BACKGROUND_BRIGHT_MAGENTA}{WHITE}Bright Magenta Background with White Text{RESET}")
    print(f"{BACKGROUND_BRIGHT_CYAN}{BLACK}Bright Cyan Background with Black Text{RESET}")
    print(f"{BACKGROUND_BRIGHT_WHITE}{BLACK}Bright White Background with Black Text{RESET}")

if __name__ == "__main__":
    print_colored_examples()
