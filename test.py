import csv
import json

# 讀取 CSV 檔案並轉換成 JSON 格式
def csv_to_json(csv_file_path, json_file_path):
    data = []
    
    # 讀取 CSV 檔案
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        # 將每一行轉換成字典並添加到列表中
        for row in csvreader:
            data.append(row)
    
    # 將字典列表轉換成 JSON 格式並寫入文件
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

# 指定 CSV 檔案路徑和輸出 JSON 檔案路徑
csv_file_path = 'aqx_p_432.csv'
json_file_path = 'aqx_p_432.json'

# 執行轉換
csv_to_json(csv_file_path, json_file_path)