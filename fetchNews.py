from requests import Request, Session
import json
from datetime import datetime, timedelta

i = 1
session = Session()
public_url = 'https://cryptopanic.com/api/v1/posts/?auth_token=f8d35df861317a27f9e520363e61f2e083fea36e&public=true&filter=important'
# public_url = 'https://cryptopanic.com/api/v1/posts/?auth_token=f8d35df861317a27f9e520363e61f2e083fea36e&public=true&filter=hot'
# public_url = 'https://cryptopanic.com/api/v1/posts/?auth_token=f8d35df861317a27f9e520363e61f2e083fea36e&public=true'

public_response = session.get(public_url)
pubic_data = json.loads(public_response.text)["results"]

# columns = ["Title", "Published date", "url", ]

for public_new in pubic_data:
    ##TODO:create content
    content = []
    title = public_new["title"]
    publish_date = public_new["created_at"]
    url = public_new["url"]

    content.append(title)
    ##TODO:adjust datetime format
    publish_date = datetime.strptime(publish_date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=8)
    content.append(publish_date)
    content.append(url)

    print(f"{i}: {title}, {publish_date}")
    print(f"{url}\n")

    i += 1
