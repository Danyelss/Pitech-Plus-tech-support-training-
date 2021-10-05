from flask import Flask, render_template
import os

template_dir = os.path.abspath('app/templates')
static_dir = os.path.abspath('app/static')
app = Flask(__name__,template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def main():
    return render_template('public/index.html')

@app.route('/prices')
def prices():
    return render_template('public/prices.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')