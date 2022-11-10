from typing import Optional, Iterable

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from builder import query_builder
from models import BatchRequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        # Проверка на ошибки
        params = BatchRequestParams().load(data=request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result: Optional[Iterable[str]] = None
    for query in params['queries']:
        result = query_builder(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )

    return jsonify(result)
