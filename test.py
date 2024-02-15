#temperature = 25

#if temperature = 30:
#print ("It is a good day")
#print ("It is a bard day")

#birth_year = input("what is your birth year")
#age = 2024 - int(birth_year)
#print(age)

names=['John','Mel','Lough','Ben']
print(names[-5])

i= 1
while i <= 2:
    i =i+1
    print (i)




weight= float(input("input your weight: "))
unit= input("Is it in K(kg) or L(bs): ")
new_weightK= weight / 0.45
new_weightL= weight * 0.45
if unit.upper()== 'K':
    print("Your weight in Pounds is: " + str(new_weightK))
elif unit.upper()== "L":
    print ("Your weight in Kilogram is: " + str(new_weightL))


#temperature= int(input("Input your current Temperature: "))

if temperature == 38:
    #print('You have Fever')
elif temperature >= 35:
    print("You show signs of Hyperthermia" +str(C))
elif temperature <= 30:
    print("You show signs of Hypothermia")
else: print("You are fine")