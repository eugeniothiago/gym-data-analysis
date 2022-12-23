import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
load_dotenv()


def extract_data() -> list:
    SCOPES = [os.environ.get('SCOPE')]
    SERVICE_ACCOUNT_FILE = os.environ.get('KEYS_PATH')
    SHEET_ID = os.environ.get('SHEET_ID')
    SHEET_RANGE = os.environ.get('SHEET_RANGE')

    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    try:
        service = build('sheets', 'v4', credentials=credentials)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SHEET_ID,
                                    range=SHEET_RANGE).execute()
        values = result.get('values', [])
        return values
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    extract_data()