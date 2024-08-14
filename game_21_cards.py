import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def select_cards(deck, num=21):
    return random.sample(deck, num)

def arrange_in_columns(cards):
    columns = [[], [], []]
    for i, card in enumerate(cards):
        columns[i % 3].append(card)
    return columns

def rearrange_columns(columns, chosen_column):
    new_order = [columns[i] for i in range(3) if i != chosen_column]
    new_order.insert(1, columns[chosen_column])
    return [card for col in new_order for card in col]
