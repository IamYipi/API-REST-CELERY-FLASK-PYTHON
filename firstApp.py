# export FLASK_APP=firstApp.py
# flask run
from flask import Flask, jsonify
from flask_celery import make_celery
import redis

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'pyamqp://'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'
celery = make_celery(app)

examples = [{'name': "Example 0",
             'example_id': "0",
             'Description': "This is the example 0 for the API restful using flask",
             'price': "pay me with BTC"},
            {'name': "Example 1",
             'example_id': "1",
             'Description': "This is the example 1 for the API restful using flask",
             'price': "pay me with ETH"}]


# For lunch the API in a virtual machine local web server http://127.0.0.1:5000/ or http://localhost:5000/

@app.route('/')
def index():
    	text = "Welcome Yipi's API REST"
    	celery_monitor.delay("User in main page")
    	return text

# For run introduce the next url:
# http://127.0.0.1:5000/examples

@app.route("/examples", methods=['GET'])
def get():
	celery_monitor.delay("User in: /examples")
	update(examples)
	return jsonify({'Examples': examples})

# For run introduce the next url:
# http://127.0.0.1:5000/examples/id
# id is the number of the example you want to see


@app.route("/examples/<int:example_id>", methods=['GET'])
def get_example(example_id):
	celery_example.delay("User in: /examples/" + str(example_id))
	return jsonify({'example': examples[example_id]})


# For run introduce in a second terminal:
# curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/examples

@app.route("/examples", methods=['POST'])
def create():
	number = len(examples)
	example = {'name': "Example " + str(number),
	'example_id': str(number),
	'Description': "This is the example " + str(number) + " for the API restful using flask",'price': "pay me with SOL"}
	examples.append(example)
	celery_monitor.delay("User has created a new example")
	return jsonify({'Created': example})


# For run introduce in a second terminal:
# curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/examples/id
# -- id is the number you want to put

@app.route("/examples/<int:example_id>", methods=['PUT'])
def example_update(example_id):
	examples[example_id]['Description'] = "Description has been changed :D"
	celery_example.delay("User has changed the example " + str(example_id))
	return jsonify({'example': examples[example_id]})


# For run introduce in a second terminal:
# curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/examples/id
# -- id is the number you want to delete

@app.route("/examples/<example_id>", methods=['DELETE'])
def delete(example_id):
	examples.remove(examples[int(example_id)])
	celery_example.delay("User has deleted the example " + str(example_id))
	return jsonify({'result': True})

# Celery Task for monitor

@celery.task(name='celery_monitor')
def celery_monitor(string):
    return string

# Celery Task for examples id

@celery.task(name='celery_example_id')
def celery_example(string):
	return string

# Function for update jsonify examples

def update(examples):
	n = len(examples)
	for i in range(n):
		examples[i]['name'] = "Example " + str(i)
		examples[i]['example_id'] = str(i)
		examples[i]['Description'] = "This is the example " + str(i) + " for the API restful using flask"


# For run Main

if __name__ == '__main__':
    app.run(debug=True)
