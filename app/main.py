from app.csv.utils import CsvReader
from app.csv.utils import CsvWriter
from app.http.services import RestClient
from app.user.utils import Transformer

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
		self.urls = [
			'https://uinames.com/api/?region={region}&amount=5',
			'https://randomuser.me/api/?inc=name&results=5'
		]
		self.roles = [
			'District Admin', 'Principal', 'Assistant Principal',
			'Counselor', 'Security Resource Officer'
		]

	def start(self):
		logger.info('Application has started')
		schools = CsvReader.read()

		logger.info('Read [%s] records', len(schools))

		for school in schools:
			logger.info('School: %s', school['Name'])
			base_url = self.urls[1]

			for role in self.roles:
				users = RestClient.get(base_url, {})
				users = users['results']

				user_profiles = Transformer.create_user_profiles(users, school, role)
				CsvWriter.write(data=user_profiles)
