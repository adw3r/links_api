from unittest import IsolatedAsyncioTestCase

import httpx
import requests

from link_shortner import get_link_v2, get_refs_from_api, get_link


class TestLinkShortner(IsolatedAsyncioTestCase):

    async def test_get_refs_from_api(self):
        answer: dict = await get_refs_from_api()
        print(answer)
        self.assertIsNotNone(answer)

    async def test_get_link_v2(self):
        self.skipTest('Deprecated')
        utm_source = 'turk'
        utm_campaign = 'Admiral Shark'
        utm_term = 'testdonor'
        link = await get_link_v2(utm_source=utm_source, utm_campaign=utm_campaign, utm_term=utm_term)
        resp = requests.get(link)
        self.assertTrue(resp.status_code < 400)

    async def test_get_link(self):
        utm_source = 'turk'
        utm_campaign = 'Admiral Shark'
        utm_term = 'testdonor'
        link = await get_link(utm_source=utm_source, utm_campaign=utm_campaign, utm_term=utm_term)
        resp = httpx.get(link)
        self.assertTrue(resp.status_code < 400)
