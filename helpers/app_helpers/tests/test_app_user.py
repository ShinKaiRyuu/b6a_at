import unittest
import logging
from nose.tools import assert_true
from helpers.app_helpers import create_user, create_blocked_user, delete_user
from helpers import data_helpers as data


class UserTest(unittest.TestCase):
    def _get_user_data(self):
        user_data = data.create_user_data()
        user_data['username'] = 'delete.me.{}'.format(user_data['username'])[:25]
        return user_data

    def _create_user(self, blocked=False):
        user_data = self._get_user_data()
        self.logger.info('user_data: {}'.format(user_data))
        create_func = create_user if not blocked else create_blocked_user
        user_info = create_func(user_data)
        self.logger.info('user_info: {}'.format(user_info))
        assert_true(user_info)
        self.users_ids.append(user_info.get('id'))
        return user_info

    def setUp(self):
        self.users_ids = []
        self.logger = logging.getLogger(self._testMethodName)

    def test_create_user(self):
        self._create_user()

    def test_create_blocked_user(self):
        self._create_user(blocked=True)

    def test_delete_user(self):
        user_info = self._create_user()
        delete_user(user_info.get('id'))

    def tearDown(self):
        if self.users_ids:
            for _id in self.users_ids:
                delete_user(_id)
