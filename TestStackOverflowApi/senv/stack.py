import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://stackoverflow.com/questions')

soup = BeautifulSoup(res.text, 'html.parser')

ques_data = {
    'questions':[]
}

question = soup.select('.question-summary')
# id = 0

for ques in question:
    # id += 1
    
    q = ques.select_one('.question-hyperlink').getText()
    vote_count = ques.select_one('.vote-count-post').getText()
    views = ques.select_one('.views').attrs['title']
    tags = [i.getText() for i in (ques.select('.post-tag'))]
    ques_data['questions'].append({
        # 'id':id,
        'question':q,
        'views': views,
        'vote-count': vote_count,
        'tags': tags
    })

json_data = json.dumps(ques_data, sort_keys=True, indent=4)
print(json_data)

