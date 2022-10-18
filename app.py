from flask import Flask, render_template, session, request, flash, redirect, jsonify
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"] = "BlahBlahBlah"


@app.route('/')
def home():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('/boggle.html', board=session['board'])

@app.route('/handle', methods=['POST'])
def handledata():
    guess = request.json.get('guess')
    result = boggle_game.check_valid_word(session['board'], guess)
    return jsonify({'answer': result})
