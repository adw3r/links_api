from unittest import TestCase

import requests

from link_shortner import get_link_v2, get_refs_api_response, get_refs_from_api


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
        link = get_link_v2(utm_source=utm_source, utm_campaign=utm_campaign)
        resp = requests.get(link)
        self.assertTrue(utm_campaign in resp.text)
