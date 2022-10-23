# srt_translator.py

import SrtToJson
import convert

def main():
    import os
    base_path = input('文件夹路径：')
    files_list = os.listdir(base_path)
    srt_files = filter(lambda x: x.endswith('.srt'), files_list)
    json_files = tuple(filter(lambda x: x.endswith('.json'), files_list))
    srt_files_no_translate = tuple(filter(lambda x: (x[:-4]+'.json') not in json_files, srt_files))
    if input("continue(y/n):") == 'y':
        # 转换没有转换成json的文件
        for srt_file in srt_files_no_translate:
            Path = SrtToJson.main(base_path + '/' + srt_file[:-4])
            print('正在转换: {}'.format(srt_file))
        # 换json为srt，会自动判断是否已翻译
        for json_file in json_files:
            print(f'翻译{json_file}')
            path = base_path + '/' + json_file
            with open(f'{base_path}/{json_file[:-5] + ".srt"}', 'r', encoding='utf-8') as f:
                if convert.is_contain_chinese(f.read()):
                    print("包含中文，跳过……")
                else:
                    convert.convert(path)
