from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from endpoints.tax import Tax

app = Flask(__name__)
CORS(app)
api = Api(app)
app.debug = True
api.add_resource(Tax, '/income-tax')

if __name__ == '__main__':
    app.run()
