import translator
import time
import os
import sys

def convertMicroSecondToTime(microSecond):
    '''
    将毫秒转换为字幕时间
    '''
    mics = microSecond % 1000
    if 10 <= mics < 100:
        mics = '0' + str(mics)
    elif 0 <= mics < 10:
        mics = '00' + str(mics)
    seconds = convertIntAndAddZero(microSecond // 1000 % 60)
    minutes = convertIntAndAddZero(microSecond / 1000 // 60 % 60)
    hours = convertIntAndAddZero(microSecond / 1000 / 60 // 60)
    return '{}:{}:{},{}'.format(hours, minutes, seconds, mics)

def convertIntAndAddZero(number):
    '''
    转整数以及补零
    '''
    number = int(number)
    if number < 10:
        number = '0' + str(number)
    return number

def GetCapFromFile(FileName):
    '''
    打开文件获取Captions字典列表
    '''
    with open(FileName, 'r', encoding='utf-8') as f:
        captions = eval(f.read().replace('false','False').replace('true', 'True'))['captions']
    return captions

def ParseAndMerge(captions, translate=False):
    '''
    传入字幕字典列表合成srt字符串
    '''
    srtStrList = []
    resultList = []
    # 取出所有字幕为列表方便单独处理
    captionsStrList = list(map(lambda x:x['content'].replace('\n', ' '), captions))
    
    def translateList(captionsStrList):
        '''
        翻译给定的英文字符串列表，并把翻译结果插入到列表元素的第一行
        由于get有字节的限制因此要将要翻译的东西分开。
        '''
        print('原文分段...')
        counter = 0
        partList = list()
        partList.append(list()) # 始终会有一部分
        for tmpStr in captionsStrList:
            counter += sys.getsizeof(tmpStr)
            if counter < 2000:
                if tmpStr != '':
                    partList[-1].append(tmpStr)
            else:
                partList.append(list())
                partList[-1].append(tmpStr)
                counter = 0

        print('开始翻译...')
        for i in range(len(partList)):
            resultList.extend(translator.translate('\n'.join(partList[i])))
            print(f'翻译第 {i+1} 部分，共{len(partList)}部分')
            time.sleep(1) # 接口限制，等待 1 s
        
        # 把翻译好的东西插入到原来的英文上面
        print(len(resultList), resultList)
        for index in range(len(captionsStrList)):
            captionsStrList[index] = resultList[index] + '\n' + captionsStrList[index]

    if translate:
        translateList(captionsStrList)

    for index in range(len(captions)):
        thisCaption = captions[index]
        srtStrList.append(str(index+1))
        srtStrList.append('{} --> {}'.format(
            convertMicroSecondToTime(thisCaption['startTime']),
            convertMicroSecondToTime(thisCaption['startTime'] + thisCaption['duration'])
            ))
        content = captionsStrList[index]
        srtStrList.append(content)
        srtStrList.append('')
    srtStr = '\n'.join(srtStrList)
    return srtStr

def GetNoSrtList(path):
    files = map(lambda x:path + '/' + x, os.listdir(path))
    NoSrtList = list()
    for filename in files:
        if filename.endswith('.json'):
            if not(os.path.exists(filename.replace('.json', '.srt'))) and 'translateApi' not in filename:
                # srt不存在
                print(filename + '\t[ \033[0;32m{}\033[0m ]'.format('Ready'))
                NoSrtList.append(filename)
            else:
                # srt已经存在
                print(filename + '\t[ \033[1;34m{}\033[0m ]'.format('OK'))
    return NoSrtList

def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def convent(FileName):
    '''
    将给定的json文件名转换成对应的srt文件保存在相同目录
    '''
    captions = GetCapFromFile(FileName)
    # 翻译决策部分
    print("字幕内容一瞥：" + captions[1]['content'])
    translate = is_contain_chinese(captions[1]['content'])
    if translate:
        print('判断为包含中文')
    else:
        print('判断为不包含中文')
    # 开始转换字幕
    print('-------------转换字幕开始-------------')
    srtStr = ParseAndMerge(captions, translate=not(translate))
    print('-------------转换字幕结束-------------')
    print("---------生成字幕内容一瞥开始----------")
    print(srtStr[:400])
    print("---------生成字幕内容一瞥结束----------")
    with open(FileName.replace('.json', '.srt'), 'w', encoding='utf-8') as f:
        f.write(srtStr)

def main():
    #path = os.getcwd()
    path = input('请输入json所在目录：')
    NoSrtList = GetNoSrtList(path)
    print('-----------------------华丽的分割线-----------------------------')
    if input('continue?(y/n):') == 'y':
        for FileName in NoSrtList:
            print('-----------------------正在转换{}-----------------------------'.format(FileName))
            convent(FileName)

if __name__ == '__main__':
    main()
