import requests
import json

# get north american news sources 


url = 'https://newsapi.org/v2/sources'

def get_sources():
    sources = []
    countries = ['us', 'ca', 'mx']

    for country in countries:
        parameters = {
            'apiKey' : "8b47adc8dce94cfdb68d8da779ffb5ca",
            'country' : country,
            'language' : 'en'
        }

        result = requests.get(url, params = parameters)
        json_result = result.json().get('sources')
        sources.extend(json_result)

    return sources 

if __name__ == "__main__":
    sources = get_sources()
    with open("sources_output.txt", "w") as file:
        file.write(f"Total Sources: {len(sources)}\n")
        for source in sources:
            file.write(f"ID: {source['id']}, Name: {source['name']}\n")