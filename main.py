#Restaurant project for demonstrating functions!
#Computer Science 10
#Your name here

#Define all your functions here:

def addTax(beforeTax):
  #put code here and fix the return below
  return beforeTax * 1.05

def addTip():
  #
  return 3.50








print("Welcome to the HEE HUT") #Give your restaurant a better name. This one is bad. 
print("The very best viking eatery in town.")

print("Please enter the total for the bill:")

subTotal = float(input(">$"))
#Floating point value. AKA Double. 

total = addTax(subTotal)

print("After tax, the total is $" + str(total))

#Continue this, running each function in order. 

