from flask import Blueprint, request, jsonify
import logging
import datetime as dt
from config.db_connection import app_configuration
from bson import json_util, ObjectId
import json
from datetime import datetime, timedelta
from routes import api
import os
from http import HTTPStatus
from dotenv import load_dotenv
load_dotenv()


_logger = logging.getLogger(__name__)
monitor_bp = Blueprint('monitor_bp', __name__)


@monitor_bp.route(api.route['root'], methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        _logger.info('root endpoint OK')
        return jsonify({"message": "ok", "status": True}), HTTPStatus.ACCEPTED


@monitor_bp.route(api.route['health_check'], methods=['GET', 'POST'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return jsonify({"message": "ok", "status": True}), HTTPStatus.ACCEPTED
