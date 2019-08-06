import logging

logger = logging.getLogger(__name__)


class Transformer:

    @staticmethod
    def get_first_name(user):
        return user['name']['first']

    @staticmethod
    def get_last_name(user):
        return user['name']['last']

    @staticmethod
    def create_email(user):
        return Transformer.get_first_name(user) + '.' + Transformer.get_last_name(user) + '@mailinator.com'

    @staticmethod
    def create_user_profiles(users, school, role):
        user_profiles = []
        for u in users:
            logger.info('Creating profile for user: %s', u)
            profile = {
                'Name': Transformer.get_first_name(u).capitalize() + ' ' + Transformer.get_last_name(u).capitalize(),
                'Email': Transformer.create_email(u),
                'Password': 'Tams123',
                'School': school,
                'Role': role
            }
            user_profiles.append(profile)
            logger.info('Created profile: %s', profile)

        return user_profiles
