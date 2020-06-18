from twilio.rest import Client
from bs4 import BeautifulSoup
import requests
import time

#use whatsapp number used by twilio bot
from_whatsapp_number = 'whatsapp:'
#whatsapp number where news to be received
to_whatsapp_number = 'whatsapp:'

#account sid and token on twilio dashboard
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)
#page link from news headlines to be scraped
page_link = ''
history = []
while True:
    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")
    recent_stories = list(map(lambda x: x.text, soup.findAll('div', attrs={"class":"eachStory"})))[:3]
    for story in recent_stories:
        if story not in history:
            client.messages.create(body=story, from_=from_whatsapp_number, to=to_whatsapp_number)
            history.append(story)
    if len(history) > 100:
        history = history[:10]
    time.sleep(100)