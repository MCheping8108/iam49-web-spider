import requests
import time
import os

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"
}

url = "https://iam49.fandom.com/zh/wiki/Annina?action=edit"

response = requests.get(url, headers=headers)
time_start = time.time()
time.sleep(0.5)
time_end = time.time()
print('Time cost = %fs' % (time_end - time_start))

text = response.text
with open("GET.txt", "w", encoding="utf-8")as f:
    f.write(text)

os.system("pause")