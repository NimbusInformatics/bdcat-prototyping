import requests
from bs4 import BeautifulSoup
import pandas as pd


# URL for the Gen3 data model page
gen3_url = "https://gen3.biodatacatalyst.nhlbi.nih.gov/DD"

# Fetching the content of the Gen3 data model page
response = requests.get(gen3_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting entities
categories = soup.find_all('h2')
entities = []

for category in categories:
    print(category)
    category_name = category.text.strip()
    table = category.find_next('table')
    if table:
        print(table)
        entity_list = table.find_all('tr')[1:]  # Skipping the header row
        for entity in entity_list:
            entity_name = entity.find('td').text.strip()
            description = entity.find_all('td')[1].text.strip()
            entities.append((entity_name, category_name, description))

# Creating a DataFrame for the entities
gen3_entities_df = pd.DataFrame(entities, columns=['Entity', 'Category', 'Description'])

print(gen3_entities_df)
