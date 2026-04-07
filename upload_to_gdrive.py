from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
import json

# Path to service account JSON
SERVICE_ACCOUNT_FILE = os.environ.get("GDRIVE_SERVICE_ACCOUNT_JSON", "service_account.json")

# Authenticate
gauth = GoogleAuth()
gauth.LoadClientConfigFile(SERVICE_ACCOUNT_FILE)  # correct method for service accounts
gauth.ServiceAuth()  # service account login
drive = GoogleDrive(gauth)

# File to upload
file_path = "spotify.png"
file_name_in_drive = "spotify.png"

# Upload file
file = drive.CreateFile({'title': file_name_in_drive})
file.SetContentFile(file_path)
file.Upload()

print(f"✅ Uploaded {file_name_in_drive} successfully!")
