import json

from requests import Response
from utils.checking import Checking

from utils.api import Google_maps_api

"""Create, update and delete new location"""


class Test_create_test:

    def test_create_new_place(self):

        print('Method POST')
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        print(list(token))
        Checking.check_json_value_token(result_post, 'status', 'OK')

        print("Method GET POST")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_value_token(result_get, "address", "29, side layout, cohen 09")

        print("Method PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        token = json.loads(result_put.text)
        print(list(token))
        Checking.check_json_value_token(result_put, "msg", "Address successfully updated")

        print("Method GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_value_token(result_get, "address", "100 Lenina street, RU")

        print("Method DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        token = json.loads(result_delete.text)
        print(list(token))
        Checking.check_json_value_token(result_delete, 'status', 'OK')

        print("Method GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_search_word_in_value_token(result_get, 'msg', 'failed')

        print("All tests PASSED")
