class LogFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_error_lines(self):
        try:
            error_lines = []  # Danh sách các dòng chứa lỗi
            with open(self.file_path, 'r') as file:
                for line in file:
                    if 'ERROR' in line:
                        error_lines.append(line.strip())  # Thêm dòng chứa lỗi vào danh sách
            return error_lines
        except FileNotFoundError:
            print("Không tìm thấy tệp nhật ký.")
        except IOError:
            print("Có lỗi khi đọc tệp nhật ký.")

    def read_line(self, line_number):
        try:
            with open(self.file_path, 'r') as file:
                for i, line in enumerate(file):
                    if i + 1 == line_number:
                        return line.strip()
                return None
        except FileNotFoundError:
            print("Không tìm thấy tệp nhật ký.")
        except IOError:
            print("Có lỗi khi đọc tệp nhật ký.")

if __name__ == "__main__":
    a = False
    line_last = None  # Khai báo biến line_last
    while True:
        if a == False or line_last != line:
            path_name_file = 'DateBase_0_DATE_2024-03-18.log'
            log_handler = LogFileHandler(path_name_file)
            
            # Lấy danh sách các dòng chứa lỗi và in ra
            error_lines = log_handler.get_error_lines()
            for line in error_lines:
                print(line)
                line_last = line
                a = True
