# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hullo")

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

# Dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	if search_query.lower() == 'michael':
		return 'Hello... {}'.format(search_query)
	else:
		return 'Not Found'

# Different data values

@app.route("/integer/<int:integer>")
def int_type(integer):
	print(integer)
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print(value)
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"

# start the development server using the run() method
if __name__ == "__main__":
	app.run()