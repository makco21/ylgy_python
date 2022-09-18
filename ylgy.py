from ast import For
import json
from os import getcwd
from re import I
import ssl
from wsgiref import headers

import requests
import locale
from requests.packages.urllib3.exceptions import InsecureRequestWarning


if __name__ == '__main__':
    token=input("输入token：")
    j=int(input("输入次数："))
    ###### go 代码 ：
    # SetBaseURL("https://cat-match.easygame2021.com").
	# SetHeader("Host", "cat-match.easygame2021.com").
	# SetHeader("Content-Type", "application/json").
	# SetHeader("Accept-Encoding", "gzip,compress,br,deflate").
	# SetHeader("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.28(0x18001c25) NetType/WIFI Language/zh_CN")
    # SetHeader("Referer", "https://servicewechat.com/wx141bfb9b73c970a9/15/page-frame.html").
	# SetHeader("t", token).
    	# SetQueryParam("rank_score", "1").
		# SetQueryParam("rank_state", "1").
		# SetQueryParam("rank_time", strconv.FormatInt(consumeTime, 10)).
		# SetQueryParam("rank_role", "1").
		# SetQueryParam("skin", "1").
		
    headers = {"Host": "cat-match.easygame2021.com",
               "Content-Type": "application/json",
               "Accept-Encoding":"gzip,compress,br,deflate",
               "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.28(0x18001c25) NetType/WIFI Language/zh_CN",
               "Referer": "https://servicewechat.com/wx141bfb9b73c970a9/15/page-frame.html",
               "t": token 
    }
    url = 'https://cat-match.easygame2021.com/sheep/v1/game/game_over?'+'rank_score=1&rank_state=1&rank_time=1&rank_role=1&skin=1'


    # context = ssl.create_default_context()
    # context.load_verify_locations(cafile=getcwd()+"/isrgrootx1.pem")


    requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
    # 禁用安全请求警告
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    s = requests.session()
    s.keep_alive = False # 关闭多余连接

    # print(certifi.where())
    i=1
    while(i<=j):
        res = s.get(url,headers=headers,verify=False)
        i=i+1
        print(res)
    # res = json.loads(res.text)


    
