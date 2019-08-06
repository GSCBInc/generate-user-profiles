from urllib import parse, request

import logging
import json
import re

logger = logging.getLogger(__name__)


class RestClient:

	@staticmethod
	def set_url_params(url, params):
		for p in params:
			url = re.sub('{' + p + '}', parse.quote(params[p]), url)

		logger.info('Requesting url: %s', url)
		return url

	@staticmethod
	def get(url, params):
		response = request.urlopen(request.Request(RestClient.set_url_params(url, params), method='GET')).read()
		return json.loads(response.decode())
