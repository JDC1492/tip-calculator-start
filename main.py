#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print('Welcome to the tip calculator')

total = input('What was the total of the bill?\n')

tip = input("What percentage tip would you like to give?\n10, 12, or 15?\n")

tip_float = int(tip)/100 
total_w_tip = float(total) * round(tip_float) + float(total)

prty = input("How many people to split the bill?")

indi_amount = total_w_tip / round(int(prty),2)
print(type(indi_amount))

# print(type(tip_float))

print(f'Each person should pay: {round(indi_amount, 2)}')