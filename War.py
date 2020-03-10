#  File: War.py
#  Description: Simulates the card game "War"
#  Student's Name: Matthew Yap
#  Student's UT EID: my5476
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 9/28/2017
#  Date Last Modified: 9/28/2017
import random

#   global variables
cardsuit = ("C", "D", "H", "S")
rank = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
cardvalue = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14,}

#   allows you to create a card
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = cardvalue.get(rank)

    #   allows you to print an individual card
    def __str__(self):
        cardone = ""
        cardone = cardone + str(self.rank)
        cardone = cardone + str(self.suit)
        return(cardone)

#   allows you to create a deck
class Deck:

    def __init__(self):
        self.cardList = []

        for i in range(len(cardsuit)):
            for j in range(len(rank)):
                self.cardList.append(Card(cardsuit[i], rank[j]))

    #   shuffles the cards in the deck
    def shuffle(self):
        random.shuffle(self.cardList)

    #   prints out the cards in the deck
    def __str__(self):
        cardhold = ""
        cardhold = cardhold + "  "
        for i in range(len(self.cardList)):
            cardhold = cardhold + str(self.cardList[i]) + " "
            if i == 12 or i == 25 or i == 38:
                cardhold = cardhold + "\n  "
            elif i % 13 == 0 and i != 0 and i != 13 and i != 26 and i != 39:
                cardhold = cardhold + "\n  "

        cardhold = cardhold + "\n"

        return(cardhold)

    #   deals a card to a player
    def dealOne(self,player):

        (player.hand).append(self.cardList[0])
        del self.cardList[0]

#   creates a player to play the game
class Player:

    def __init__(self):
        self.hand = []

    #   allows us to see the contents of the player's hand
    def __str__(self):
        currenthand = ""
        currenthand = currenthand + " "
        for i in range(len(self.hand)):
            currenthand = currenthand + str(self.hand[i]) + " "
            if i == 12 or i == 25 or i == 38:
                currenthand = currenthand + "\n"
                currenthand = currenthand + " "
            elif i % 13 == 0 and i != 0 and i != 13 and i != 26 and i != 39:
                currenthand = currenthand + "\n"
                currenthand = currenthand + " "

        currenthand = currenthand + "\n"
        
        return(currenthand)

    #   determines if their hand still has cards in it
    def handNotEmpty(self):
        if len(self.hand) > 0:
            return True
        else:
            return False
        
