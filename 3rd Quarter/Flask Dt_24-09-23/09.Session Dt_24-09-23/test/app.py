from flask import Flask

app = Flask( __name__)


@app.route('/')
def home():
    return "Hello with Python with Flask"

@app.route('/about')
def about():
    return "Hello with Python with Flask"

if __name__ == "__main__":
    
    app.run(debug=True)
