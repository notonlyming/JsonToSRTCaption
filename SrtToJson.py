# SrtToJson.py

def convertTimeStrToMicroseconds(TimeStr):
    hours,minutes,seconds,microseconds = tuple(map(int, [TimeStr[:2],TimeStr[3:5],TimeStr[6:8],TimeStr[9:]]))
    minutes += hours*60
    seconds += minutes*60
    microseconds += seconds*1000
    return microseconds

def getStartTimeAndDuration(srtTimeStr):
    startTimeStr, endTimeStr = srtTimeStr.split(' --> ')
    startTime = convertTimeStrToMicroseconds(startTimeStr)
    endTime = convertTimeStrToMicroseconds(endTimeStr)
    return startTime, endTime-startTime

def convent(fileName):
    '''
    fileName是Srt文件名（不含拓展名）。
    返回json字符串
    '''
    with open(fileName+'.srt', 'r', encoding='utf-8') as f:
        srtLines = f.read().split('\n')

    jsonDict = {"captions":[]}
    # 取出第一行出来看看是从第几开始
    initialLineIndex = int(srtLines[0])
    for index in range(len(srtLines) // 4):
        #thisIndex是指真正的行索引，index则是指第几个字幕的索引
        thisIndex = index * 4
        if(srtLines[thisIndex] == str(index + initialLineIndex)):
            startTime, duration = getStartTimeAndDuration(srtLines[thisIndex+1])
            if srtLines[thisIndex+2][-1:] in [',', '.']:
                srtLines[thisIndex+2] = srtLines[thisIndex+2][:-1]
            jsonDict['captions'].append({'content':srtLines[thisIndex+2], 'startTime':startTime, 'duration':duration})
        else:
            print('字幕文件跳行读取失败')
            print('第{}行为{}，期望值{}'.format(thisIndex, srtLines[thisIndex], index+1))
            raise IOError
    return str(jsonDict)

def main(fileName=None):
    '''
    从用户读入文件路径，转换成srt写出。
    并返回新的json路径
    '''
    if fileName == None:
        fileName = input('请输入Srt文件名（不含拓展名）：')
    jsonStr = convent(fileName)
    with open(fileName+'.json', 'w', encoding='utf-8') as f:
        f.write(jsonStr)
    return fileName+'.json'

if __name__ == '__main__':
    main()
