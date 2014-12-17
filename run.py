"""run.py

An example app, demonstrating how to use the jsonrpcserver library.
"""

from flask import Flask
from jsonrpcserver import bp, dispatch, exceptions

# Create a Flask app and register the blueprint.
app = Flask(__name__)
app.register_blueprint(bp)

# Add a route to dispatch requests to the handling methods.
@app.route('/', methods=['POST'])
def index():
    return dispatch(HandleRequests)

# Now go ahead and write the methods that will carry out the requests.
class HandleRequests:

    def add(x, y):
        try:
            return x + y
        except TypeError as e:
            raise exceptions.InvalidParams('Type error')

if __name__ == '__main__':
    app.run()
