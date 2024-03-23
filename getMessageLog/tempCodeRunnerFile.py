import os
import time
import serial  # Import thư viện PySerial

class LogFileHandler:
    def __init__(self, directory):
        self.directory = directory
        self.previous_modification_times = {}  # Lưu trữ thời gian sửa đổi trước đó của mỗi tệp log

    def get_error_lines(self, file_path):
        try:
            error_keywords = ['ERROR', 'CHANGE', 'BEYOND LIMIT', 'REQUEST ACT RIGHT NOW']
            error_lines = []  # Danh sách các dòng chứa lỗi

            # Mở tệp nhật ký và kiểm tra từng dòng
            with open(file_path, 'r') as file:
                for line in file:
                    if any(keyword in line for keyword in error_keywords):
                        error_lines.append(line.strip())  # Thêm dòng chứa lỗi vào danh sách

            return error_lines  # Trả về danh sách các dòng chứa lỗi
        except FileNotFoundError:
            print("Không tìm thấy tệp nhật ký:", file_path)
            return []  # Trả về danh sách rỗng nếu không tìm thấy tệp
        except IOError:
            print("Có lỗi khi đọc tệp nhật ký:", file_path)
            return []  # Trả về danh sách rỗng nếu có lỗi khi đọc tệp

    def print_new_errors(self, serial_port):
        try:
            # Lấy danh sách tất cả các tệp nhật ký trong thư mục
            log_files = [f for f in os.listdir(self.directory) if f.endswith('.log')]

            for file_name in log_files:
                file_path = os.path.join(self.directory, file_name)

                # Kiểm tra thời gian sửa đổi của tệp log
                modification_time = os.path.getmtime(file_path)

                # Kiểm tra xem có sự thay đổi so với thời gian sửa đổi trước không
                if file_path not in self.previous_modification_times or modification_time != self.previous_modification_times[file_path]:
                    # Lấy danh sách các dòng chứa lỗi mới
                    new_error_lines = self.get_error_lines(file_path)

                    # In ra tên tệp nhật ký
                    serial_port.write((file_name + ">>\n").encode())

                    # In ra các dòng chứa lỗi mới
                    for line in new_error_lines:
                        serial_port.write((line + "\n").encode())
                    
                    # Cập nhật thời gian sửa đổi của tệp log
                    self.previous_modification_times[file_path] = modification_time
        except Exception as e:
            print("Có lỗi khi xử lý tệp nhật ký:", str(e))

if __name__ == "__main__":
    # Đường dẫn thư mục chứa tệp nhật ký
    directory = 'C:/ProgramData/CODESYS/CODESYSControlWinV3x64/19C83874/PlcLogic/'

    # Tạo một thể hiện của lớp LogFileHandler với đường dẫn thư mục tệp nhật ký
    log_handler = LogFileHandler(directory)

    # Mở cổng UART
    try:
        serial_port = serial.Serial('COM10', 115200)  # Thay 'COMx' bằng cổng UART thực tế của ESP32
        print("Kết nối UART thành công")
    except serial.SerialException:
        print("Không thể kết nối UART")

    while True:
        # In ra các dòng chứa lỗi mới và gửi chúng qua UART
        log_handler.print_new_errors(serial_port)
        time.sleep(1)  # Chờ 1 giây trước khi kiểm tra sự thay đổi trong tệp log
