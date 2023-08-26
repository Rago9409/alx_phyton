from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' when the root URL is navigated to.

    Returns:
        str: The message 'Hello HBNB!'
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' when the '/hbnb' URL is navigated to.

    Returns:
        str: The message 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C <text>' when the '/c/<text>' URL is navigated to.

    Args:
        text (str): The text variable in the URL.

    Returns:
        str: The message 'C <text>'
    """
    return f'C {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
