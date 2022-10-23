# main.py
import convert
import SrtToJson
import traceback
import srt_translate

message = '''
-------------------------------------------------
字幕处理小程序 By Little Ming updated 2019.08.22
该版本目前在Github开源^_^ 
Github项目主页：https://github.com/notonlyming/JsonToSRTCaption
-------------------------------------------------
'''

if __name__ == "__main__":
    try:
        print(message)
        print('1.转换srt文件为json')
        print('2.转换json文件为srt并翻译(批量操作)')
        print('3.转换英文srt文件为中英srt(批量操作)')
        choise = input('请输入序号：')
        print('-----------------------')
        if choise == '1':
            SrtToJson.main()
        elif choise == '2':
            convert.main()
        elif choise == '3':
            srt_translate.main()
        else:
            print('没有匹配到正确的序号')
    except Exception as e:
        traceback.print_exc()
        input('程序发生了异常，请查看信息。（回车键退出）')
    finally:
        print("\033[1;34m{}\033[0m".format('\nHave a nice day, Bye. ^_^\n'))
        # print('Have a nice day, Bye. ^_^\n')
