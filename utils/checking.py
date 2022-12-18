"""Method for tests responses our requests"""
import json

from requests import Response


class Checking:
    """Метод для проверки статуса кода"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"TEST PASSED. Status code: {response.status_code}")

    """Метод для проверки наличия обязательных полей в ответах запроса"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('All columns are in place')

    """Метод для проверки значений обязательных полей в ответе запроса"""


    @staticmethod
    def check_json_value_token(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'test: PASSED. {field_name} equal')

    @staticmethod
    def check_json_search_word_in_value_token(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f'Word {search_word} in')
        else:
            print('Word {search_word} out')

