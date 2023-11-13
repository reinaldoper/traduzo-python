import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    expected_data = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]
    history_json = HistoryModel.list_as_json()

    assert json.loads(history_json) == expected_data
