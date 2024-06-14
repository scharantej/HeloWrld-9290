
from flask import Flask, render_template

# Create a Flask app.
app = Flask(__name__)

# Define the route for the home page.
@app.route('/')
def home():
    # Render the hello.html template.
    return render_template('hello.html')

# Run the app.
if __name__ == '__main__':
    app.run(debug=True)
