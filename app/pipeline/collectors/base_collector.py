from abc import ABC, abstractmethod
from typing import List, Dict


class BaseCollector(ABC):
    """
    Classe base para todos os coletores de dados.
    """

    @abstractmethod
    def collect(self) -> List[Dict]:
        """
        Deve retornar uma lista de registros coletados.
        """
        pass