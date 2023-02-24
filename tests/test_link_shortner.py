from unittest import TestCase

import requests

from link_shortner import get_link_v2, get_refs_api_response, get_refs_from_api, get_link


class TestLinkShortner(TestCase):

    def test_get_referrals_api_response(self):
        response: requests.Response = get_refs_api_response()
        self.assertTrue(response.ok)

    def test_get_refs_from_api(self):
        answer: dict = get_refs_from_api()
        self.assertIsNotNone(answer)

    def test_get_link_v2(self):
        utm_source = 'turk'
        utm_campaign = 'AllRight'
        utm_term = 'testdonor'
        link = get_link_v2(utm_source=utm_source, utm_campaign=utm_campaign, utm_term=utm_term)
        resp = requests.get(link)
        self.assertTrue(utm_campaign in resp.text)

    def test_get_link(self):
        utm_source = 'turk'
        utm_campaign = 'AllRight'
        utm_term = 'testdonor'
        link = get_link(utm_source=utm_source, utm_campaign=utm_campaign, utm_term=utm_term)
        resp = requests.get(link)
        self.assertTrue(utm_campaign in resp.text)
