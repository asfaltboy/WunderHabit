import logging
import habitica as hlib

from . import default


logger = logging.getLogger('wunderhabit')


class HabiticaApi(hlib.api.Habitica):
    def __init__(self, user_id, api_token):
        headers = {default.AUTH_HEADER_CLIENT: user_id,
                   default.AUTH_HEADER_TOKEN: api_token}
        super(HabiticaApi, self).__init__(headers)

    def status(self):
        """
        Returns the Habitica server status.
        """

        return self.server()[default.JSON_STATUS] == default.JSON_UP

    def get_user(self):
        """
        Returns the full user object.
        """

        try:
            user = self.user()
        except Exception:
            logger.exception('Could not load Habitica user.')
            return None

        return user

    def get_user_details(self):
        """
        Parses the user details like the username or email from the Habitica user object.
        """

        user = self.get_user()
        if not user or default.JSON_AUTH not in user:
            return None

        auth_details = user[default.JSON_AUTH]
        user_details = dict()

        # Parse user id
        try:
            user_details[default.JSON_ID] = user[default.JSON_ID]
        except Exception:
            logger.exception('Could not find Habitica user id')

        # Parse user details
        if default.JSON_LOCAL in auth_details and auth_details[default.JSON_LOCAL]:
            # User is authenticated with Habitica account
            try:
                auth_local = auth_details[default.JSON_LOCAL]
                user_details[default.JSON_EMAIL] = auth_local[default.JSON_EMAIL]
                user_details[default.JSON_NAME] = auth_local[default.JSON_USERNAME]
            except Exception:
                logger.exception('Could not parse Habitica user with local auth.')

        elif default.JSON_FACEBOOK in auth_details:
            # User is authenticated with facebook
            try:
                auth_facebook = auth_details[default.JSON_FACEBOOK][default.JSON_FORMAT_JSON]
                user_details[default.JSON_EMAIL] = auth_facebook[default.JSON_EMAIL]
                user_details[default.JSON_NAME] = auth_facebook[default.JSON_NAME]
            except Exception:
                logger.exception('Could not parse Habitica user with Facebook auth.')

        else:
            # No valid authentication provider found
            logger.error('No valid Habitica auth provider found.')

        return user_details

    def post_task(self, task_id, up=True):
        """
        Up- or down-scores a task specified by the task_id.
        """

        if up:
            score = default.JSON_UP
        else:
            score = default.JSON_DOWN

        return self.user.tasks(_id=task_id, _direction=score, _method='post')

    def test_auth(self):
        """
        Tests whether the authentication credentials work or not.
        """

        user = self.get_user()
        if user:
            return True
        else:
            return False
