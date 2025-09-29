from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.yallakora.com/match-center?date=9/28/2025"
page = requests.get(url)
matches_data=[]
def main(page):
    src =  page.content
    soup = BeautifulSoup(src, "lxml")
    championships = soup.find_all("div" , {"class": "matchCard"})
    def get_match_info(championships):
        match_title = championships.contents[1].find("h2").text.strip()
        all_matches = championships.contents[3].find_all ("div" , {"class" : "liItem"})

        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            teamA = all_matches[i].find("div", {"class": "teamA"}).find("p").text.strip()
            teamB = all_matches[i].find("div", {"class": "teamB"}).find("p").text.strip()
            match_result = all_matches[i].find("div", {"class": "MResult"}).find_all("span")#.text.strip()
            score = f"{match_result[0].text.strip()} - {match_result[2].text.strip()}"
            match_time = all_matches[i].find("span", {"class": "time"}).text.strip()
            # Append row to list
            matches_data.append({
                "Championship": match_title,
                "Team A": teamA,
                "Team B": teamB,
                "Team B": teamB,
                "Score": score
            })


    for champ in range(len(championships)):
        get_match_info(championships[champ])

    df = pd.DataFrame(matches_data)
    return df
df_matches = main(page)
print(df_matches)