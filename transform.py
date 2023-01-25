from fetch import API
from load import DB
from pprint import pprint

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



