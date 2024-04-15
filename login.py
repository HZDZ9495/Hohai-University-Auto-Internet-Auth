import requests
import re
import urllib.parse

your_cookie = ''
your_user_id = ''
your_password = ''
your_service = ''

get_url = requests.get('http://123.123.123.123')
script_text = get_url.text
url_match = re.search(r"location.href='(.*?)'", script_text)
original_url = url_match.group(1)
encoded_url = urllib.parse.quote(original_url, safe='')

host="localhost:5000"
url=f"http://eportal.hhu.edu.cn/eportal/InterFace.do"
headers={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '985',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': your_cookie,
    'Host': 'eportal.hhu.edu.cn',
    'Origin': 'http://eportal.hhu.edu.cn',
    'Referer': original_url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}
params = {
    'method': 'login',
}
data = {
    'userId': your_user_id,
    'password': your_password,
    'service':your_service,
    'queryString': encoded_url,
    'operatorPwd': '',
    'operatorUserId': '',
    'validcode': '',
    'passwordEncrypt': 'true',
}
response=requests.post(url=url,headers=headers,params=params,data=data,allow_redirects=False)
print(response.status_code)
if response.status_code==200:
    print(response.text)
    print("Success")
else:
    print("Error")