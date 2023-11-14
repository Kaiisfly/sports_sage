from bs4 import BeautifulSoup
import pandas as pd
from table_html import u10_coed, u12_boys, u14_boys
data_dict = {
    'u10_coed': u10_coed,
    'u12_boys': u12_boys,
    'u14_boys': u14_boys,
}


def extract_data(data_key):
    # Check if the key exists in the dictionary
    if data_key not in data_dict:
        print(f"No data found for key: {data_key}")
        return None

    # Get the data from the dictionary
    html_string = data_dict[data_key]

    # Create BeautifulSoup object
    soup = BeautifulSoup(html_string, 'html.parser')

    # Find the table in the soup
    table = soup.find('tbody')
    # Create lists to hold the extracted data
    rankings = []
    teams = []
    games_played = []
    wins = []
    losses = []
    points = []
    pct = []
    home_record = []
    away_record = []
    pf = []
    pa = []
    pm = []
    streak = []

    # Iterate over each row in the table
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        rankings.append(columns[0].text.strip())
        teams.append(columns[1].find('span', class_='standing_team_name').text.strip())
        games_played.append(columns[2].text.strip())
        wins.append(columns[3].text.strip())
        losses.append(columns[4].text.strip())
        points.append(columns[5].text.strip())
        pct.append(columns[6].text.strip())
        home_record.append(columns[7].text.strip())
        away_record.append(columns[8].text.strip())
        pf.append(columns[9].text.strip())
        pa.append(columns[10].text.strip())
        pm.append(columns[11].text.strip())
        streak.append(columns[13].text.strip())

    # Create a DataFrame from the extracted data
    df = pd.DataFrame({
        'Rank': rankings,
        'Team': teams,
        'Games Played': games_played,
        'Wins': wins,
        'Losses': losses,
        'Points': points,
        'Pct': pct,
        'Home Record': home_record,
        'Away Record': away_record,
        'Points Scored': pf,
        'Points Allowed': pa,
        'Plus Minus +/-': pm,
        'Streak': streak
    })

    return df


# Use the function with a key
'''
data_key = input("Enter data key: ")
df = extract_data(data_key)
if df is not None:
    print(df)
'''