
# deal two cards to player and two cards to computer
# if player has a natural (ace + 10) and dealer does not, playerwins 1.5x their bet
    # if deal face up card = 10 or ace, they look at the 2nd card
        # if dealer has a natural, collect bets of all players who don't have a natural

# if player draws an 11 (ace) can decide if 1 or 11

# player decides whether to stand or hit UNTIL they stand or bust (card total > 21)
    # if ace in original two cards, player can decide whether they want it as 1 or 11
    # if they pick 11 and draws a bust, the ace then counts as a 1 and the player continues by standing or hitting again

# dealer plays:
    # if total is 17+, must stand
    # hit until total is 17+
    # if ace, and counting is as 11 would bring total to 17+ but not over 21, the dealer must count it as 11 and stand


deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4 # Deck is total of 52 cards 
