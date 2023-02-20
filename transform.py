from fetch import API
from load import DB
from pprint import pprint
import json

api = API()

"""
Order:
- Call fetch to pull data
- Make any transformation calls in between
- Call load to load the db up with transformed data
"""

def get_divisions():
    data = api.fetch('divisions')['divisions']
    ret = []
    for row in data:
        ret.append({
            "id": row['id'],
            "name": row['name'],
            'name_short': row['nameShort'],
            'link': row['link'],
            'abbreviation': row['abbreviation']
        })
    return ret

def get_venues():
    data = api.fetch('venues')['venues']
    ret = []
    for row in data:
        ret.append({
            "id": row['id'],
            "name": row['name'],
            'link': row['link'],
        })
    return ret

def get_conferences():
    data = api.fetch('conferences')['conferences']
    ret = []
    for row in data:
        ret.append({
            "id": row['id'],
            "name": row['name'],
            'link': row['link'],
        })
    return ret

def get_franchises():
    data = api.fetch('franchises')['franchises']
    ret = []
    for row in data:
        ret.append({
            "id": row['franchiseId'],
            "team_name": row['teamName'],
            "location_name": row['locationName'],
            'link': row['link'],
            'first_season_id': row['firstSeasonId'],
            'most_recent_team_id': row['mostRecentTeamId']
        })
    return ret

def get_teams():
    data = api.fetch('teams')['teams']
    ret = []
    for row in data:
        ret.append({
            "id": row['id'],
            "name": row['name'],
            'link': row['link'],
            'abbreviation': row['abbreviation'],
            'team_name': row["teamName"],
            'official_site_url': row['officialSiteUrl'],
            'active': row['active'],
            'location_name': row["locationName"],
            'short_name': row['shortName'],
            'first_year_of_play': row["firstYearOfPlay"],
            'conference_id': row["conference"]["id"],
            'division_id': row["division"]["id"],
            "franchise_id": row["franchise"]["franchiseId"]
        })
    return ret

def get_schedule():
    data = api.fetch('schedule', params={'startDate': '2022-07-26', 'endDate': '2023-07-25'})
    dates = data['dates']
    ret = []

    for days in dates:
        date = days['date']
        for game in days['games']:
            ret.append({
                'id': game['gamePk'],
                'date': date,
                'game_type': game['gameType'],
                'season': game['season'],
                'game_date': game['gameDate'],
                'status': game['status']['detailedState'],
                'home_team_id': game['teams']['home']['team']['id'],
                'away_team_id': game['teams']['away']['team']['id']
            })

    return ret

def get_events(game_id):
    data = api.fetch('game/{0}/feed/live'.format(game_id))
    events = data['liveData']['plays']['allPlays']
    ret = []

    for event in events:
        keys = event.keys()
        d = {"game_id": game_id}

        if 'result' in keys:
            d.update({
                'result_event': event['result']['event'],
                'result_event_code': event['result']['eventCode'],
                'result_event_type_id': event['result']['eventTypeId'],
                'result_event_description': event['result']['description']
            })
        else:
            d.update({
                'result_event': None,
                'result_event_code': None,
                'result_event_type_id': None,
                'result_event_description': None
            })

        if 'about' in keys:
            d.update({
                "about_event_id": event["about"]["eventIdx"],
                "about_period": event["about"]["eventId"],
                "about_period_type": event["about"]["periodType"],
                "about_ordinal_num": event["about"]["period"],
                "about_period_time": event["about"]["periodTime"],
                "about_period_time_remaining": event["about"]["periodTimeRemaining"],
                "about_date_time": event["about"]["dateTime"],
                "about_goals_home": event["about"]["goals"]["away"],
                "about_goals_away": event["about"]["goals"]["home"]
            })
        else:
            d.update({
                "about_event_id": None,
                "about_period": None,
                "about_period_type": None,
                "about_ordinal_num": None,
                "about_period_time": None,
                "about_period_time_remaining": None,
                "about_date_time": None,
                "about_goals_home": None,
                "about_goals_away": None
            })

        if 'players' in keys:
            d.update({
                "players": json.dumps(event["players"])
            })
        else:
            d.update({
                "players": None
            })

        if 'coordinates' in keys:
            if 'x' in event["coordinates"]:
                d.update({
                    "coordinate_x": event["coordinates"]["x"],
                    "coordinate_y": event["coordinates"]["y"]
                })
            else:
                d.update({
                    "coordinate_x": None,
                    "coordinate_y": None
                })
        else:
            d.update({
                "coordinate_x": None,
                "coordinate_y": None
            })

        if 'team' in keys:
            d.update({
                "team_id": event["team"]["id"]
            })
        else:
            d.update({
                "team_id": None
            })

        ret.append(d)

    return ret

