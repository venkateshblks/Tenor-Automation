# This code sends unlimited views based on the variable "total" in the code.
# 
# This code only sends one share
# 
import requests
url = "https://tenor.googleapis.com/v2/registershare"
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

params = {
    "appversion": "browser-r20240829-1",
    "prettyPrint": "false",
    "key": "AIzaSyC-P6_qz3FzCoXGLk6tgitZo4jEJ5mLzD8",
    "client_key": "tenor_web",
    "locale": "en",
    "anon_id": "AAYg45bu7SgHxOKP1BxLkw",
    "id": "8449110717979128293",
    "component": "web_mobile",
    "apirefid": "f70ab27a-3553-4a91-b354-53abc7eab2c4",

}

response = requests.post(url, headers=headers, params=params)

print("Response: ",response.text)
print("Status_code: ",response.status_code)

i = 1
total = 201  
while i <= total:
    try:
        response = requests.post(url, headers=headers, params=params)
        if response.status_code == 200:
            print(f"{i} shares sent")
        else:
            print(f"Non-200 status code {response.status_code} at iteration {i}")
    except Exception as e:
        print(f"Error at iteration {i}: {e}")
    finally:
        i += 1
