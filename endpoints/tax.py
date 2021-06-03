import json
from flask import abort, jsonify, make_response, request
import logging
from models.tax import TaxCalculation
from flask_restful import Resource, reqparse

# Opening JSON file
file = open('tax_bands.json', "r")
# returns JSON object as a dictionary
tax_bands = json.load(file)
parser = reqparse.RequestParser()
parser.add_argument('income')


class Tax(Resource):

    def __init__(self):
        self.tax_calculation = TaxCalculation(tax_bands)

    def post(self):
        try:
            # Get required income field
            args = parser.parse_args()
            income = float(args['income'])

        except Exception as get_error:

            # Logging the error.
            logging.warning(get_error)

            # Return missing parameter error.
            return abort(400, description="There are missing or invalid parameters.")

        try:
            tax = self.tax_calculation.tax_calculation(income)
            return {'tax': tax}

        except Exception as error:
            return abort(400, description=str(error))
