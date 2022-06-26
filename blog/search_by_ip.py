import requests


def search_by_ip(ip: str='88.147.153.170') -> str:
    try:
        response = requests.get(url=f'https://ip-api.com/json/{ip}').json()
        print(response)
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')



