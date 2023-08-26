from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    This function returns a string "Hello HBNB!" when the route '/' is accessed.

    Returns:
        str: A string "Hello HBNB!".
    """
    return 'Hello HBNB!'
   

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns a string "HBNB!" when the route '/' is accessed.

    Returns:
        str: A string "HBNB!".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    This function returns a string "C <text>" when the route '/c/<text>' is accessed.

    Args:
        text (str): A string to be displayed after "C".

    Returns:
        str: A string "C <text>".
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    This function returns a string "Python <text>" when the route '/python/<text>' is accessed.

    Args:
        text (str): A string to be displayed after "Python".

    Returns:
        str: A string "Python <text>".
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    This function returns a string "<n> is a number"
    when the route '/number/<n>' is accessed.

    Args:
        n (int): An integer to be displayed in the response.

    Returns:
        str: A string "<n> is a number".
    """
    
    
    return '{} is a number'.format(n)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
