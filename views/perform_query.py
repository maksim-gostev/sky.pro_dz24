import os

from flask import request, jsonify
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

from utils import execute
from models import BatchRequestSchema

perform_query_ns = Namespace('perform_query')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")

@perform_query_ns.route('')
class Perform_query(Resource):
    def post(self):
        req_json = request.json

        try:
            BatchRequestSchema().load(req_json)
        except ValidationError as e:
            return jsonify(e.messages), 400

        filename = os.path.join(DATA_DIR, req_json["file_name"])

        if not os.path.exists(filename):
            return 'Фаила не существует', 400

        result = None
        for query in req_json["queryes"]:
            result = execute(
                cmd=query["cmd"],
                value=query["value"],
                file_name=filename,
                data=result
            )
        return result


