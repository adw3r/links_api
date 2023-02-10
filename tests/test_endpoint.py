from unittest import TestCase

import requests

import config


class TestEndpoint(TestCase):

    def test_get_link(self):
        self.skipTest('deprecated')
        params = {
            'project_name': 'AllRight',
            'targets_base': 'turk',
        }
        url = f'http://localhost:{config.PORT}/link'
        resp = requests.get(url, params=params)
        self.assertTrue('bit.ly/' in resp.text)

    def test_get_link_v2(self):
        params = {
            'project_name': 'AllRight',
            'targets_base': 'turk',
        }
        url = f'http://localhost:{config.PORT}/link_v2'
        resp = requests.get(url, params=params)
        self.assertTrue('https://' in resp.text)
