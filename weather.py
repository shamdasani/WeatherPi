import time, datetime, json
import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials

DHT_TYPE = Adafruit_DHT.AM2302
DHT_PIN = 4

GDOCS_OAUTH_JSON = 'WeatherPi.json'
GDOCS_SPREADSHEET_NAME = 'WeatherPi'

def login_open_sheet(oauth_key_file, spreadsheet):
    try:
        scope =  ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)


def WeatherPi():
    worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M")

    humidity, temperature = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    temperature = temperature * 9/5.0 + 32

    if humidity is not None and temperature is not None:
        try:
            worksheet.append_row((now, temperature, humidity))
        except:
            print('Append error')

WeatherPi()
