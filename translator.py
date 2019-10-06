import urllib.request
import sys
import ssl

def translate(querystr, to_l="zh", from_l="auto"):
    ssl._create_default_https_context = ssl._create_unverified_context
    querystr = urllib.parse.quote(querystr)
    C_agent = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
    flag = 'class="t0">'
    tarurl = "https://translate.google.cn/m?hl={}&sl={}&q={}".format(
        to_l, from_l, querystr.replace(" ", "+"))
    request = urllib.request.Request(tarurl, headers=C_agent)
    page = str(urllib.request.urlopen(request).read().decode('utf-8'))
    target = page[page.find(flag) + len(flag):]
    target = target.split("<")[0]
    return urllib.parse.unquote(target).replace('&gt;', '>').replace('&lt;', '<')
