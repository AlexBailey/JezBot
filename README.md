# JezBot
A Tinder bot that mimics Jeremy from Peep Show - it will like everyone in your set radius and send them quotes from the messages.py file.

Find your Facebook ID here: https://findmyfbid.com/

Find your Facebook Auth Token for Tinder by going to this [page.](https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&state=%7B%22challenge%22%3A%22q1WMwhvSfbWHvd8xz5PT6lk6eoA%253D%22%2C%220_auth_logger_id%22%3A%2254783C22-558A-4E54-A1EE-BB9E357CC11F%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=54783C22-558A-4E54-A1EE-BB9E357CC11F#_=) Before clicking "OK" open Chrome Developer Tools (for Mac: CMD + Option + i) and click on the "Network" tab. Make sure to filter by XHR requests. Then click on "OK" to authorize Tinder in the Facebook dialog. Then search for "access_token="

Uses [Pynder](https://github.com/charliewolf/pynder) to talk to Tinder.

Super serious project.
