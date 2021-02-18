import time
import requests
import json
import hashlib
import traceback

def baidu_get_url_encoded_params(query_text, lang_from, lang_to):
    """按api调用要求拼接url
    Args:
        query_text: 待翻译的文本
    Returns:
        符合调用接口要求的参数dict
    """
    tmpDict = json.load(open('translateApi.json', 'r', encoding='utf-8'))
    app_id = tmpDict['app_id']
    app_secret = tmpDict['app_secret']
    salt = str(round(time.time() * 1000))
    sign_raw = app_id + query_text + salt + app_secret
    sign = hashlib.md5(sign_raw.encode('utf8')).hexdigest()
    params = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'q': query_text,
        'from': lang_from,
        'to': lang_to,
        'appid': app_id,
        'salt': salt,
        'sign': sign
    }
    return params

def translate(querystr, to_l="zh", from_l="auto"):
    # 发送的请求头
    header = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}

    # get 请求的参数(未来可能发生变动)
    params = baidu_get_url_encoded_params(querystr, 'auto', 'zh')
    
    base_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    # 发送请求，出错重试机制
    for i in range(3):
        retry = False
        try:
            response = requests.post(base_url, headers=header, data=params)
            # 检查返回状态码
            if not response.status_code == 200:
                raise Exception(f'error res code:{response.status_code}')

            resJson = json.loads(response.text) # 解析返回的文本
            resList = [i['dst'] for i in resJson['trans_result']]
            print(resList) # 调试输出返回的json

            # 检查是否需要重试
            if not retry:
                break
        except:
            traceback.print_stack()
            print(f'\n出错啦，重试剩余：{3-i}')
            time.sleep(1.5) # 延迟1.5s
            retry = True

    return resList