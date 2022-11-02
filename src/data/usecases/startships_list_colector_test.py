from .startships_list_colector import StarshipsListColector
from src.infra import SwapiApiConsumer

def test_list():
    '''
        Testing List
    '''

    api_consumer =  SwapiApiConsumer()
    startships_list_colector = StarshipsListColector(api_consumer)

    page = 1
    startships_list_colector.list(page)
    