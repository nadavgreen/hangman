# External Modules
from flask import Flask, jsonify, request

#Internal Modules
from game_modules.game_class import Game

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def pong():
	if request.method == 'GET':
		pass
		return jsonify({'msg': 'pong'})

@app.route('/', methods=['GET', 'POST'])
def game():
	if request.method == 'GET':
		pass
		return jsonify({'msg': 'Welcome to hangman microservice'})
	elif request.method == 'POST':
		pass
		req = request.get_json()

		game = None
		res = {
			'msg': None
		}
		
		res['msg'] = str(req)

		try:
			game = Game.check(**req)
		except TypeError as err:
			res['msg'] = str(err)
		except ValueError as err:
			res['msg'] = str(err)
		else:
			res['msg'] = game

		return jsonify(res)

if __name__ == '__main__':
	app.debug = True
	app.run()
