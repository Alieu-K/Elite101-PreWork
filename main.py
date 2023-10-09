# imports

# Define Functions
def order_maker():
  x = True
  main_dishes = ["Burger", "Burger 2.0", "Cheeseburger", "Vegan Burger","Lettuce  Burger"]
  while x is True:
    print("\n--------------------------------------------------------\n")
    print("What main would you like on the menu?\n")
    for dish in main_dishes:
      print(dish)
      print("-------------------\n")
    meal_part_one = input("")
    if meal_part_one in main_dishes:
      print("Ok, noted.")
      x = False
    else:
      print("Please type an item on the list")
  

def user_query():
  user_choice = True
  
  while user_choice is True:
    print("\nHow may I assit you?")
    
    print("-------------------")
    print("Make an Order(1)")
    print("-------------------")
    print("Edit the Order(2)")
    print("-------------------")
    print("See Order Status(3)")
    print("-------------------")
    print("See Reciept(4)")
    print("-------------------")
    print("Date/Time Check(5)")
    print("-------------------")
    print("Exit(6)")

    choice = input("Type each chocie respective number to select that choice. ")

    if choice == "6":
      print(f"Bye bye {name}")
      user_choice = False

    if choice == "1":
      order_maker()

# Program itself
print("Hot Burgers Chatbot")
print("------------------------------------------")

name = input("What is your name? ")
age = int()

get_age = True
while get_age is True:
  try:
    age = int(input("How old are you? "))
    get_age = False
  except ValueError:
    print("That's not a number, try again")
  
  if age == 0:
    print("I know you ain't zero years old but we'll run with it anyway")
  elif age >= 1 and age <= 13:
    print("You should go play with legos or instead of using this app but alas.")
  elif age > 13 and age <= 20:
    print("Hey, please focus on deadlines.")
  
print(f"Hello {name}, welcome to the Internet's Handy Chatbot.")

user_query()


"""
Sources:

https://stackoverflow.com/questions/7713700/check-variable-if-it-is-in-a-list | Used for the "in" operator.

"""