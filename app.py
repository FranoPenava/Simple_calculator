from flask import Flask, render_template
from main import main

# This is file for running my project!

app = Flask(__name__)

# Registration of my bluprint I created in main.py file!
app.register_blueprint(main)


if __name__ == "__main__":
    app.run(debug=True)