from sports_api.config import Config
from sports_api.data_scraper import DataScraper
from sports_api.storage.file_storage import FileStorage
from sports_api.storage.db_storage import DatabaseStorage

if __name__ == '__main__':
    config = Config()

    # Test with file storage (default)
    print("=== Testing with File Storage ===")
    file_scraper = DataScraper(config, storage=FileStorage(config))
    countries = file_scraper.scrape_countries(save_data=True)
    print(f"Saved {len(countries.get('countries', []))} countries to files")

    # Test with database storage
    print("\n=== Testing with Database Storage ===")
    db_scraper = DataScraper(config, storage=DatabaseStorage(config))
    countries = db_scraper.scrape_countries(save_data=True)
    print(f"Saved countries to database")

    # Test leagues
    leagues = db_scraper.scrape_leagues(save_data=True)
    print(f"Saved leagues to database")
