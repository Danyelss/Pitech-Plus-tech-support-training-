from flask import Flask, render_template
import os

template_dir = os.path.abspath('app/templates')
static_dir = os.path.abspath('app/static')
app = Flask(__name__,template_folder=template_dir, static_folder=static_dir)

@app.route('/hello_to_training')
def main():
	return render_template('public/index.html')

