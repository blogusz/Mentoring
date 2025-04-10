# Football analytics platform

## Project Description

The goal of the project is to create a football analytics platform, which will be gradually expanded with more
functionality. As for now the **https://www.thesportsdb.com/** free sports API was chosen as the project's main data
source. It has a request limit of 100 requests per minute on free tier.

## Project Timeline

### Week 1

**DONE**

- The **https://www.thesportsdb.com/** free sports API was chosen.
- Created functions for all available API requests and stored them in
  **[api_possible_requests](api_possible_requests/)**
  directory.
- Separated the functions by the type of
  operation - **[searches](api_possible_requests/searches.py)**, **[lists](api_possible_requests/lists.py)**,
  **[lookups](api_possible_requests/lookups.py)**
  and **[schedules](api_possible_requests/schedules.py)**.
- Added decorator for premium functions.

**TODO**

- Create functions for finding a Player's ID by their name, Club's ID by their name etc.
- Think about saving downloaded data to files.
- Search the available data for useful information.
- Convert the data into Pandas DataFrames (or similar) and analyze it.