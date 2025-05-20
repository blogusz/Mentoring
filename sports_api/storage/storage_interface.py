from abc import ABC, abstractmethod
from typing import Any


class StorageInterface(ABC):
    """Interface for data storage implementations."""

    @abstractmethod
    def save(self, data: Any, data_type: str = None, **kwargs) -> str:
        """
        Save data using the storage implementation.

        :param data: Data to be saved
        :param data_type: Type of data for naming/categorization
        :param kwargs: Additional parameters for storage (path, filename, etc.)
        :return: Identifier or location where data was saved
        """
        pass
