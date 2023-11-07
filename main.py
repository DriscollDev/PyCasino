import random


def casino(balance):
  print("\n=============================\n")
  print("Welcome to the Casino!")
  print(f"You have ${balance} balance")
  print(
      "Choose from these options to play: \n 1:Death's Crown \n 2:Blackjack(WIP) \n 3:7-12 Dice \n 4:Roulette \n 5:Buy more balance \n 6:Exit the program"
  )
  choice = int(input("Input the number of the game you wish to play: "))
  if (choice == 1):
    balance = deathscrown(balance)
    casino(balance)
  elif (choice == 2):
    balance = blackjack(balance)
    casino(balance)
  elif (choice == 3):
    balance = dice712(balance)
    casino(balance)
  elif (choice == 4):
    balance = basicroulette(balance)
    casino(balance)
  elif (choice == 5):
    print("\n=============================\n")
    balance += int(input("How much more do you wish to add: "))
    casino(balance)
  elif (choice == 6):
    print("\n=============================\n")
    print("Thanks for playing!")
    exit()
  else:
    print("\n=============================\n")
    print("Invalid Input")
    casino(balance)


def deathscrown(balance):
  print("\n==========================================================\n")
  print(
      "Welcome to Deaths Crown \n The Rules are simple we will roll 3 special 6 sided dice, with the faces being\n Crown\n Skull\n Earth\n Fire\n Water\n Air \nYou just have to bet on one of the possible results and you can win back money based on the number of dice that match. \n Good Luck!"
  )
  #print(answer)
  if (input("Ready to play?(y/n): ") == "y"):
    print()
    print("How much would you like to bet?")
    bet = int(input("Input your bet: "))
    if (bet > balance):
      print("You don't have enough money to bet that much.")
    else:
      print(f"You have bet ${bet}")
      print("--------------------------------------------------------")
      place = int(
          input(
              "What face would you like to bet on? \n 1:Crown \n 2:Skull \n 3:Earth \n 4:Fire \n 5:Water \n 6:Air \n 7:Exit\n: "
          ))
      if (place == 7):
        print("Thanks for playing!")
        return balance
      else:
        wins = 0
        for i in range(3):
          dice = random.randint(1, 6)
          #print(dice)
          if (dice == place):
            wins += 1
          if (dice == 1):
            print("Crown")
          elif (dice == 2):
            print("Skull")
          elif (dice == 3):
            print("Earth")
          elif (dice == 4):
            print("Fire")
          elif (dice == 5):
            print("Water")
          elif (dice == 6):
            print("Air")
        if (wins > 0):
          print("----------------------------------------------------------")
          profit = bet * wins
          print(f"You win ${profit}!")
          balance += profit
          print(f"Your current balance is ${balance}")
          if (input("Would you like to play again? (y/n):") == "y"):
            deathscrown(balance)
          else:
            return balance
        else:
          print("You lost!")
          balance -= bet
          print(f"Your current balance is ${balance}")
          if (input("Would you like to play again? (y/n):") == "y"):
            deathscrown(balance)
          else:
            return balance
  else:
    return balance


def blackjack(balance):
  print("\n=============================\n")
  return balance


def dice712(balance):
  print("\n=============================\n")
  print(
      "Welcome 7-12 Dice, rules are really simple. You buy in for 50$ and roll 2 dice, if the dice add up to 7 or 12 you win. If you want to you can double down your bet to add another die."
  )
  if (input("Ready to play? (y/n): ") == "y"):
    if (balance < 50):
      print("You don't have enough money to play.")
      return balance
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    print(f"You rolled {dice1} and {dice2}. Which add to {sum}")
    if (sum == 7 or sum == 12):
      print("You win!")
      balance += 50
      print(f"Your current balance is ${balance}")
      if (input("Would you like to play again? (y/n): ") == "y"):
        dice712(balance)
      else:
        return balance
    else:
      if (input("Would you like to double down to roll another die? (y/n)\n: ")
          == "y"):
        if (balance < 100):
          print("You do not have enough money to double down.")
          return balance
        dice3 = random.randint(1, 6)
        sum2 = sum + dice3
        print(f"You rolled {dice3}. Which add to {sum2}")
        if (sum2 == 7 or sum2 == 12):
          print("You win!")
          balance += 100
        else:
          print("You lost!")
          balance -= 100
        print(f"Your current balance is ${balance}")
        if (input("Would you like to play again? (y/n): ") == "y"):
          dice712(balance)
        else:
          return balance
      else:
        print("You lost!")
        balance -= 50
        print(f"Your current balance is ${balance}")
        if (input("Would you like to play again? (y/n): ") == "y"):
          dice712(balance)
        else:
          return balance
  return balance


