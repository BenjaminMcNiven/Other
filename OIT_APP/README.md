# OIT Application Roman Numeral Converter 

Here you will find the final program for the roman numeral converter
The project was started at 10:20 on April 4, 2024
The project was finished at 11:35 on April 4, 2024

See the Provided Decimal to Numeral PDF for the given assistance

Using the converter from https://numeralsconverter.com/convert-number-to-numeral/ I decided that I would not try to also implement the vinculum notation for numbers over 3999.

General Process for the Converter
  1. Read in the numbers from the given file into a list
  2. Call the num_to_rom function on each number in the list and store it in a new list
     a. Create a dictionary with the symbols and their corresponding values for simplicity
     b. For each number, check if the vinculum notation should be used if the number is greater than 3999
     c. If so, call the function again on the num divided by a thousand to get the vinculum notation of the thousands
     d. If not, but it is greater than 1000, add the necessary number of corresponding symbols
     e. Initialize the places variable to specifiy we are starting with the hundreds and then enter the loop for the rest of the number
       i. Since the special cases are the same in hundreds, tens, and single digits, it check in one loop if it 
