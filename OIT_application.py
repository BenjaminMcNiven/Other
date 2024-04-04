import sys

def read_file(filename):
    with open(filename,'r') as input_file:
        lines=[]
        for line in input_file:
            lines.append(int(line.strip()))
    return lines

def create_roman(numbers):
    roman=[]
    for num in numbers:
        roman.append(num_to_rom(num))
    return roman

def num_to_rom(num):
    special_values= {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
    rom=""
    if (num/1000)>=4:
        rom+="("+num_to_rom(num//1000)+")"
        num=num%1000
    #loop for the thousands
    while num//1000>=1:
        rom+=special_values[1000]
        num-=1000
    # loop for the rest
    place=100
    while num>0:
        changed=False
        if num>=9*place:
            changed=True
            rom+=special_values[9*place]
            num-=9*place
        if num>=5*place:
            changed=True
            rom+=special_values[5*place]
            num-=5*place
        if num>=4*place:
            changed=True
            rom+=special_values[4*place]
            num-=4*place
        if num>=1*place:
            changed=True
            rom+=special_values[1*place]
            num-=1*place
        if not changed:
            place/=10
    return rom

def print_to_file(numerals, filename):
    filename+="_out.txt"
    with open(filename, "w") as outpt:
        for numeral in numerals:
            outpt.write(numeral+"\n")
    


if __name__=="__main__":
    if(len(sys.argv)<2):
        print("NO ARGUMENTS GIVEN")
    else:
        numbers=read_file(sys.argv[1])
        roman=create_roman(numbers)
        print_to_file(roman, sys.argv[1])
        print(roman)
