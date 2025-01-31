import requests
from sources import get_sources

url = 'https://newsapi.org/v2/everything'

def fetch_articles(source_id, query, max_articles=500):
    """
    Fetches articles from a given source and query, up to the max_articles limit.
    """
    parameters = {
        'apiKey': '2253f518b3f0406f83e65b3394e1c028',
        'sources': source_id,
        'q': query,
        'pageSize': 100, 
        'language': 'en'
    }

    articles = []
    count = 1

    while len(articles) < max_articles:
        parameters['page'] = count
        result = requests.get(url, params=parameters)
        response_json = result.json()

        if result.status_code != 200 or 'articles' not in response_json:
            print(f"Error fetching from source {source_id}: {response_json.get('message', 'Unknown error')}")
            break

        page_articles = response_json.get('articles', [])
        articles.extend(page_articles)

    
        if len(page_articles) < parameters['pageSize']:
            break

        count += 1

    return articles[:max_articles]

if __name__ == '__main__':
    sources = get_sources()

    all_articles = []
    query = "Trump"

    for source in sources:
        source_id = source['id']
        print(f"Fetching articles from source: {source_id}")
        articles = fetch_articles(source_id, query)
        all_articles.extend(articles)
        print(f"Fetched {len(articles)} articles from {source_id}")

        if len(all_articles) >= 500:
            break

    output_filename = "all_trump_articles.txt"

    with open(output_filename, 'w') as file:
        for article in all_articles:
            title = article.get('title')
            description = article.get('description')
            #url = article.get('url')
            file.write(f"Title: {title}\nDescription: {description}\n")

    print(f"Total articles fetched: {len(all_articles)}")
    print(f"All articles saved to {output_filename}")
