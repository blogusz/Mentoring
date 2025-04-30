import os
import yaml
from typing import Optional


class Config:
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None,
                 config_path: Optional[str] = None):
        """
        Initialize configuration either from parameters or YAML file.

        :param api_key: Optional API key
        :param base_url: Optional base URL
        :param config_path: Optional path to YAML config file
        """
        if api_key and base_url:
            self.api_key = api_key
            self.base_url = base_url
        else:
            self._load_config(config_path)

            # Always mask API key with at least 4 asterisks
            api_display = 'Not set' if not self.api_key else ('*' * max(4, len(str(self.api_key))))

            print(f"""Configuration loaded successfully:
            - API Key  : {api_display}
            - Base URL : {self.base_url}
            - Storage Path : {self.get_output_settings()['output_path']}\n""")

    def _load_yaml_config(self, config_path: Optional[str] = None) -> bool:
        """
        Load configuration from YAML file.

        :param config_path: Path to YAML config file
        :return: True if successful, False otherwise
        """
        paths_to_try = [
            config_path,
            'config/config.yaml',
        ]

        for path in paths_to_try:
            if path and os.path.exists(path):
                try:
                    with open(path, 'r') as f:
                        self.config_data = yaml.safe_load(f)

                    self.api_key = self.config_data['api']['key']
                    self.base_url = self.config_data['api']['base_url']
                    return True
                except (yaml.YAMLError, KeyError) as e:
                    print(f"Error loading YAML config from {path}: {e}")

        return False

    def _load_config(self, config_path: Optional[str] = None) -> None:
        if not self._load_yaml_config(config_path):
            raise ValueError(
                "Failed to load configuration. Please provide a valid YAML config file or API credentials.")

    def get_credentials(self):
        return self.api_key, self.base_url

    def get_output_settings(self) -> dict:
        """
        Get output-related configuration.
        Returns merged configuration with defaults for missing values.
        """
        defaults = {
            'output_path': 'retrieved_data/',
            'default_file': 'data.json'
        }

        if 'data' not in self.config_data:
            return defaults

        # Merge defaults with values from config file
        config = defaults.copy()
        config.update(self.config_data['data'])
        return config
