# OIT Application Roman Numeral Converter 

Here you will find the final program for the roman numeral converter
The project was started at 10:20 on April 4, 2024
The project was finished at 11:35 on April 4, 2024

See the Provided Decimal to Numeral PDF for the given assistance

Using the converter from https://numeralsconverter.com/convert-number-to-numeral/ I decided that I would not try to also implement the vinculum notation for numbers over 3999.

General Process for the Converter
  1. Read in the numbers from the given file into a list
  2. Call the num_to_rom function on each number in the list and store it in a new list
  3. Create a dictionary with the symbols and their corresponding values for simplicity
  4. For each number, check if the vinculum notation should be used if the number is greater than 3999
  5. If so, call the function again on the num divided by a thousand to get the vinculum notation of the thousands
  6. If not, but it is greater than 1000, add the necessary number of corresponding symbols
  7. Initialize the places variable to specifiy we are starting with the hundreds and then enter the loop for the rest of the number
  8. Since the special cases are the same in hundreds, tens, and single digits, it checks in one loop if the remaining number is greater than 9,5,4,and 1 respectively
  9. If so, it adds the corresponding character from the dictionary and subtracts the necessary amount.
  10. If it goes through the loop and nothing changed, it decrements the place variable by a factor of 10
  11. Once it finishes, the finished numeral is added to the list of all the numerals
  12. After finishing all the conversions, it prints each numeral out on a separate line of an output file given by the name of the input file plus "_out.txt" to specify the output
