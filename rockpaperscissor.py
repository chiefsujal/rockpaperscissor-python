import random

print("Hello and Welcome to Rock Paper Scissors")
print("What do you choose? 0 for rock, 1 for paper, 2 for scissor")
user_choice = int(input("Enter your choice: "))

if user_choice == 0:
    print("Your choice is rock")
    print("""
            _______
        ---'   ____)
              (_____)
              (_____)
               (____)
        ---.__(___)
        """)
elif user_choice == 1:
    print("Your choice is paper")
    print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
else:
    print("Your choice is scissor")
    print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

random_num = random.randint(0, 2)
if random_num == 0:
    print("Computer's choice is rock")
    print("""
            _______
        ---'   ____)
              (_____)
              (_____)
               (____)
        ---.__(___)
        """)
elif random_num == 1:
    print("Computer's choice is paper")
    print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
else:
    print("Computer's choice is scissor")
    print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

if user_choice == random_num:
    print("Draw")
elif (user_choice == 0 and random_num == 2) or (user_choice == 1 and random_num == 0) or (user_choice == 2 and random_num == 1):
    print("You Win")
else:
    print("Computer Wins")
