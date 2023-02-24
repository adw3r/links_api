import logging
from random import choice

import requests

from config import ZENNO_KEY, REFERRALS_API_HOST, REFERRALS_API_PORT, DOMAINS, URL


def get_refs_api_response() -> requests.Response:
    response = None
    while response is None:
        try:
            response = requests.get(f'http://{REFERRALS_API_HOST}:{REFERRALS_API_PORT}/referals')
            return response
        except Exception as e:
            logging.exception(e)


def get_refs_from_api() -> dict:
    api_response = get_refs_api_response()
    json_response = api_response.json()
    return json_response


def _fix_link(link: str):
    link = link if 'http://' in link or 'https://' in link else f'https://{link}'
    return link


def get_link_v2(utm_source: str, utm_campaign: str, utm_term: str):
    api_json = get_refs_from_api()
    compaign = api_json.get(utm_campaign)
    link = compaign.get("link")

    project_link = f'{link}&utm_campaign={utm_campaign}&utm_source={utm_source}&utm_term={utm_term}'
    print(project_link)
    params = {'key': ZENNO_KEY, 'url': project_link, 'action': 'shurl', 'chat': '1'}
    url = f'http://{choice(DOMAINS)}/api.php'

    response = None
    while type(response) is not requests.Response:
        try:
            response = requests.post(url, data=params)
        except Exception as err:
            logging.exception(err)
        else:
            content = response.text
            return _fix_link(content)


def get_link(utm_source: str, utm_campaign: str, utm_term: str) -> str:
    api_json = get_refs_from_api()
    compaign = api_json.get(utm_campaign)
    link = compaign.get("link")

    project_link = f'{link}&utm_campaign={utm_campaign}&utm_source={utm_source}&utm_term={utm_term}'
    print(project_link)
    params = {'key': ZENNO_KEY, 'shurl': project_link}
    response = None

    while type(response) is not requests.Response:
        try:
            response = requests.get(URL, params=params)
        except Exception as err:
            logging.exception(err)
        else:
            content = response.text
            return _fix_link(content)
