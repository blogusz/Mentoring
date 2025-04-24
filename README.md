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
  `api_possible_requests` directory.
- Separated the functions by the type of operation - `searches`, `lists`, `lookups` and `schedules`.
- Added decorator for premium functions.

**TODO**

- Create functions for finding a Player's ID by their name, Club's ID by their name etc.
- Think about saving downloaded data to files.
- Search the available data for useful information.
- Convert the data into Pandas DataFrames (or similar) and analyze it.

### Week 2

**DONE**

- Added option to save data.
- Refactored the test functions.
- Reorganized the project structure.

**TODO**

- Setup project in Jira.
- Start working on feature branches.
- Implement the Config class.

### Week 3

**DONE**

- Set up the Jira project.
- Started working on feature branches.
- Implemented the Config class.
- Separated the data scraper abstraction layers.
- Implemented classes for other functions.

**TODO**

- Integrate Jira with GitHub.
- Create the API Client class.
- Create project configuration file in YAML.
- Start logging messages instead of printing them.

### Week 4

**DONE**

- Completely restructured the project into the `sports_api` package.
- Implemented service-oriented architecture while retaining the previous separation of requests by type.
- Created a user-friendly `ApiClient` class that abstracts away implementation details.
- Organized code into logical components: endpoints, services, and core modules.
- Added comprehensive documentation with usage examples.

**TODO**

- Add unit tests for all components.
- Implement logging instead of print statements.
- Create a project configuration file in YAML or TOML (Poetry).
- Add data analysis using Pandas.