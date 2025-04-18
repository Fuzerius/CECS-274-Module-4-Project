import time
import game
import critter_tester

print("\n\nWelcome to the programming exercises for the Module 1 Lab Activities!!!")

time.sleep(2)

response = '0'
while response != '3':
  menu = "\n\nYou can test the implementation of your Ant and Spider classes by selecting from the following options.\n\nWhat would you like to do?\n\n\t1. Create and manipulate MobileCritter objects.\n\t2. Play board game.\n\t3. Quit.\n\nEnter your selection: "

  response = input(menu)

  if response == '1':
    critter_tester.main()
  elif response == '2':
    time.sleep(1)
    print("Starting game...")
    time.sleep(2)
    print('\n\n')
    game.main()
    
    
  elif response == '3':
    print("Goodbye!")
    break
  else:
    print("Invalid selection.  Please try again.")
  
