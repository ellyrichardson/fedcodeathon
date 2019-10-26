import requests
import json
from pprint import pprint

api_key = 'Q7m1szUGxW5Luh5SKv3uwQxyXWEnv6u_jqsO8AC5t-UhcUc7uTHDdxXMwN-3t8C_6hVY49_VASpCbGDjceRdsXOFzAY0SZb3slCyxZ07O5AeeXcmswWd0-iVsnO0XXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
url = 'https://api.yelp.com/v3/businesses/search'


class YelpRequester:
    def get_yelp_results(self, itemCriteria, itemLocation):
        # In the dictionary, term can take values like food, cafes or businesses like McDonalds
        # params = {'term': 'seafood', 'location': 'New York City'}
        params = {'term': itemCriteria, 'location': itemLocation}

        # Making a get request to the API
        req = requests.get(url, params=params, headers=headers)

        # proceed only if the status code is 200
        print('The status code is {}'.format(req.status_code))

        # printing the text from the response
        json.loads(req.text)

        # printing the text from response
        return json.loads(req.text)
        #


pprint(YelpRequester().get_yelp_results("restaurant", "Kansas City"))
