import requests
import time

url = "https://iam49.fandom.com/zh/wiki/%E5%91%A8%E6%A6%95%E6%9C%88?action=edit" #周榕月的wiki

headers = { # 伪装成浏览器
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"
}

response = requests.get(url, headers=headers)
time_start = time.time()
time.sleep(0.5)
time_end = time.time()

print('Time cost = %fs' % (time_end - time_start))



# print(response) #响应状态码
# print(response.reason) #相应状态描述
# print(response.encoding) #编码
text = response.text
with open("GET.txt", "w", encoding="utf-8")as f:
    f.write(text)
# print(response)

