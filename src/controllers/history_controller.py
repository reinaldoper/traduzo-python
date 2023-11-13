from flask import Blueprint, jsonify
from models.history_model import HistoryModel

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def history():

    history = HistoryModel.list_as_json()
    if not history:
        return jsonify({"error": "History not found"}), 404
    else:
        return jsonify(history), 200
