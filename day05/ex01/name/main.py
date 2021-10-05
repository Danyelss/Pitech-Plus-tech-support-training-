from flask import Flask, render_template
import os
from subprocess import Popen, call

template_dir = os.path.abspath('app/templates')
static_dir = os.path.abspath('app/static')
app = Flask(__name__,template_folder=template_dir, static_folder=static_dir)

@app.route('/hello_to_training/<name>')
def main(name):
    pathVar = name
    #Popen("export FLASK_RUN_PORT=8080")
    #call(["export", "FLASK_RUN_PORT=8080"])
    #os.system("export FLASK_RUN_PORT=8080")
    return render_template('public/index.html',value=pathVar)

if __name__ == "__main__":
    app.run(port=8080)