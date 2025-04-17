
import random

# Define card values and suits
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Function to create a deck of cards
def create_deck():
    deck = []
    for suit in card_suits:
        for value in card_values:
            deck.append(f"{value} of {suit}")
    random.shuffle(deck)
    return deck

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        card_value = card.split()
        if card_value in ['J', 'Q', 'K']:
            value += 10
        elif card_value == 'A':
            ace_count += 1
            value += 11
        else:
            value += int(card_value)
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

# Function to display hand
def display_hand(hand, name):
    print(f"{name}'s hand: {', '.join(hand)}")

# Function to play the game
def play_blackjack():
    # Initialize player's total money
    total_money = 1000
    while True:
        print(f"\nTotal money: ${total_money}")
        # Get player's betting amount
        bet = int(input("Enter your betting amount: "))
        if bet > total_money:
            print("You don't have enough money to place that bet.")
            continue
    # Create and shuffle deck
        deck = create_deck()
        # Deal initial hands
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        display_hand(player_hand, "Player")
        display_hand(dealer_hand[:1], "Dealer")
        # Player's turn
        while True:
            player_value = calculate_hand_value(player_hand)
            if player_value > 21:
                print("Bust! You lose.")
                total_money -= bet
                break
            action = input("Do you want to hit or stand? (hit/stand): ").lower()
            if action == "hit":
                player_hand.append(deck.pop())
                display_hand(player_hand, "Player")
            elif action == "stand":
                break
        # Dealer's turn
        if player_value <= 21:
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            display_hand(dealer_hand, "Dealer")
            dealer_value = calculate_hand_value(dealer_hand)
            if dealer_value > 21 or player_value > dealer_value:
                print("You win!")
                total_money += bet
            elif player_value < dealer_value:
                print("You lose.")
                total_money -= bet
            else:
                print("It's a tie!")
        # Check if player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print(f"\nGame over! You have ${total_money} left.")

# Start the game
play_blackjack()
