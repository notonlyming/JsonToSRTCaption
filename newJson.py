import os

def newJson(path):
    '''
    为没有json的mp4文件生成对应的json
    '''
    files = map(lambda x:path + '/' + x, os.listdir(path))
    for filename in files:
        if filename.endswith('.mp4') and not(os.path.exists(filename.replace('.mp4', '.json'))):
            print(filename)
            open(filename.replace('.mp4', '.json'), 'w', encoding='utf-8').close()

if __name__ == '__main__':
    #path = os.getcwd()
    path = input('请输入json所在目录：')
    newJson(path)