from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns a string "Hello HBNB!" when the route '/' is accessed.

    Returns:
        str: A string "Hello HBNB!".
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns a string "HBNB" when the route '/hbnb' is accessed.

    Returns:
        str: A string "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function returns a string "C <text>" when the route '/c/<text>' is accessed.

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
    This function returns a string "<n> is a number" when the route '/number/<n>' is accessed.

    Args:
        n (int): An integer to be displayed in the response.

    Returns:
        str: A string "<n> is a number".
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    This function returns an HTML page with the text "Number: <n>" when the route '/number_template/<n>' is accessed.

    Args:
        n (int): An integer to be displayed in the response.

    Returns:
        str: An HTML page with the text "Number: <n>".
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    This function returns an HTML page with the text "Number: <n> is even|odd" when the route '/number_odd_or_even/<n>' is accessed.

    Args:
        n (int): An integer to be displayed in the response.

    Returns:
        str: An HTML page with the text "Number: <n> is even|odd".
            If <n> is even, then 'even' will be displayed after <n>.
            If <n> is odd, then 'odd' will be displayed after <n>.
            For example, if n=3, then the response will be an HTML page with the text "Number: 3 is odd".
            If n=4, then the response will be an HTML page with the text "Number: 4 is even".
            The HTML page should contain an H1 tag with the text as described above.
            The H1 tag should be inside the tag BODY.
            The HTML page should also contain a DOCTYPE declaration and an HTML tag.
            The HTML tag should have a LANG attribute set to “en-US”.
            The HTML page should also contain a meta charset attribute set to “UTF-8” inside HEAD tag.
            The HTML page should also contain a TITLE tag with text “Number template” inside HEAD tag.
            The HTML page should also contain a DIV tag with text “Number: ” inside BODY tag.
            The HTML page should also contain a footer with text “Holberton School” and should be displayed within an
                HTML5 footer tag (<footer>) within BODY tag.
            You are not allowed to use conditional statements in this task.
            You have to use the modulo operator (%) to determine if an integer is odd or even.
            You can assume that n will always be an integer.
            You have to use jQuery
                You must use bootstrap for styling
                You are not allowed to use any CSS styling
                When creating your project, you should have only one HTML file for all routes and one CSS file for all styles
                Your styles.css must be as small as you can - you must use Bootstrap classes as much as you can
                You are not allowed to use words “if” and “else”
                You can only use one DIV and one UL for all elements """