import urllib2
import simplejson as json
import urls

#Get the player state for display
def fetchPlayerState():
    stateURL = urls.urls["state"]

    #Try to connect to acoustics instance.
    try:
        state = urllib2.urlopen(stateURL)
    except:
        return None
    statePyObj = json.loads(state.read())
    return statePyObj

#Perform a search query on Acoustics
def searchQuery(query_type, query):
    searchURL = urls.urls["search"] + ";field=" + query_type + ";value=" + query
    
    #Try to connect to acoustics instacne
    try:
        searchResults = urllib2.urlopen(searchURL)
        print searchResults.read()
    except:
        return None
    
    try:
        searchJson = json.loads(searchResults.read())
    except:
        return None

    return searchJson
    
