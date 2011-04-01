import urllib2
import sys

#json
if sys.version_info < (2, 6):
	import simplejson as json
else:
	import json

import settings


def fetchPlayerState():

    stateURL = settings.URLS["state"]

    #Try to connect to acoustics instance.
    try:
        state = urllib2.urlopen(stateURL)
    except URLError:
        return None
    statePyObj = json.loads(state.read())
    return statePyObj

def searchQuery(query_type, query):

    searchURL = settings.URLS["search"] + ";field=" + query_type + ";value=" + query
    
    #Try to connect to acoustics instance.
    try:
        searchResults = urllib2.urlopen(searchURL)
    except URLError:
        return None

    searchJson = json.loads(searchResults.read())
    return searchJson

