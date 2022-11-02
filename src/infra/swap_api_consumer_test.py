from .swapi_api_consumer import SwapiApiConsumer

def test_get_starships():
    ''' Testing get staships method'''
    response = SwapiApiConsumer().get_starships(1)
    print(response)
    
