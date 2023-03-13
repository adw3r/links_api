import asyncio
from unittest import TestCase, IsolatedAsyncioTestCase

import aiohttp
import requests

import config


async def fetch_url(session, url, params):
    async with session.get(url, params=params) as resp:
        return await resp.text()


class TestEndpoint(IsolatedAsyncioTestCase):

    async def test_get_link(self):
        params = {
            'project_name': 'Admiral Shark',
            'targets_base': 'turk',
            'donor': 'testdonor'
        }
        url = f'http://localhost:{config.PORT}/link'
        resp = requests.get(url, params=params)
        print(url)
        self.assertTrue('bit.ly/' in resp.text)

    async def test_get_link_v2(self):
        self.skipTest('deprecated')
        params = {
            'project_name': 'Admiral Shark',
            'targets_base': 'turk',
            'donor': 'testdonor'
        }
        url = f'http://localhost:{config.PORT}/link_v2'
        resp = requests.get(url, params=params)
        self.assertTrue('https://' in resp.text)

    async def test_endpoint_on_high_load(self):
        params = {
            'project_name': 'Admiral Shark',
            'targets_base': 'turk',
            'donor': 'testdonor'
        }
        url = f'http://localhost:{config.PORT}/link'

        async with aiohttp.ClientSession() as session:
            cors = [asyncio.create_task(fetch_url(session, url, params)) for _ in range(50)]
            results = await asyncio.gather(*cors)
        print(results)
