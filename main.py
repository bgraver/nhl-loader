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

    # Loading data to db
    print("--------- INSERTS ---------")

    for table in STATIC_TABLES.keys():
        db.insert(STATIC_TABLES[table], table)

def load_games():
    schedule = transform.get_schedule()

    for game in schedule:
        db.insert([game], 'games')

def load_game_events(game_id):
    events = transform.get_events(game_id)
    db.insert(events, 'event')
    return


# load_game_events(2022010001)


