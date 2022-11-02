from abc import ABC, abstractclassmethod

from typing import Dict, List

class StarshipsListColectorInterface(ABC):
    '''
        Startships Colector Interface
    '''
    @abstractclassmethod
    def list(self, page: int) -> List[Dict]:
        ''' must implement '''
        raise Exception('Must implement list method')
        