import logging

logger = logging.getLogger(__name__)


class Transformer:

    @staticmethod
    def get_first_name(user):
        if type(user) is str:
            first_name = user.split(' ')[0]
        else:
            first_name = user['name']['first']

        return first_name.capitalize()

    @staticmethod
    def get_last_name(user):
        if type(user) is str:
            last_name = user.split(' ')[1]
        else:
            last_name = user['name']['last']

        return last_name.capitalize()

    @staticmethod
    def create_email(user):
        return Transformer.get_first_name(user).lower() + \
               '.' + \
               Transformer.get_last_name(user).lower() + \
               '@mailinator.com'

    @staticmethod
    def create_user_profile(user, school, role):
        return {
            'Name': Transformer.get_first_name(user) + ' ' + Transformer.get_last_name(user),
            'Email': Transformer.create_email(user),
            'Password': 'Tams123',
            'School': school['Name'],
            'Role': role
        }
