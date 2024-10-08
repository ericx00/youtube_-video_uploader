import os
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# OAuth 2.0 scopes required for accessing YouTube Data API
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secrets.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)

def upload_video(youtube, video_file, title, description, tags):
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "22"  # Category 22 is 'People & Blogs'
        },
        "status": {
            "privacyStatus": "public",  # or 'unlisted' or 'private'
        },
    }

    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)

    response_upload = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    ).execute()

    print(f"Uploaded video with ID: {response_upload['id']}")

def upload_videos_in_folder(folder_path):
    youtube = authenticate_youtube()
    for video_file in os.listdir(folder_path):
        if video_file.endswith(".mp4"):  # Assuming videos are in .mp4 format
            full_path = os.path.join(folder_path, video_file)
            upload_video(
                youtube,
                full_path,
                title=video_file[:-4],  # Use the filename without extension as the title
                description="Uploaded by a Python script",  # You can modify the description
                tags=["short", "video", "upload"]  # Add relevant tags
            )

if __name__ == "__main__":
    folder_path = "path_to_your_folder_containing_videos"  # Replace with your folder path
    upload_videos_in_folder(folder_path)

