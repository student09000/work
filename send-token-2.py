import requests
import time

def send_request():
    url = "https://ably.com/users/password"
    headers = {
        "Host": "ably.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://ably.com/users/password/new",
        "X-Csrf-Token": "F4Uofav-BSVfhtefdP8ZSJONPjqPwf2ujWCykOV9-ccCpF8GCZ_x7N8dyhgKWTTfREPYwjOWeCzJ9VLYyzv7EA",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://ably.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=1",
        "Te": "trailers"
    }
    data = {
        "utf8": "%e2%9c%93",
        "user[email]": "t8591905@gmail.com",
        "commit": "Continue"
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

if __name__ == "__main__":
    while True:
        send_request()
        time.sleep(30)  # Sleep for 30 seconds
