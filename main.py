from fetch import API
from load import DB
import transform
from pprint import pprint

api = API()
db = DB()


def work_static_data():
    # Data that should not change on a day-to-day basis
    STATIC_TABLES = {
        'division': transform.get_divisions(),
        'venue': transform.get_venues(),
        'conference': transform.get_conferences(),
        'franchise': transform.get_franchises(),
        'team': transform.get_teams()
    }

    for table in STATIC_TABLES.keys():
        STATIC_TABLES[table]

    pprint(STATIC_TABLES)

    # Loading data to db
    print("--------- INSERTS ---------")

    for table in STATIC_TABLES.keys():
        db.insert(STATIC_TABLES[table], table)


pprint(transform.get_schedule())
