import gspread
from oauth2client.service_account import ServiceAccountCredentials

myscope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
mycred = ServiceAccountCredentials.from_json_keyfile_name('creds.json',myscope)

client =gspread.authorize(mycred)
mysheet = client.open("Google sheet API bot").sheet1

def user_data(user_name):
    try:
        row = mysheet.find(user_name).address[1:]
        row_values = mysheet.get_values(f"{row}:{row}")[0]
        date = mysheet.get("1:1")[0][1:]
    except: return 0
    arr = []
    for k in date:
        arr.append(f'{k, row_values[1:][date.index(k)]}')

    return arr
def get_user_avarage_a(user_name):
    try:
        row = mysheet.find(user_name).address[1:]
        row_values = mysheet.get_values(f"{row}:{row}")[0][1:]
    except: return 0
    f = 0
    t = 0
    for i in row_values:
        if i == "FALSE":
            f+=1
        else: t+=1
    return t/(t+f)*100


def all_user_name():
    return mysheet.get("A:A")[1:]






