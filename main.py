"""
Start flask app
"""
from justicia_digital import app

app = app.create_app()


if __name__ == '__main__':
    app.run()
