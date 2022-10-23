# srt_translator.py

import SrtToJson
import convert

def main():
    import os
    base_path = input('文件夹路径：')
    files_list = os.listdir(base_path)
    srt_files = filter(lambda x: x.endswith('.srt'), files_list)
    json_files = tuple(filter(lambda x: x.endswith('.json'), files_list))
    if input("continue(y/n):") == 'y':
        # 遍历所有srt文件
        for srt_file in srt_files:
            print(f'翻译{srt_file}')
            # 判断是否需要翻译
            with open(f'{base_path}/{srt_file}', 'r', encoding='utf-8') as f:
                if convert.is_contain_chinese(f.read()):
                    print("包含中文，跳过……")
                    continue

            # 需要翻译，转换成json的文件
            print('{}转换为json'.format(srt_file))
            path_json = SrtToJson.main(base_path + '/' + srt_file[:-4])
            convert.convert(path_json)
            print('清理临时json……')
            os.remove(path_json)
