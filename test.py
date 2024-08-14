def arrange_in_columns(cards):
    columns = [[], [], []]
    for i, card in enumerate(cards):
        columns[i % 3].append(card)
    return columns

cards = [1,2,3,4,5,6]

arrange_in_columns(cards)