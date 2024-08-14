from flask import Flask, render_template, jsonify, request
import random
from game_21_cards import create_deck, select_cards, arrange_in_columns, rearrange_columns

app = Flask(__name__)

game_state = {
    "deck": create_deck(),
    "selected_cards": [],
    "round": 0
}

def reset_game():
    game_state["deck"] = create_deck()
    game_state["selected_cards"] = []
    game_state["round"] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_cards', methods=['GET'])
def get_cards():
    if game_state["round"] == 0:
        game_state["selected_cards"] = select_cards(game_state["deck"])
    columns = arrange_in_columns(game_state["selected_cards"])
    cards = [{'rank': card[0], 'suit': card[1]} for card in game_state["selected_cards"]]
    return jsonify({"cards": cards})

@app.route('/select_column', methods=['POST'])
def select_column():
    data = request.json
    selected_column = int(data["column"]) - 1
    
    columns = arrange_in_columns(game_state["selected_cards"])
    game_state["selected_cards"] = rearrange_columns(columns, selected_column)
    game_state["round"] += 1
    
    if game_state["round"] < 3:
        return jsonify({"round": game_state["round"]})
    else:
        revealed_card = game_state["selected_cards"][10]
        return jsonify({"revealed_card": {"rank": revealed_card[0], "suit": revealed_card[1]}})

@app.route('/reset', methods=['POST'])
def reset():
    reset_game()
    return jsonify({"message": "Game reset successful!"})

if __name__ == '__main__':
    app.run(debug=True)
