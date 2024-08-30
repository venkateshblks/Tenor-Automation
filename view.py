# This code only sends one view
# 
import requests
import json

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "tenor.googleapis.com",
    "Origin": "https://tenor.com",
    "Referer": "https://tenor.com/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",

}

url = "https://tenor.googleapis.com/v2/registerevent"
params = {
    "appversion": "browser-r20240829-1",
    "prettyPrint": "false",
    "key": "AIzaSyC-P6_qz3FzCoXGLk6tgitZo4jEJ5mLzD8",
    "client_key": "tenor_web",
    "locale": "en",
    "anon_id": "AAYg45bu7SgHxOKP1BxLkw",
    "eventname": "itemview_impression",
    "component": "web_mobile",
    "current_uri": "https://tenor.com/view/persist-ventures-persist-ventures-venkatesh-gif-8449110717979128293",
    "data": '{"rid":"8449110717979128293","apirefid":"fa6fb6bb-b9fe-4183-af50-02f0c4676206","isUserLoggedIn":""}'
}

response = requests.post(url, headers=headers, params=params)

print("Response: ",response.text)
print("Status_code: ",response.status_code)