from flask import Flask, jsonify, request
import data
import core

app = Flask(__name__)

@app.route('/')
def home():
    return """Welcome to the Dice API!<br>
                Use the endpoint <code>/random</code> to get a random number between 1 and 100.<br>
                Try <code>/roll/d6?n=3</code> to roll three 6-sided dice. ( try rolling a 37 sided die)"""

@app.route('/random')
def random_number():
    return jsonify({ "random_number" : core.rand100() })

@app.route('/roll/d<int:num_faces>')
def roll_dice(num_faces):
    num_dice = request.args.get('n', default=1, type=int)
    if num_faces < 1 or num_dice < 1:
        return jsonify({'error': 'Number of faces and number of dice must be positive integers.'}), 400
    
    result = core.roll_dice(num_faces, num_dice)

    if num_faces == 37:
        return jsonify([37] * 37) + """You found the Lucky 37 Jackpot!""" #  37 37's easter egg

    data.save_roll_history(result, source='flask_app')

    return jsonify(result)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)