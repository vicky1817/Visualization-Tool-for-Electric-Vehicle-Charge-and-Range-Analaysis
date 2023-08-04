from flask import Flask, render_template
import os

app = Flask(__name__)

# Specify the path to the templates folder
template_dir = os.path.abspath('EVcars')
app.template_folder = template_dir

@app.route('/')
def index():
    return render_template('evhtml.html')

if __name__ == '__main__':
    app.run(debug=True)
