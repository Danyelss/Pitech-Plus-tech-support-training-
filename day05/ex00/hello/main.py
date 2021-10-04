from flask import Flask

app = Flask(__name__)

@app.route('/hello_to_training')
def main():
	return 'Hy there'
