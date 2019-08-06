from app.csv.utils import CsvReader
from app.csv.utils import CsvWriter
from app.http.services import RestClient
from app.user.utils import Transformer

import logging

logger = logging.getLogger(__name__)


class Application:

	def __init__(self):
		self.url_index = None
		self.urls = [
			'https://node-data-generator.herokuapp.com/api/names/fullNames?n=5000',
			'https://randomuser.me/api/?inc=name,location&results=5000&nat=us'
		]
		self.roles = [
			'District Admin', 'Principal', 'Assistant Principal',
			'Counselor', 'Security Resource Officer'
		]

	def get_generated_names(self):
		self.url_index = 1 if self.url_index == 0 else 0
		return RestClient.get(self.urls[self.url_index], {})

	def start(self):
		logger.info('Application has started')
		schools = CsvReader.read()

		logger.info('Read [%s] records', len(schools))
		user_profiles = []
		users = []

		for school in schools:
			logger.info('School: %s', school['Name'])

			for role in self.roles:
				for index in range(0, 5):

					if len(users) == 0:
						data = self.get_generated_names()

						if self.url_index == 1:
							users = data['results']
						else:
							users = data

					user_profiles.append(Transformer.create_user_profile(users.pop(0), school, role))

		CsvWriter.write(data=user_profiles)