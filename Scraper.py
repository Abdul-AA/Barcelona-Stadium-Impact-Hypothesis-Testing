import nest_asyncio
nest_asyncio.apply()

import asyncio
import aiohttp
from understat import Understat


async def get_barcelona_home_games(season):
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        matches = await understat.get_team_results("Barcelona", season)

        # Filtering home games
        home_games = [match for match in matches if match['h']['title'] == 'Barcelona']

        # Extracting only relevant data and add stadium info
        data = []
        for game in home_games:
            match_date = datetime.strptime(game['datetime'], '%Y-%m-%d %H:%M:%S')
            if match_date < datetime(2023, 6, 4):
                stadium = 'Camp Nou'
            else:
                stadium = 'Montjuic'
            data.append({
                'date': game['datetime'],
                'home_team': game['h']['title'],
                'away_team': game['a']['title'],
                'xG_home': game['xG']['h'],
                'xG_away': game['xG']['a'],
                'goals_for': game['goals']['h'],
                'goals_against': game['goals']['a'],
                'result': game['result'],
                'stadium': stadium
            })

        return data

async def main():
    seasons = [2022, 2023]
    all_data = []

    for season in seasons:
        try:
            data = await get_barcelona_home_games(season)
            all_data.extend(data)
        except Exception as e:
            print(f"Error fetching data for season {season}: {e}")

    df = pd.DataFrame(all_data)
    df.to_csv('barcelona_home_games.csv', index=False)
    print("Data saved to barcelona_home_games.csv")

# Run the main function
asyncio.run(main())
