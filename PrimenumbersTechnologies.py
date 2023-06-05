import requests
from bs4 import BeautifulSoup

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")


table = soup.find("table", {"id": "posting-table"})

rows = table.findAll("tr")[1:]

postings = []

for row in rows:
    columns = row.find_all("td")
    if len(columns) >= 3:
        est_value_notes = columns[0].text.strip()
        description = columns[1].text.strip()
        closing_date = columns[2].text.strip()

        posting = {
            "Est. Value Notes": est_value_notes,
            "Description": description,
            "Closing Date": closing_date,
        }

        postings.append(posting)

        if len(postings) == 5:
            break

for posting in postings:
    print(posting)
