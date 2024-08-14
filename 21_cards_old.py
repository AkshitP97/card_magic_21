import random

# Step 1: Create a deck and select 21 cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def select_cards(deck, num=21):
    return random.sample(deck, num)

# Step 2: Arrange cards in 3 columns
def arrange_in_columns(cards):
    columns = [[], [], []]
    for i, card in enumerate(cards):
        columns[i % 3].append(card)
    return columns

# Step 3: Display cards to the user
def display_columns(columns):
    # Print the columns row by row
    print("Here are the cards arranged in 3 columns:")
    for row in range(7):
        row_display = []
        for col in range(3):
            row_display.append(f"{columns[col][row][0]} of {columns[col][row][1]}")
        print(f"Row {row+1}: {row_display[0]} | {row_display[1]} | {row_display[2]}")

# Step 4: Rearrange based on user input
def rearrange_columns(columns, chosen_column):
    # Place the chosen column in the middle
    new_order = [columns[i] for i in range(3) if i != chosen_column]
    new_order.insert(1, columns[chosen_column])
    # Flatten the columns back into a single list of cards
    return [card for col in new_order for card in col]

# Step 5: Main logic loop
def play_game():
    deck = create_deck()
    selected_cards = select_cards(deck)
    
    for _ in range(3):
        columns = arrange_in_columns(selected_cards)
        display_columns(columns)
        
        # Ask the user to pick a column (1, 2, or 3)
        chosen_column = int(input("Which column (1, 2, or 3) is your card in? ")) - 1  # Subtract 1 to adjust for index
        selected_cards = rearrange_columns(columns, chosen_column)
    
    # Step 6: Reveal the 11th card
    print(f"\nYour card is: {selected_cards[10][0]} of {selected_cards[10][1]}")

# To run the game
play_game()
