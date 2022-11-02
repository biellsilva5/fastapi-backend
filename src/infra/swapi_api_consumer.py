import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SwapiApiConsumer:
    '''
        consumer api for swapi
    '''
    @classmethod
    def get_starships(cls, page: int) -> any:
        ''' get startships '''
        params = {'page': page}
        response = requests.get(
            'https://swapi.dev/api/starships/', params=params,timeout=10, verify=False)

        return response.json()
