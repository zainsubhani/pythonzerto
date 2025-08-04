import requests
from bs4 import BeautifulSoup

# Fetch the page
res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

# Select title lines and score lines
links = soup.select('.titleline')
subtext = soup.select('.subtext')  # needed to find scores correctly

def get_titles_links_scores(links, subtext):
    results = []
    for idx, item in enumerate(links):
        a_tag = item.find('a')
        title = a_tag.getText()
        href = a_tag['href']

        # Get score if available
        score_tag = subtext[idx].select_one('.score')
        score = int(score_tag.getText().replace(' points', '')) if score_tag else 0
        

        results.append({'title': title, 'link': href, 'score': score})
    return results

# Display results
titles_and_links = get_titles_links_scores(links, subtext)
for i, item in enumerate(titles_and_links, 1):
    print(f"{i}. {item['title']} → {item['link']} → {item['score']}")
