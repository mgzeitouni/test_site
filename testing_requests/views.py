# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse
# import requests
# import json

# SANDBOX_URL = 'https://api.stubhubsandbox.com'
# PROD_URL = 'https://api.stubhub.com'

# USERNAME = 'mgzeitouni@gmail.com'
# PASSWORD = 'morris12'
# BASIC_AUTH_SAND = 'ZjRjSlptUGZ0VExSQklLdDdtaHJiYU5pOW9ZYTpCZnVfbDVyTzZUSklscU9Cbl9MSlpJeXk5Sklh'
# APP_TOKEN_SAND = '6u6p394ZmCk75NfNPUZ0gHR74dMa'
# BASIC_AUTH_PROD = 'QWNSQUNfZjdXenYzQjRZaG1wakpUazFPYjBjYTplSzVxSll0bVYwb2diRDdRRHFtMGhIUENfQ2th'
# APP_TOKEN_PROD = 'sllPgZnDi98izhNL63NMp5oTTTka'

# #Specify keys to use - Sandbox or Prod
# BASIC_AUTH = BASIC_AUTH_PROD
# APP_TOKEN = APP_TOKEN_PROD
# URL = PROD_URL
# cache = {}

# def req(full_url, headers, params, req_type='GET', use_cache=True):
#     cache_key = str(full_url) + str(headers) + str(params) + str(req_type)
#     if use_cache and (cache_key in cache):
#         return cache[cache_key]
#     #print "Request:", full_url, headers, params, req_type
#     response = None
#     if req_type == 'GET':
#         response = requests.get(full_url, headers=headers, params=params)
#     elif req_type == 'POST':
#         response = requests.post(full_url, headers=headers, params=params)
#     elif req_type == 'PUT':
#         #import pdb; pdb.set_trace()
#         response = requests.put(full_url, headers=headers, data=json.dumps(params))
#     elif req_type == 'DELETE':
#         response = requests.delete(full_url, headers=headers, params=params)
#     else:
#         return None
    
#     #print response
#    # import pdb; pdb.set_trace()
#     cache[cache_key] = response
#     return cache[cache_key]


# def login(basic_auth=BASIC_AUTH, username=USERNAME, password=PASSWORD, base_url=URL):
#     headers = {'Content-Type': 'application/x-www-form-urlencoded',
#                'Authorization': 'Basic %s' % (basic_auth),
#                }

#     params = {
#         'grant_type': 'password',
#         'username': username,
#         'password': password,
#         'scope': 'PRODUCTION'
#     }

#     return req(full_url='%s/login' % (base_url), headers=headers, params=params, req_type='POST')

# class Stubhub():
#     @staticmethod
#     def get_app_token(app_token=APP_TOKEN):
#         return app_token

#     @staticmethod
#     def get_user_token(basic_auth=BASIC_AUTH, username=USERNAME, password=PASSWORD, base_url=URL):
#         return login(basic_auth=basic_auth, username=username, password=password, base_url=base_url).json()[
#             'access_token']

#     @staticmethod
#     def get_user_id(basic_auth=BASIC_AUTH, username=USERNAME, password=PASSWORD, base_url=URL):
#         return login(basic_auth=basic_auth, username=username, password=password, base_url=base_url).headers[
#             'X-StubHub-User-GUID']

#     def __init__(self, app_token, user_token, user_id):
#         self.app_token = app_token
#         self.user_token = user_token
#         self.user_id = user_id

#     def send_req(self, url, token_type='USER', req_type='GET', headers=None, params=None, use_cache=False):
#         token = self.user_token if token_type == 'USER' else self.app_token
#         params = params or {}
#         headers = headers or {'Authorization': 'Bearer %s' % (token), 'Content-Type': 'application/json'}

#         full_url = '%s%s' % (URL, url)
#         # print full_url, params, headers

#         return req(full_url=full_url, headers=headers, params=params, req_type=req_type, use_cache=use_cache)

# 	def get_event_inventory(self, event_id, start=0, rows=10000, zonestats=True, sectionstats=True):
# 		params = {'eventId': event_id, 'start': start, 'rows': rows, 'zonestats' : zonestats, 'sectionstats' : sectionstats}
# 		return self.send_req('/search/inventory/v1', token_type='USER', req_type='GET', params=params).json()


# def index(request):

# 	username = USERNAME
# 	password = PASSWORD
# 	basic_auth = BASIC_AUTH
# 	app_token = APP_TOKEN

# 	app_token = Stubhub.get_app_token(app_token=app_token)
# 	user_token = Stubhub.get_user_token(basic_auth=basic_auth, username=username, password=password)
# 	user_id = Stubhub.get_user_id(basic_auth=basic_auth, username=username, password=password)
	  
# 	stubhub = Stubhub(app_token=app_token, user_token=user_token, user_id=user_id)
	
# 	#import pdb; pdb.set_trace()
# 	#print stubhub
# 	event_id = 9444003
	
# 	params = {'eventId': event_id, 'start': 0, 'rows': 500, 'zonestats' : True, 'sectionstats' : True}
	
# 	url = '/search/inventory/v1'

# 	headers = {'Authorization': 'Bearer %s' % (user_token), 'Content-Type': 'application/json'}
# 	full_url = '%s%s' % (URL, url)
# 	response = requests.get(full_url, headers=headers, params=params).json()
	


# 	return HttpResponse("User ID: %s \n Listings: %s" %(user_id, response))


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
