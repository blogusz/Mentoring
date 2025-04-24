"""Endpoint definitions for the Sports DB API."""

from sports_api.endpoints.lists import Lists
from sports_api.endpoints.lookups import Lookups
from sports_api.endpoints.schedules import Schedules
from sports_api.endpoints.searches import Searches

__all__ = ['Lists', 'Lookups', 'Schedules', 'Searches']