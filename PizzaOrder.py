#Pizza Order
#Benjamin Readman
print("Welcome to Pizza Pie People!")
name=str(input("What is your name?"))
gf=str(input("Would you like to have a gluten free pizza?"))
price=12.50
if gf == 'yes':
  price=14.50
  pizza=str(input("Would you like to have pepperoni on that pizza:"))
  if pizza == 'yes':
    price+=1.25
    print('Thank you, ',name,", that pizza is $",price,sep=(""))
  else:
    if pizza == 'no':
      print('Thank you, ',name,", that pizza is $",price,sep=(""))
else:
  if gf == 'no':
    pizza=str(input("Would you like to have pepperoni on that pizza:"))
    if pizza == 'yes':
      price+=1.25
      print('Thank you, ',name,", that pizza is $",price,sep=(""))
    else:
      if pizza == 'no':
        print('Thank you, ',name,", that pizza is $",price,sep=(""))
  else:
    print("Sorry, I didn't get that, GOODBYE")
