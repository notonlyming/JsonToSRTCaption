fileName = input('请输入文件名（无拓展名）：')

with open(fileName+'.srt', 'r', encoding='utf-8') as f:
    srtLines = f.read().split('\n')

with open(fileName+'chi.txt', 'r', encoding='utf-8') as f:
    chiLines = f.read().split('\n')

contentCount = (len(srtLines) - 1) // 4
for index in range(contentCount):
    srtLines[index*4+2] = chiLines[index] + '\n' + srtLines[index*4+2]

finalStr = '\n'.join(srtLines)

print(finalStr)

if input('写入吗？(y/n)') == 'y':
    with open(fileName+'.srt', 'w', encoding='utf-8') as f:
        f.write(finalStr)