# convert_temp.py
# A program to convert Celsius to Fahrenheit
# By: Daniela Hirsch

def main(): 
  celsius = eval(input("What is the Celsius temperature? "))
  fahrenheit = 9/5 * celsius + 32
  print("The temperature is", fahrenheit, "degrees Fahrenheit")

main()