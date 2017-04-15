import pynder
import config
import time
import datetime
import requests
from messages import messages

requests.packages.urllib3.disable_warnings()

session = pynder.Session(config.FACEBOOK_ID, config.FACEBOOK_AUTH_TOKEN)


def log(msg):
    print '[' + str(datetime.datetime.now()) + ']' + ' ' + msg

#This is just the send function that Jez uses to send messages
#to his matches with a delay of 3 seconds between conservative
#messages, just to be a bit more realistic. Will also print out
#the sent message and to who Jez sent it to.
def send(match, message_no):
    for m in messages[message_no]:
        session._api._post('/user/matches/' + match['id'],
                           {"message": m})
        time.sleep(3)
    log('Sent message ' + str(message_no) + ' to ' + match['person']['name'])

#Jez will message all matches that he has not spoken to and
#every 10 minutes Jez will check for a reply, if they have
#not replied, then Jez will ignore them until they do.
def message(match):
    ms = match['messages']
    jeremy = session.profile.id
    if not ms:
        send(match, 0)
        return
    said = False
    count = 0
    name = match['person']['name']
    for m in ms:
        if m['from'] == jeremy:
            count += 1
            said = False
    if count >= len(messages):
        log('Jez stopped talking to ' + name)
        return
    if said:
        send(match, count)
    else:
        log('Jez has no new messages from ' + name)

#Jez isn't shy and he will try and match with literally anyone.
#He will like everyone near by in the set radius.
#If we see user 'Tinder Team', that'll be Jez out of swipes! and
#will try again in 10 minutes, otherwise will keep liking people.
def handle_likes():
    while True:
        try:
            users = session.nearby_users()
            for u in users:
                if u.name == 'Tinder Team':
                    log('Jez is out of Swipes. Thanks a bunch, Elgar!')
                    return
                u.like()
                log('Jez liked ' + u.name)
        except ValueError:
            continue
        except pynder.errors.RequestError:
            continue

#Anyone that Jez matches he will now message. This is handled
#by the message function using this function as the parameter
def handle_matches():
    log(str(len(session._api.matches())) + ' matches')
    matches = session._api.matches()
    for m in matches:
        message(m)

#Every 5 minutes, Jez will check if he has anymore available swipes.
#If he does, he will like everyone. If he doesn't, he's either out of
#likes or out of avilable potentials within the set radius.
while True:
    handle_likes()
    handle_matches()
    log('Pausing for ten minutes...')
    time.sleep(300)
