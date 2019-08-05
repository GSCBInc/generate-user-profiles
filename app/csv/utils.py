import csv


class CsvReader:

	properties = ['Name', 'Phone', 'Address']
	folder = 'data/'

	@staticmethod
	def read(file_name='schools.csv'):
		full_file_name = CsvReader.folder + file_name
		file_handle = open(CsvReader.folder + file_name, 'r')
		data = []

		reader = csv.DictReader(file_handle)
		for row in reader:
			school = {}
			for prop in CsvReader.properties:
				school[prop] = row[prop]

			data.append(school)

		file_handle.close()

		return data