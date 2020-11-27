def main():
  # Program Variables

  # Main Program Loop
  loop = True
  while loop:
    selection = getMenuSelection()

    if selection == "1":
      option1()
    elif selection == "2":
      print("Option 2")
    elif selection == "3":
      print("Option 3")
    elif selection == "4":
      print("Exit")
      loop = False

  print("Goodbye")
# end main()

def getMenuSelection():
  print("\nMAIN MENU")
  print("1: Option 1")
  print("2: Option 2")
  print("3: Option 3")
  print("4: Exit")
  return input("Enter menu selection:")

def option1():
  print("Option 1")

# Call main to begin program
main()