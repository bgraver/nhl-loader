import requests
import psycopg2
from pprint import PrettyPrinter

'''
Usage: 
- Getting data from other places
'''
class API:
    STATS_URL = 'https://statsapi.web.nhl.com/api/v1'

    # Querying an external api based on the table name
    def fetch(self, model, params={}, headers={}):
        try:
            r = requests.get('{0}/{1}'.format(self.STATS_URL, model), params=params, headers=headers)
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            return
        finally:
            return r.json()