def basicroulette(balance):
  type = "none"
  bet = 0
  number = 0
  choice = "none"
  print("\n=============================\n")
  print(
      "Welcome to Roulette. The rules are simple, a number between 0 and 36 will be chosen at randomly.\nYou can bet on these categories \n1:Specific number between 0-36 \n2:Even or odd \n3:Red or black \n4:12 number ranges"
  )
  answer = int(input("Which type of bet would you like to do?: "))
  print("----------------------------------------------------------")
  if (answer == 1):
    type = "Number"
    print("You have chosen to bet on a specific number.")
    bet = int(input("How much would you like to bet?: "))
    if (bet > balance):
      print("You don't have enough money to bet that much.")
    else:
      print(f"You have bet ${bet}")
      number = int(input("What number would you like to bet on?: "))
      if (number > 36 or number < 0):
        print("That number is not between 0 and 36")
  elif (answer == 2):
    type = "E/O"
    print("You have chosen to bet on even or odd.")
    bet = int(input("How much would you like to bet?: "))
    if (bet > balance):
      print("You don't have enough money to bet that much.")
    else:
      print(f"You have bet ${bet}")
      choice = int(
          input(
              "Would you like to bet on even or odd?: \n 1:Even \n 2:Odd \n: ")
      )
      if (choice == 1):
        choice = "even"
      elif (choice == 2):
        choice = "odd"
      else:
        print("That is not a valid choice.")
  elif (answer == 3):
    type = "R/B"
    print("You have chosen to bet on red or black.")
    bet = int(input("How much would you like to bet?: "))
    if (bet > balance):
      print("You don't have enough money to bet that much.")
    else:
      print(f"You have bet ${bet}")
      choice = int(
          input(
              "Would you like to bet on red or black?: \n 1:Red \n 2:Black \n: "
          ))
      if (choice == 1):
        choice = "red"
      elif (choice == 2):
        choice = "black"
      else:
        print("That is not a valid choice.")
  elif (answer == 4):
    type = "Range"
    print("You have chosen to bet on 12 number ranges.")
    bet = int(input("How much would you like to bet?: "))
    if (bet > balance):
      print("You don't have enough money to bet that much.")
    else:
      print(f"You have bet ${bet}")
      choice = int(
          input(
              "Would you like to bet on ranges of numbers?: \n 1:1-12 \n 2:13-24 \n 3:25-36"
          ))
      if (choice == 1):
        choice = "R1"
      elif (choice == 2):
        choice = "R2"
      elif (choice == 3):
        choice = "R3"
      else:
        print("That is not a valid choice.")
  else:
    print("That is not a valid choice.")
  print("----------------------------------------------------------")
  print("Spinning the wheel...")
  roll = random.randint(0, 36)
  print(f"The wheel landed on {roll}")
  if (type == "Number"):
    if (roll == number):
      profit = bet * 35
      print(f"You won ${profit}!")
      balance += profit
      print(f"You now have ${balance} dollars.")
    else:
      print("You lost!")
      balance -= bet
  elif (type == "E/O"):
    if (roll % 2 == 0 and choice == "even"):
      print(f"You won ${bet}!")
      balance += bet
      print(f"You now have ${balance} dollars.")
    elif ((roll % 2 == 1) and choice == "odd"):
      print(f"You won ${bet}!")
      balance += bet
      print(f"You now have ${balance} dollars.")
    else:
      print("You lost!")
      balance -= bet
      print(f"You now have ${balance} dollars.")
  elif (type == "R/B"):
    rollcolor = "none"
    reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    blacks = [
        2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
    ]
    for i in range(18):
      if (roll == reds[i]):
        rollcolor = "red"
      elif (roll == blacks[i]):
        rollcolor = "black"

    if (choice == rollcolor):
      print(f"You won ${bet}!")
      balance += bet
      print(f"You now have ${balance} dollars.")
    else:
      print("You lost!")
      balance -= bet
      print(f"You now have ${balance} dollars.")
  elif (type == "Range"):
    if (roll >= 1 and roll <= 12 and choice == "R1"):
      print(f"You won ${bet}!")
      balance += bet
      print(f"You now have ${balance} dollars.")
    elif (roll >= 13 and roll <= 24 and choice == "R2"):
      print(f"You won ${bet}!")
      balance += bet
      print(f"You now have ${balance} dollars.")
    elif (roll >= 25 and roll <= 36 and choice == "R3"):
      print(f"You won ${bet}!")
      balance += bet
      print(f"You now have ${balance} dollars.")
    else:
      print("You lost!")
      balance -= bet
      print(f"You now have ${balance} dollars.")

  if (input("Would you like to play again? (y/n): ") == "y"):
    basicroulette(balance)

  return balance


casino(100)
