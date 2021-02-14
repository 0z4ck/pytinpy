# coding=utf-8
import json

import requests


class TinderClient:
    headers = {
        "app_version": "6.9.4",
        "platform": "ios",
        "User-agent": "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)",
        "Accept": "application/json",
        "content-type": "application/json"
    }
    
    def __init__(self, authToken, host="https://api.gotinder.com"):
        self.headers['X-Auth-Token'] = authToken
        self.host = host


    def get_recommendations(self):
        '''
        Returns a list of users that you can swipe on
        '''
        try:
            r = requests.get('https://api.gotinder.com/user/recs', headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong with getting recomendations:", e)
    
    
    def get_updates(self, last_activity_date=""):
        '''
        Returns all updates since the given activity date.
        The last activity date is defaulted at the beginning of time.
        Format for last_activity_date: "2017-07-09T10:28:13.392Z"
        '''
        try:
            url = self.host + '/updates'
            r = requests.post(url,
                              headers=self.headers,
                              data=json.dumps({"last_activity_date": last_activity_date}))
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong with getting updates:", e)
    
    
    def get_self(self):
        '''
        Returns your own profile data
        '''
        try:
            url = self.host + '/profile'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your data:", e)
    
    
    def change_preferences(self, **kwargs):
        '''
        ex: change_preferences(age_filter_min=30, gender=0)
        kwargs: a dictionary - whose keys become separate keyword arguments and the values become values of these arguments
        age_filter_min: 18..46
        age_filter_max: 22..55
        age_filter_min <= age_filter_max - 4
        gender: 0 == seeking males, 1 == seeking females
        distance_filter: 1..100
        discoverable: true | false
        {"photo_optimizer_enabled":false}
        '''
        try:
            url = self.host + '/profile'
            r = requests.post(url, headers=self.headers, data=json.dumps(kwargs))
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not change your preferences:", e)
    
    
    def get_meta(self):
        '''
        Returns meta data on yourself. Including the following keys:
        ['globals', 'client_resources', 'versions', 'purchases',
        'status', 'groups', 'products', 'rating', 'tutorials',
        'travel', 'notifications', 'user']
        '''
        try:
            url = self.host + '/meta'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your metadata:", e)
    
    def get_meta_v2(self):
        '''
        Returns meta data on yourself from V2 API. Including the following keys:
        ['account', 'client_resources', 'plus_screen', 'boost',
        'fast_match', 'top_picks', 'paywall', 'merchandising', 'places',
        'typing_indicator', 'profile', 'recs']
        '''
        try:
            url = self.host + '/v2/meta'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your metadata:", e)
    
    def update_location(self, lat, lon):
        '''
        Updates your location to the given float inputs
        Note: Requires a passport / Tinder Plus
        '''
        try:
            url = self.host + '/passport/user/travel'
            r = requests.post(url, headers=self.headers, data=json.dumps({"lat": lat, "lon": lon}))
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not update your location:", e)
    
    def reset_real_location(self):
        try:
            url = self.host + '/passport/user/reset'
            r = requests.post(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not update your location:", e)
    
    
    def get_recs_v2(self):
        '''
        This works more consistently then the normal get_recommendations becuase it seeems to check new location
        '''
        try:
            url = self.host + '/v2/recs/core?locale=en-US'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            print('excepted')
    
    def set_webprofileusername(self, username):
        '''
        Sets the username for the webprofile: https://www.gotinder.com/@YOURUSERNAME
        '''
        try:
            url = self.host + '/profile/username'
            r = requests.put(url, headers=self.headers,
                             data=json.dumps({"username": username}))
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not set webprofile username:", e)
    
    def reset_webprofileusername(self, username):
        '''
        Resets the username for the webprofile
        '''
        try:
            url = self.host + '/profile/username'
            r = requests.delete(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not delete webprofile username:", e)
    
    def get_person(self, id):
        '''
        Gets a user's profile via their id
        '''
        try:
            url = self.host + '/user/%s' % id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get that person:", e)
    
    
    def send_msg(self, match_id, msg):
        try:
            url = self.host + '/user/matches/%s' % match_id
            r = requests.post(url, headers=self.headers,
                              data=json.dumps({"message": msg}))
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not send your message:", e)
    
    def unmatch(self, match_id):
        try:
            url = self.host + '/user/matches/%s' % match_id
            r = requests.delete(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not unmatch person:", e)
    
    def superlike(self, person_id):
        try:
            url = self.host + '/like/%s/super' % person_id
            r = requests.post(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not superlike:", e)
    
    
    def like(self, person_id):
        try:
            url = self.host + '/like/%s' % person_id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not like:", e)
    
    
    def dislike(self, person_id):
        try:
            url = self.host + '/pass/%s' % person_id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not dislike:", e)
    
    
    def report(self, person_id, cause, explanation=''):
        '''
        There are three options for cause:
            0 : Other and requires an explanation
            1 : Feels like spam and no explanation
            4 : Inappropriate Photos and no explanation
        '''
        try:
            url = self.host + '/report/%s' % person_id
            r = requests.post(url, headers=self.headers, data={
                              "cause": cause, "text": explanation})
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not report:", e)
    
    
    def match_info(self, match_id):
        try:
            url = self.host + '/matches/%s' % match_id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your match info:", e)
    
    def all_matches(self):
        try:
            url = self.host + '/v2/matches'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your match info:", e)
    
    def fast_match_info(self):
      try:
          url = self.host + '/v2/fast-match/preview'
          r = requests.get(url, headers=self.headers)
          count = r.headers['fast-match-count']
          # image is in the response but its in hex..
          return count
      except requests.exceptions.RequestException as e:
          print("Something went wrong. Could not get your fast-match count:", e)

    def get_teasers(self):
      try:
          url = self.host + '/v2/fast-match/teasers'
          r = requests.get(url, headers=self.headers)
          return r.json()
      except requests.exceptions.RequestException as e:
          print("Something went wrong. Could not get your teasers:", e)
    
    def trending_gifs(self, limit=3):
      try:
          url = self.host + '/giphy/trending?limit=%s' % limit
          r = requests.get(url, headers=self.headers)
          return r.json()
      except requests.exceptions.RequestException as e:
          print("Something went wrong. Could not get the trending gifs:", e)
    
    def gif_query(self, query, limit=3):
      try:
          url = self.host + '/giphy/search?limit=%s&query=%s' % (limit, query)
          r = requests.get(url, headers=self.headers)
          return r.json()
      except requests.exceptions.RequestException as e:
          print("Something went wrong. Could not get your gifs:", e)
    

