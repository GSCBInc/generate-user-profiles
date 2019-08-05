from app.csv.utils import CsvReader

import logging

logger = logging.getLogger(__name__)


class Application:

	def __init__(self):
		self.allowed_regions = [
			'Albania', 'Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada',
			'Colombia', 'Costa Rica', 'Denmark', 'England', 'France', 'Germany', 'India',
			'Indonesia', 'Ireland', 'Italy', 'Mexico', 'Morocco', 'Nepal', 'New Zealand',
			'Nigeria', 'Pakistan', 'Poland', 'Portugal', 'Spain', 'Turkey', 'United States'
		]

	def start(self):
		logger.info('Application has started')
		schools = CsvReader.read()

		logger.info('Read [%s] records', len(schools))
