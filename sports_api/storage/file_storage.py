from typing import Any

from sports_api.storage.storage_interface import StorageInterface
from sports_api.utils.file_utils import save_json_file
from sports_api.config import Config
from sports_api.utils.datascraper_utils import generate_file_path


class FileStorage(StorageInterface):
    """
    Implementation of the StorageInterface that saves data to files.
    """

    def __init__(self, config: Config):
        self.config = config

    def save(self, data: Any, data_type: str = None, **kwargs) -> None:
        """
        Save data to a file.

        :param data: Data to be saved
        :param data_type: Type of data for naming/categorization
        :param kwargs: Additional parameters for file storage (path, filename, etc.)
        """
        output_path = kwargs.get('output_path')
        output_file = kwargs.get('output_file')

        if data_type and not (output_path and output_file):
            generated_path, generated_file = generate_file_path(self.config, data_type, **kwargs)
            final_path = output_path or generated_path
            final_file = output_file or generated_file
        else:
            storage_config = self.config.get_output_settings()
            final_path = output_path or storage_config['output_path']
            final_file = output_file or storage_config['default_file']

        save_json_file(data, final_path, final_file)
