import os
import time

# Đường dẫn đến file .log
log_file_path = "C:/ProgramData/CODESYS/CODESYSControlWinV3x64/19C83874/PlcLogic/DateBaseTPK_0_DATE_2024-03-19.log"

# Các từ khóa để kiểm tra
keywords = ['ERROR', 'CHANGE', 'BEYOND LIMIT', 'REQUEST ACT RIGHT NOW']

def check_log_for_keywords():
    try:
        with open(log_file_path, 'r') as file:
            # Đọc từng dòng trong file
            for line in file:
                # Kiểm tra xem dòng có chứa từ khóa không
                if any(keyword in line for keyword in keywords):
                    print(line.strip())
    except FileNotFoundError:
        print("Không tìm thấy file .log")

# Kiểm tra liên tục
while True:
    check_log_for_keywords()
    # Dừng 1 giây trước khi kiểm tra lại
    time.sleep(0.5)
