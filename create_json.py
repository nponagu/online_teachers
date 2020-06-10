import json
from pprint import pprint

from data import goals, teachers


with open("mock_db.json", "w", encoding="utf-8") as f:
    json.dump([goals, teachers], f, ensure_ascii=False)


goals_from_file = json.load(open('mock_db.json', 'r'))
pprint(goals_from_file)