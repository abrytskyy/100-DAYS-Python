# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n ")

add_pepperoni = input("Do you want pepperoni? Y or N\n ")
extra_cheese = input("Do you want extra cheese? Y or N\n ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
    bill += 25
else:
  print("Your typed wrong letter or symbol. Start program again")

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  elif size == "M" or "L":
    bill += 3
  else:
    print("Your typed wrong letter or symbol. Start program again")

if extra_cheese == "Y":
  bill += 1
elif extra_cheese == "N":
  bill += 0
else:
  print("Your typed wrong letter or symbol. Start program again")

print(f"Your final bill is ${bill}")

