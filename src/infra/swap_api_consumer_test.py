from .swapi_api_consumer import SwapiApiConsumer


def test_get_starships(requests_mock):
    ''' Testing get staships method'''
    requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'some': 'thing'})

    response = SwapiApiConsumer().get_starships(1)
    print(response)
    
