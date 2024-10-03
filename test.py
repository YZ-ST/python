import subprocess
from configs import *

class Tron:
    def __init__(self, module_name, urls):
        self.module_name = module_name
        self.urls = urls

    def run_command(self):
        # 執行第一個 API 請求
        # stdout=subprocess.PIPE: 將子進程輸出導向到 PIPE
        # stderr=subprocess.PIPE: 將子進程錯誤導向到 PIPE
        # text=True: 確保子進程的輸出是以文本格式處理，而不是以字節流處理
        process = subprocess.Popen(['curl', self.urls[0]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # 獲取子進程的輸出和錯誤
        output, error = process.communicate()
        
        if process.returncode != 0:
            print(f"{self.module_name} API 1st URL failed, error")
        else:
            print(f"{self.module_name} API 1st URL Response")
            # 若失敗，嘗試執行第二個 API
            process = subprocess.Popen(['curl', self.urls[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            output, error = process.communicate()
        
            if process.returncode != 0:
                print(f"{self.module_name} API 2nd URL also failed, error")
            else:
                print(f"{self.module_name} 2nd URL Response ")


if __name__ == '__main__':
    # 建立 Tron 物件
    for key, value in MODULE.items():
        tron = Tron(key, value)
        tron.run_command()
