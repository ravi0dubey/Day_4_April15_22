import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#print(rock)
#print(scissors)
options= [rock, paper, scissors]
options1=["rock","paper","scissors"]
#print(choices)
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_choice = random.randint(0,2)
#computer_choice = 2
print(your_choice)
print(f"Computer chose:{options1[computer_choice]}")
#print(options[your_choice])

if(options1[your_choice] == "rock" and options1[computer_choice] == "scissors"):
  print(f"You Win as you chose rock{options[your_choice]}")
elif(options1[your_choice] == "scissors" and options1[computer_choice] == "paper"):
  print(f"You Win as you chose scissors{options[your_choice]}")
elif(options1[your_choice] == "paper" and options1[computer_choice] == "rock"):
  print(f"You Win as you chose paper {options[your_choice]}")
elif(options1[your_choice] == "rock" and options1[computer_choice] == "paper"):
  print(f"Computer Win as computer chose paper{options[computer_choice]}")
elif(options1[your_choice] == "scissors" and options1[computer_choice] == "rock"):
  print(f"Computer Win as computer chose rock{options[computer_choice]}")
elif(options1[your_choice] == "paper" and options1[computer_choice] == "scissors"):
  print(f"Computer Win as computer chose scissors{options[computer_choice]}")
elif(options1[your_choice] == options1[computer_choice]):
  print("It's a tie since yours and computer choice is same")
else:
  print("Bogus")

