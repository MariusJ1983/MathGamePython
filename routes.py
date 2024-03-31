from flask import Blueprint, render_template, request, redirect, url_for
from game_logic import Game

game = Blueprint('game', __name__)
game_instance = Game()

@game.route('/')
def index():
    return render_template('index.html')

@game.route('/play', methods=['POST'])
def play():
    difficulty = request.form['difficulty']
    game_instance.start(difficulty)
    return redirect(url_for('game.play_game'))

@game.route('/play/game')
def play_game():
    if game_instance.is_game_over():
        return redirect(url_for('game.result'))
    return render_template('play.html', problem=game_instance.get_current_problem(), game_instance=game_instance)


@game.route('/play/answer', methods=['POST'])
def submit_answer():
    answer = int(request.form['answer'])
    game_instance.check_answer(answer)
    return redirect(url_for('game.play_game'))

@game.route('/result')
def result():
    return render_template('result.html', score=game_instance.get_score(), total_questions=game_instance.get_total_questions())
