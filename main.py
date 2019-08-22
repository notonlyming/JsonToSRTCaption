# main.py
import convert
import SrtToJson

if __name__ == "__main__":
    print("-----------------------")
    print('1.转换srt文件为json')
    print('2.转换json文件为srt并翻译(批量操作)')
    print('3.转换英文srt文件为中英srt')
    choise = input('请输入序号：')
    print('-----------------------')
    if choise == '1':
        SrtToJson.main()
    elif choise == '2':
        convert.main()
    elif choise == '3':
        Path = SrtToJson.main()
        print('-----------------------正在转换{}-----------------------------'.format(Path))
        convert.convent(Path)
    else:
        print('没有匹配到正确的序号')

    print("\033[1;34m{}\033[0m".format('\nHave a nice day, Bye. ^_^'))