from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns a string "Hello HBNB!" 
    when the route '/' is accessed.

    Returns:
        str: A string "Hello HBNB!".
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns a string "HBNB"
    when the route '/hbnb' is accessed.

    Returns:
        str: A string "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function returns a string "C <text>" 
    when the route '/c/<text>' is accessed.

    Args:
        text (str): A string to be displayed after "C".

    Returns:
        str: A string "C <text>".
    """
    return f'C {text.replace("_", " ")}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    This function returns a string "Python <text>" when the route '/python/<text>' is accessed.

    Args:
        text (str): A string to be displayed after "Python".

    Returns:
        str: A string "Python <text>".
    """
    return f'Python {text.replace("_", " ")}'


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
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    This function returns an HTML page with the text "Number: <n>" 
    when the route '/number_template/<n>' is accessed.

    Args:
        n (int): An integer to be displayed in the response.

    Returns:
        str: An HTML page with the text "Number: <n>".
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    This function returns an HTML page with the text "Number: <n> is even|odd" 
    when the route '/number_odd_or_even/<n>' is accessed.

    Args:
        n (int): An integer to be displayed in the response.

    Returns:
        str: An HTML page with the text "Number: <n> is even|odd".
            If <n> is even, then 'even' will be displayed after <n>.
            If <n> is odd, then 'odd' will be displayed after <n>.
             """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

