import requests

from flask import redirect, render_template, session
from functools import wraps
import random


def apology(code, message):
    """
    Render an apology page with a random cat background.
    """
    # List of cat image URLs
    cat_images = [
        "https://i.imgur.com/D0Wpl64.jpeg",
        "https://i.imgur.com/tPhRO7R.jpeg",
        "https://i.imgur.com/PQtdjJz.jpeg"
    ]

    # Randomly select one image from the list
    random_cat = random.choice(cat_images)

    def escape(s):
        """
        Escape special characters for memegen.link.
        https://github.com/jacebrowning/memegen#special-characters
        """
        # Convert s to a string if it isn't already, default to empty string if None
        s = str(s) if s is not None else ""
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    # Ensure code is a string too, since it’s used in the URL
    code = str(code)

    # Render the template with the random cat image
    return render_template(
        "apology.html",
        top=code,
        bottom=escape(message),
        background=random_cat
    ), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function