#   allows us to play "war"
def playGame(cardDeck, player1, player2):

    #   variables to determine if the game continues and what round it is
    count = 1
    go = True

    #   while loop that keeps the game running until someone runs out of cards
    while go == True:
        
        #   prints out what round it is and the players' cards
        print("ROUND {}:".format(count))
        print("Player 1 plays: ", player1.hand[0])
        print("Player 2 plays: ", player2.hand[0])
        print()

        #   determines what do it if it is the card values are equal
        if player1.hand[0].value == player2.hand[0].value:
            print("War starts:" , player1.hand[0], "=", player2.hand[0])
            print("Player 1 puts", player1.hand[1], "face down")
            print("Player 2 puts", player2.hand[1], "face down")
            print("Player 1 puts", player1.hand[2], "face down")
            print("Player 2 puts", player2.hand[2], "face down")
            print("Player 1 puts", player1.hand[3], "face down")
            print("Player 2 puts", player2.hand[3], "face down")
            print("Player 1 puts", player1.hand[4], "face up")
            print("Player 2 puts", player2.hand[4], "face up")
            print()

            #   determines who wins the "war"
            if player1.hand[4].value > player2.hand[4].value:
                print("Player 1 wins round {}:".format(count), player1.hand[4], ">", player2.hand[4])
                (player1.hand).append(player1.hand[0])
                (player1.hand).append(player1.hand[1])
                (player1.hand).append(player1.hand[2])
                (player1.hand).append(player1.hand[3])
                (player1.hand).append(player1.hand[4])

                (player1.hand).append(player2.hand[0])
                (player1.hand).append(player2.hand[1])
                (player1.hand).append(player2.hand[2])
                (player1.hand).append(player2.hand[3])
                (player1.hand).append(player2.hand[4])

                del player2.hand[0]
                del player2.hand[0]
                del player2.hand[0]
                del player2.hand[0]
                del player2.hand[0]

                del player1.hand[0]
                del player1.hand[0]
                del player1.hand[0]
                del player1.hand[0]
                del player1.hand[0]


            elif player1.hand[4].value < player2.hand[4].value:
                print("Player 2 wins round {}:".format(count), player2.hand[4], ">", player1.hand[4])
                (player2.hand).append(player1.hand[0])
                (player2.hand).append(player1.hand[1])
                (player2.hand).append(player1.hand[2])
                (player2.hand).append(player1.hand[3])
                (player2.hand).append(player1.hand[4])

                (player2.hand).append(player2.hand[0])
                (player2.hand).append(player2.hand[1])
                (player2.hand).append(player2.hand[2])
                (player2.hand).append(player2.hand[3])
                (player2.hand).append(player2.hand[4])

                del player1.hand[0]
                del player1.hand[0]
                del player1.hand[0]
                del player1.hand[0]
                del player1.hand[0]

                del player2.hand[0]
                del player2.hand[0]
                del player2.hand[0]
                del player2.hand[0]
                del player2.hand[0]

            #   incase there's a double war
            elif player1.hand[4].value == player2.hand[4].value:
                print("War starts:" , player1.hand[4], "=", player2.hand[4])
                print("Player 1 puts", player1.hand[5], "face down")
                print("Player 2 puts", player2.hand[5], "face down")
                print("Player 1 puts", player1.hand[6], "face down")
                print("Player 2 puts", player2.hand[6], "face down")
                print("Player 1 puts", player1.hand[7], "face down")
                print("Player 2 puts", player2.hand[7], "face down")
                print("Player 1 puts", player1.hand[8], "face up")
                print("Player 2 puts", player2.hand[8], "face up")
                print()

                if player1.hand[8].value > player2.hand[8].value:
                    print("Player 1 wins round {}:".format(count), player1.hand[8], ">", player2.hand[8])
                    (player1.hand).append(player1.hand[0])
                    (player1.hand).append(player1.hand[1])
                    (player1.hand).append(player1.hand[2])
                    (player1.hand).append(player1.hand[3])
                    (player1.hand).append(player1.hand[4])
                    (player1.hand).append(player1.hand[5])
                    (player1.hand).append(player1.hand[6])
                    (player1.hand).append(player1.hand[7])
                    (player1.hand).append(player1.hand[8])

                    (player1.hand).append(player2.hand[0])
                    (player1.hand).append(player2.hand[1])
                    (player1.hand).append(player2.hand[2])
                    (player1.hand).append(player2.hand[3])
                    (player1.hand).append(player2.hand[4])
                    (player1.hand).append(player2.hand[5])
                    (player1.hand).append(player2.hand[6])
                    (player1.hand).append(player2.hand[7])
                    (player1.hand).append(player2.hand[8])

                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]

                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]

                elif player2.hand[8].value > player1.hand[8].value:
                    print("Player 2 wins round {}:".format(count), player2.hand[8], ">", player1.hand[8])
                    (player2.hand).append(player1.hand[0])
                    (player2.hand).append(player1.hand[1])
                    (player2.hand).append(player1.hand[2])
                    (player2.hand).append(player1.hand[3])
                    (player2.hand).append(player1.hand[4])
                    (player2.hand).append(player1.hand[5])
                    (player2.hand).append(player1.hand[6])
                    (player2.hand).append(player1.hand[7])
                    (player2.hand).append(player1.hand[8])

                    (player2.hand).append(player2.hand[0])
                    (player2.hand).append(player2.hand[1])
                    (player2.hand).append(player2.hand[2])
                    (player2.hand).append(player2.hand[3])
                    (player2.hand).append(player2.hand[4])
                    (player2.hand).append(player2.hand[5])
                    (player2.hand).append(player2.hand[6])
                    (player2.hand).append(player2.hand[7])
                    (player2.hand).append(player2.hand[8])

                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]
                    del player1.hand[0]

                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    del player2.hand[0]
                    
        #   determines who wins            
        elif player1.hand[0].value > player2.hand[0].value:
                print("Player 1 wins round {}:".format(count), player1.hand[0], ">", player2.hand[0])
                (player1.hand).append(player1.hand[0])
                (player1.hand).append(player2.hand[0])

                del player2.hand[0]
                del player1.hand[0]

        elif player1.hand[0].value < player2.hand[0].value:
                print("Player 2 wins round {}:".format(count), player2.hand[0], ">", player1.hand[0])
                (player2.hand).append(player1.hand[0])
                (player2.hand).append(player2.hand[0])

                del player1.hand[0]
                del player2.hand[0]

        count = count + 1

        #   prints out the players' hands after the round
        print()
        print("Player 1 now has", len(player1.hand), "card(s) in hand:")
        print(player1)
        print("Player 2 now has", len(player2.hand), "card(s) in hand:")
        print(player2)

        #   checks if the players' have cards left
        if len(player1.hand) < 1 or len(player2.hand) < 1:
            go = False
    

def main():
    
    #   main function from the assignment page
    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)

    print("Initial hands:")
    print ("Player 1:   ")
    print (player1)
    print ("\nPlayer 2:")
    print (player2)
    
    playGame(cardDeck,player1,player2)

    if player1.handNotEmpty():
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()
