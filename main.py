# imports

# Define Functions

def user_query():
  move = True
  
  while move is True:
    print("\nHow may I assit you?")
    
    print("-------------------")
    print("PlaceHolder 1")
    print("-------------------")
    print("PlaceHolder 2")
    print("-------------------")
    print("PlaceHolder 3")
    print("-------------------")
    print("PlaceHolder 4")
    print("-------------------")
    print("Exit(5)")

    choice = input("Type each chocie respective number to select that choice. ")

    if choice == "5":
      print(f"Bye bye {name}")
      move = False


# Program itself
print("Internet's Handy Chatbot")
print("------------------------------------------")

name = input("What is your name? ")
age = int()

contin = True
while contin is True:
  try:
    age = int(input("How old are you? "))
    contin = False
  except ValueError:
    print("That's not a number, try again")
  
  if age == 0:
    print("I know you ain't zero years old but we'll run with it anyways.")
  
print(f"Hello {name}, welcome to the Internet's Handy Chatbot.")

user_query()


  