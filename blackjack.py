import random
import time

# Creates deck and randomizes it
deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11] * 4 # Deck is total of 52 cards
random.shuffle(deck)

# Creates bank
bank = 500

# Start function
def startUp(bank):
    print('---------------------------------------------')
    print('      Welcome to the game - BLACKJACK!       ')
    print('---------------------------------------------\n')
    print 'You have $%d in the bank.\n' % bank


# Placing bets
def betting(bank):
    wager = int(raw_input("How much would you like to bet? $"))

    if wager > bank:
        print("I'm sorry. You do not have enough money in the bank for that bet. Please try again. ")
        betting(bank)
    else:
        print("You placed a $%d bet.\n\n" % wager)
        return wager

# Initialize player and dealer hands
def initial_hands(cards):
    player_cards = []
    dealer_cards = []
    player_cards.insert(0, cards.pop(0))
    player_cards.insert(1, cards.pop(0))
    dealer_cards.insert(0, cards.pop(0))
    dealer_cards.insert(1, cards.pop(0))

    # Check for duplicate 11s (because no ace specificity in this game)
    if sum(player_cards) > 21:
        player_cards.pop(1)
        player_cards.insert(1, 1)

    if sum(dealer_cards) > 21:
        player_cards.pop(1)
        player_cards.insert(1, 1)

    print "Your cards: ", player_cards
    print "The dealer's cards: ", dealer_cards[0]

    return (player_cards, dealer_cards)

# Player turn function
def playerTurn(deck, player_hand, bank, wager):
    # Checks for bust or blackjack
    if sum(player_hand) > 21:
        time.sleep(1)
        bank -= wager
        print ("\n\nYou BUST. You lose!")
        print "Your bank total is now: $%d" % bank
        # Play Again Option
        play_again = int(raw_input("Would you like to play again? Press 1 to play again. Press 0 to quit. "))
        exit(0) if play_again == 0 else main(deck, bank)
    elif sum(player_hand) == 21:
        time.sleep(1)
        bank += wager
        print ("\n\nYou have a BLACKJACK! YOU WIN!")
        print "Your bank total is now: $%d" % bank
        # Play Again Option
        play_again = int(raw_input("Would you like to play again? Press 1 to play again. Press 0 to quit. "))
        exit(0) if play_again == 0 else main(deck, bank)
    # Choice to hit or stand
    else:
        choice = int(raw_input("Hit - press 1\tStand - press 0: "))
        # Hit
        if choice == 1:
            time.sleep(1)
            player_hand.append(deck.pop(0))
            print "Your cards are: ", player_hand
            playerTurn(deck, player_hand, bank, wager)
        # Stand
        elif choice == 0:
            time.sleep(1)
            pass

    return player_hand

# Dealer turn function
def dealerTurn(deck, d_hand, bank, wager):

    while sum(d_hand) < 17:
        d_hand.append(deck.pop(0))
        print "The dealer's cards are: ", d_hand
        time.sleep(1)

    if sum(d_hand) > 21:
        bank += wager
        print ("\n\nThe dealer has a BUST. YOU WIN!")
        print "Your bank total is: $%d" % bank
        # Play Again Option
        play_again = int(raw_input("Would you like to play again? Press 1 to play again. Press 0 to quit. "))
        exit(0) if play_again == 0 else main(deck, bank)
    else:
        return d_hand

# Score calculation function
def scoreCalc(p_sum, d_sum, bank, wager):
    print "Your total: %d\t Dealer total: %d" %(p_sum, d_sum)

    if p_sum == d_sum:
        print "\n\nYou have TIED."
        print "Your bank total is: $%d" % bank
        return bank
    elif p_sum > d_sum:
        bank += wager
        print "\n\nYou WIN! CONGRATULATIONS!"
        print "Your bank total is: $%d" % bank
        return bank
    elif p_sum < d_sum:
        bank -= wager
        print "\n\nYou LOSE. Try again next time."
        print "Your bank total is: $%d" % bank
        return bank


# MAIN GAME LOOP
def main(deck, bank):

    # Resets deck
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11] * 4 # Deck is total of 52 cards
    random.shuffle(deck)

    # Check bank total
    if bank <= 0:
        print "You are out of money!"
        exit()

    # Initialize bet and card hands
    startUp(bank)
    wager = betting(bank)
    (p_hand, d_hand) = initial_hands(deck)

    # Check for blackjack on first two draws
    if (p_hand[0] + p_hand[1] == 21) and (int(d_hand[0]) + int(d_hand[1]) != 21):
        bank += 1.5 * wager
        print ("\nYou have a BLACKJACK! YOU WIN!")
        print "Your bank total is now: $%d" % bank
        # Play Again Option
        play_again = int(raw_input("Would you like to play again? Press 1 to play again. Press 0 to quit. "))
        exit(0) if play_again == 0 else main(deck, bank)
    elif (d_hand[0] + d_hand[1] == 21) and (int(p_hand[0]) + int(p_hand[1]) != 21):
        bank -= wager
        print ("\nThe dealer has a blackjack. You lose.")
        print "Your bank total is now: $%d" % bank
        # Play Again Option
        play_again = int(raw_input("Would you like to play again? Press 1 to play again. Press 0 to quit. "))
        exit(0) if play_again == 0 else main(deck, bank)
    elif (d_hand[0] + d_hand[1] == 21) and (int(p_hand[0]) + int(p_hand[1]) == 21):
        print ("\nBoth you and the dealer have blackjacks. You tie.")
        print "Your bank total is: $%d" % bank
        # Play Again Option
        play_again = int(raw_input("Would you like to play again? Press 1 to play again. Press 0 to quit. "))
        exit(0) if play_again == 0 else main(deck, bank)

    else:
        # Player Turn
        p_hand_final = playerTurn(deck, p_hand, bank, wager)

        # Dealer Turn
        d_hand_final = dealerTurn(deck, d_hand, bank, wager)

        # Score Calculation if no blackjacks or busts
        bank = scoreCalc(sum(p_hand_final), sum(d_hand_final), bank, wager)
        play_again = int(raw_input("Would you like to play again? Press 1 to play again. Press 0 to quit. "))
        exit(0) if play_again == 0 else main(deck, bank)

# DRIVER CODE
main(deck, bank)
