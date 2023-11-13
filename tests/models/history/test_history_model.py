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
    history_data = json.loads(history_json)

    for item in history_data:
        item.pop('_id', None)

    assert history_data == expected_data
