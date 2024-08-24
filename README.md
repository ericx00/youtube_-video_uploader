# youtube_-video_uploader
a script that will help creators automate uploading of their content with specified pre requisites

#Explanation:


![TangledExplainGIF](https://github.com/user-attachments/assets/3d823642-62a7-49da-a8ec-7acc52df54a4)












    Authenticate the user: The authenticate_youtube function handles OAuth 2.0 authentication and returns an authorized YouTube service object.
    Upload a video: The upload_video function uploads a single video file to YouTube, with a title and description.
    Upload all videos in a folder: The upload_videos_in_folder function iterates through all .mp4 files in the given folder and uploads each to YouTube.

#Notes:

![SpongebobPatrickGIF](https://github.com/user-attachments/assets/4679e44d-bd73-4c89-b473-cedb45f938fd)













    Replace "path_to_your_folder_containing_videos" with the actual path to your folder.
    Modify the title, description, and tags to fit your needs.
    Ensure your client_secrets.json file is in the same directory as the script.

#Important:

![RememberFacebookliveGIF](https://github.com/user-attachments/assets/791c4d80-77be-4b97-b01c-8113709ef374)











Using this script in production requires adherence to YouTube's API terms and Google's privacy policy.
Frequent uploads or attempts to automate could lead to throttling or API ban.
