import time
import random
from MobileCritter import MobileCritter
from Ant import Ant
from Spider import Spider



def test(bug: MobileCritter, type):
  pos = bug.position.copy() # initial position; this will be used to keep track of expected position
  
  for i in range(random.randint(3, 5)): # random number of times it will be moved
    r = random.randint(1, 4) # direction is chosen randomly
    if r == 1:  # moving up
      bug.move_up()
      print("\nMoved UP")
      # updating the expected position
      if type == 'Ant': 
        pos[1] += 2
      else:
        pos[1] += 1
      print("\tExpected new position:", pos)
      print("\tTrue position:", bug.position)
      print("\tTest passed?", pos == bug.position)
    elif r == 2: # moving down
      bug.move_down()
      print("\nMoved DOWN")
      # updating the expected position
      pos[1] -= 2
      print("\tExpected new position:", pos)
      print("\tTrue position:", bug.position)
      print("\tTest passed?", pos == bug.position)
    elif r == 3: # moving right
      bug.move_right()
      print("\nMoved RIGHT")
      # updating the expected position
      pos[0] += 1
      print("\tExpected new position:", pos)
      print("\tTrue position:", bug.position)
      print("\tTest passed?", pos == bug.position)
    else:
      bug.move_left()
      print("\nMoved LEFT")
      if type == 'Ant': 
        pos[0] -= 1
      else:
        pos[0] -= 2
      print("\tExpected new position:", pos)
      print("\tTrue position:", bug.position)
      print("\tTest passed?", pos == bug.position)
    

def main():
  print("\n\nWelcome to the critter tester.")

  while True:
    choice = input("Which class would you like to instantiate?\n\n\t1. Ant\n\t2. Spider\n\nEnter your selection: ")
  
    if choice == '1':
      print("Creating and testing an Ant object...")
      time.sleep(2)
      critter = Ant()
      test(critter, 'Ant')
    elif choice == '2':
      print("Creating and testing a Spider object...")
      time.sleep(2)
      critter = Spider()
      test(critter, 'Spider')
    else:
      print("Invalid selection.  Please try again.")
      continue
    yn = input("\n\nWould you like to test another critter? Y/N: ")
    if yn.upper() == 'N':
      break
      print("Exiting to main menu....")
      time.sleep(3)
