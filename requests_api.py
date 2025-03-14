import requests


class RequestsCollector:
    def __init__(self):
        self.url = 'http://26.241.32.104:5001/'

    def get_path(self):
        data = requests.get(self.url).json()
        return data


if __name__ == '__main__':
    rc = RequestsCollector()
    
    print(rc.get_path())