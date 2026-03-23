import os
import random
import time

class Student:
    #创建数据类，用来储存学生的相关信息
    def __init__(self, serial_number, name, gender, class_name, student_id, college):#序号	姓名	性别	班级	学号	学院
        # 初始化学生属性
        self.serial_number=serial_number
        self.name = name
        self.gender = gender
        self.class_name = class_name
        self.student_id = student_id
        self.college = college

    def __str__(self):
        # 定义函数直接打印学生信息
        return f"学号{self.serial_number},姓名：{self.name}, 性别：{self.gender}, 班级：{self.class_name}, 学号：{self.student_id}, 学院：{self.college}"
        pass

class ExamSystem:
    #创建考场系统
    def __init__(self, data_file):#data_file=“.txt文件名”
        self.students = []
        self.data_file = data_file
        # 启动时自动加载数据
        self.load_data()

    @staticmethod
    def validate_student_id(student_id):
        return student_id.isdigit()

#从文本中读取学生信息
    def load_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            if len(lines) <= 1:
                print("警告：文件内容为空或仅有表头，无有效数据。")
                return

            lines = lines[1:]#防止读取数据时将表头当成学生信息

            for line in lines:
                parts = line.strip().split()#以空格分割
                if len(parts) >= 5:
                    # 文件格式为：序号 姓名 性别 班级 学号 学院
                    serial_number=parts[0]
                    name = parts[1]
                    gender = parts[2]
                    class_name = parts[3]
                    student_id = parts[4]
                    college = parts[5]
                    
                    student = Student(serial_number, name, gender, class_name, student_id, college)
                    self.students.append(student)
                else:
                    print(f"警告：跳过格式错误的行 -> {line.strip()}")#如果格式有问题就跳过
                    
            print(f"成功加载 {len(self.students)} 名学生信息。")

        except FileNotFoundError:
            print(f"错误：找不到文件 '{self.data_file}'，请确认文件路径是否正确。")
        except Exception as e:
            print(f"发生未知错误：{e}")
#读取学生信息
    def load_data(self):
        pass
#根据学号查找学生信息
    def find_student(self, target_id):
        pass
#随机点名系统
    def random_roll_call(self, count_str):
        pass
#生成考场安排表
    def generate_seating_chart(self):
        pass
#生成准考证文件
    def generate_admission_tickets(self, seated_students):
        pass
def main():
    pass

if __name__ == "__main__":
    pass