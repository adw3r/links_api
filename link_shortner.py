import logging
from random import choice

import aiohttp
import httpx
import requests

from config import ZENNO_KEY, REFERRALS_API_HOST, REFERRALS_API_PORT, DOMAINS, URL


async def get_refs_from_api() -> dict:
    url = f'http://{REFERRALS_API_HOST}:{REFERRALS_API_PORT}/referals'
    response = None

    while response is None:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()


def _fix_link(link: str):
    link = link if 'http://' in link or 'https://' in link else f'https://{link}'
    return link


async def get_link_v2(utm_source: str, utm_campaign: str, utm_term: str):
    api_json = await get_refs_from_api()
    compaign = api_json.get(utm_campaign)
    link = compaign.get("link")
    project_link = f'{link}&utm_campaign={utm_campaign}&utm_source={utm_source}&utm_term={utm_term}'
    print(project_link)
    params = {'key': ZENNO_KEY, 'url': project_link, 'action': 'shurl', 'chat': '1'}
    url = f'http://{choice(DOMAINS)}/api.php'
    response = None

    while response is None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=params) as response:
                    text = await response.text()
        except Exception as err:
            logging.exception(err)
        else:
            return _fix_link(text)


async def get_link(utm_source: str, utm_campaign: str, utm_term: str) -> str:
    api_json = await get_refs_from_api()
    compaign = api_json.get(utm_campaign)
    link = compaign.get("link")

    project_link = f'{link}&utm_campaign={utm_campaign}&utm_source={utm_source}&utm_term={utm_term}'
    print(project_link)
    params = {'key': ZENNO_KEY, 'shurl': project_link}
    response = None

    while response is None:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(URL, params=params)
        except Exception as err:
            logging.exception(err)
    return _fix_link(response.text)
