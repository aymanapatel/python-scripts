import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from oauth2client import client # Added
from oauth2client import tools # Added
from oauth2client.file import Storage # Added

import json
from pandas import DataFrame, read_csv, ExcelWriter
import pandas as pd

scopes = ["https://www.googleapis.com/auth/youtube"]


# 1. Playlist
# 2. Videos
def get_authenticated_service_and_return_response(request_type, playlist_id):
# Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_desktop.json"

    # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #    client_secrets_file, scopes)
    # credentials = flow.run_console()

    store = Storage("token.json")    
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secrets_file, scopes)
        credentials = tools.run_flow(flow, store)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)


    
    if(request_type == 1):
        request = youtube.playlists().list(
            part="snippet",
            channelId="UC_ML5xP23TOWKUcc-oAE_Eg",
            maxResults="50"
        )

    elif(request_type == 2):
        request = youtube.playlists().list(
            part="snippet",
            id=playlist_id,
            maxResults="50"
        )

    else:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id, # playlistid
            maxResults="50"
        )        


    response = request.execute()

    return response

def get_videos_from_playlist(playlist_id):
    
    response = get_authenticated_service_and_return_response(3, playlist_id)
    playlist_name = get_authenticated_service_and_return_response(2, playlist_id)

    #print(playlist_name)
    items = playlist_name['items'][0]

    file_name = items['snippet']['localized']['title']
    file_name = file_name.replace(" ","")
    file_name = file_name.replace("/","_") # If there is / in string

    with open("./data/" + file_name +".json", 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False, indent=4)

    #print(file_name)
    return


def convert_videos_json_to_sheets(json_file, writer):
    print("==============convert_videos_json_to_sheets")    

    # 1. Load JSON from File

    with open('./data/' + json_file, encoding="utf8") as f:
        fileOpen = json.load(f)


    # print(fileOpen)    


    # 2. Get JSON Array to Python List


    itemsObj = fileOpen['items']

    titleArr=[]
    urlArr=[]
    urlOnlyArr=[]
    for item in itemsObj:
        
        # print("\n ---------------------New----\n",item['snippet']['title'])
        title = item['snippet']['title']
        # print("\n ---------------------Video ID----\n",item['snippet']['resourceId']['videoId'])
        urlOnly = item['snippet']['resourceId']['videoId']
        url = "https://www.youtube.com/watch?v=" + urlOnly
        #print("\n ---------------------Video URL----\n", url)

        # print("\n ---------------------Title----\n",item['snippet']['title'])
        if(title != 'Private video'):
            titleArr.append(title)
            urlArr.append(url)
            urlOnlyArr.append(urlOnly)
        
        




    # 3. Insert to pandas

    dataset = list(zip(titleArr, urlArr, urlOnlyArr))

    print(dataset)

    df = pd.DataFrame(data = dataset, columns=['Title', 'URL','URLOnly'])
    def make_hyperlink(value):
        url = "https://www.youtube.com/watch?v={}"
        return '=HYPERLINK("%s", "%s")' % (url.format(value), "Link")
    df['URLOnly'] = df['URLOnly'].apply(lambda x: make_hyperlink(x))    
    # print(df)



    # 4. Export to CSV
    print(json_file[:-5])

    
    df.to_excel(writer, sheet_name=json_file[:-5])


def main():

    response = get_authenticated_service_and_return_response(1, "random")
    with open("./data/!playlists.json", 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False, indent=4)
    # print(response)

    # 1. Load JSON from File

    with open('./data/' + '!playlists.json', encoding="utf8") as f:
        fileOpen = json.load(f)


    # print(fileOpen)    


    # 2. Get JSON Array to Python List


    itemsObj = fileOpen['items']
    for item in itemsObj:
        playlist_id = item['id']
        title = item['snippet']['title']
        # print(playlist_id, title)
        get_videos_from_playlist(playlist_id)



    writer = ExcelWriter("Test_Multisheet.xlsx", engine='openpyxl')
    for json_files in os.listdir("./data"):

        if not json_files.startswith("!"):
            # print(json_files)
            convert_videos_json_to_sheets(json_files, writer) 
        else:
         continue


    writer.save()

if __name__ == "__main__":
    main()