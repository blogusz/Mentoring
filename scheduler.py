import datetime

import schedule
from sports_api.config import Config
from sports_api.data_scraper import DataScraper


def job_scrape_league_table():
    print(f"Starting job at {datetime.datetime.now()}...")
    print("Scraping league table...")
    config = Config()
    scraper = DataScraper(config)
    scraper.scrape_league_table(
        league_id=4335,  # Spanish La Liga
        season='2024-2025',
        save_data=True,
    )
    print(f"Finished job at {datetime.datetime.now()}.", end="\n\n\n")


def job_scrape_all_rounds():
    print(f"Starting job at {datetime.datetime.now()}...")
    print("Scraping all rounds...")
    config = Config()
    scraper = DataScraper(config)
    scraper.scrape_all_rounds(
        league_id=4335,  # Spanish La Liga
        season='2024-2025',
        start_round=1,
        save_all_rounds=True,
        save_individual_rounds=True,
    )
    print(f"Finished job at {datetime.datetime.now()}.", end="\n\n\n")


def main():
    schedule.every().sunday.at("23:30").do(job_scrape_league_table)
    schedule.every().sunday.at("23:30").do(job_scrape_all_rounds)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
