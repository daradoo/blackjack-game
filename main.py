import random
from replit import clear
from art import logo

#Function to deal cards
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return(card)

#Function to calculate score
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Condition to change Ace from 11 to 1
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards) 

#Function to compare user score to computer's and determine winner
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a tie!"
  elif user_score == 0 or computer_score > 21 or user_score > computer_score:
    return "Woooooow so good... Do you want a gold star or something? You win tho congrats!"
  elif computer_score == 0 or user_score > 21:
    return "LOSER!!! HA HA HA!! U SUCK GET RECKT NERD."

#Funtion for actual gameplay
def gameplay():
  print(logo)
  
  #Start with empty deck
  game_over = False
  user_cards = []
  computer_cards = []
  
  #Call for deal_card function to deal 2 cards to user and computer each
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Condition for game continuation
  while not game_over:
    user_score = calculate_score(user_cards)
    print(f"Your cards: {user_cards},\nYour current score: {user_score}")
    computer_score = calculate_score(computer_cards)
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or user_score > 21 or computer_score == 0:
      game_over = True
    #Ask user if they want to draw another card based on their previous score
    else:
      user_deal = input("Type 'y' to get another card, or 'n' to pass.: ")
      #Deal another card to user or end game
      if user_deal == "y":
        user_cards.append(deal_card())
      elif user_deal == 'n':
        game_over = True
  #Determine if computer draws another card
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}\nYour final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}\nComputer's final score: {computer_score}")
  print(compare(user_score, computer_score))

#Call gamplay function and clear console to restart
while input("Do you want to play a game of Blackjack? Type 'y' or 'no': ") == "y":
  clear()
  gameplay()