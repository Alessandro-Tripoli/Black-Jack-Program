#The name of the game is Black Jack, also known as 21.
import random

#For this game we will have to program the following:

#The dealers cards (open an empty list).
dealers_cards=[ ]

#The players cards (open an empty list).
players_cards=[ ]

#Displaying the cards.

#Dealing the cards/ dealrs cards. The code "!=" means "is not equal to" which will allow the loop to stop once it reaches 2)
while len(dealers_cards) != 2:#Make a while loop
    dealers_cards.append(random.randint(1,11)) #The lengths of cards.
    if len(dealers_cards) == 2: #The  code "==" means "equal to"
       print("Dealer has X &" ,dealers_cards[1])

#Delt Player c/Users/alessandrotripoli/Desktop/Python Projects/Practice Program/Practice_003_BlackJack.pyards
while len(players_cards) !=2:
    players_cards.append(random.randint(1,11))
    if len(players_cards) == 2:
       print("Player has", players_cards)

#The sum of the dealer cards. We us an "if statement."
if sum(dealers_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealers_cards) > 21:
    print("Dealer flopped")

#The sum of the player cards. Sring input "str(input)". The "else" statement executes the conditions of the "if" statements.
while sum(players_cards) < 21: #While sum of players card is greater than 21
    decision_made = str(input("Would you like to hit or stay?")) #Asks player "do you want to stay or hit?"
    if decision_made == "hit": #If player chooses to hit.
        players_cards.append(random.randint(1,11)) #Player will then add on (append) another integer between 1 & 11 to the list.
        print("Player now has a total of "  + str(sum(players_cards)) + " from these cards", players_cards) #Tell player the total sum and what they have.
    else: #If player chooses to stay.
        print("Dealer has a total of " + str(sum(dealers_cards)) +  " with", dealers_cards) #Tells dealers total and shows the cards.
        print("Player has a total of " + str(sum(players_cards)) + " with", players_cards) #Tells players total and shows the cards.
        if  sum(dealers_cards) > sum(players_cards):
            print("Dealer Wins!")
        else:
            print("Player Wins!")
            break

if sum(players_cards) > 21:
    print("Player flopped")
elif sum(players_cards) == 21:
    print("Player has BlackJack and wins")
