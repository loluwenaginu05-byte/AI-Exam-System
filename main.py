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

#根据学号查找学生信息
    def find_student(self, target_id):
        if not self.validate_student_id(target_id):
            print("输入错误：学号必须为数字。")
            return

        found = False
        for student in self.students:
            if student.student_id == target_id:
                print("找到学生信息：")
                print(student)
                found = True
                break
        
        if not found:
            print(f"未找到学号为 {target_id} 的学生。")
#随机点名系统
    def random_roll_call(self, count_str):
        try:
            count = int(count_str)
            if count <= 0:
                print("输入错误：点名人数必须大于0。")
                return
            if count > len(self.students):
                print(f"输入错误：当前只有 {len(self.students)} 名学生，无法点名 {count} 人。")
                return
            
            # 随机抽取不重复的学生
            selected_students = random.sample(self.students, count)
            print(f"\n--- 随机点名结果 ({count}人) ---")
            for i, s in enumerate(selected_students, 1):
                print(f"{i}. {s.name} ({s.student_id})")

        except ValueError:
            print("输入错误：请输入有效的整数数字。")
#生成考场安排表
    def generate_seating_chart(self):
        if not self.students:
            print("没有学生数据，无法生成考场表。")
            return

        # 复制一份列表并打乱，避免影响原始数据
        shuffled_students = self.students[:]
        random.shuffle(shuffled_students)
        
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        filename = "考场安排表.txt"
        #创建考场安排表.txt文件，将考场安排信息写入
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"生成时间：{current_time}\n")
                f.write("-" * 30 + "\n")
                f.write(f"{'座位号':<10}{'姓名':<10}{'学号':<15}\n")
                f.write("-" * 30 + "\n")
                
                for index, student in enumerate(shuffled_students, 1):
                    f.write(f"{index:<10}{student.name:<10}{student.student_id:<15}\n")
            
            print(f"成功生成考场安排表：{filename}")
            return shuffled_students # 返回打乱后的列表供生成准考证使用

        except Exception as e:
            print(f"生成考场安排表失败：{e}")
            return None

#生成准考证文件
    def generate_admission_tickets(self, seated_students):
        if not seated_students:
            print("没有座位数据，无法生成准考证。")
            return

        folder_name = "准考证"
        
        # 创建文件夹，如果已存在则不报错
        try:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            
            for index, student in enumerate(seated_students, 1):
                # 文件名格式：01.txt, 02.txt ...
                file_name = f"{index:02d}.txt"
                file_path = os.path.join(folder_name, file_name)
                
                content = (
                    f"=== 准考证 ===\n"
                    f"座位号：{index}\n"
                    f"姓名：{student.name}\n"
                    f"学号：{student.student_id}\n"
                    f"班级：{student.class_name}\n"
                    f"学院：{student.college}\n"
                )
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            print(f"成功在 '{folder_name}' 文件夹中生成 {len(seated_students)} 张准考证。")

        except Exception as e:
            print(f"生成准考证失败：{e}")

def main():
     data_file = "人工智能编程语言学生名单.txt"
     system = ExamSystem(data_file)
#按照需求选择1-5
     while True:
        print("\n=== 学生信息与考场管理系统 ===")
        print("1. 查询学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证")
        print("5. 退出")

        choice = input("请选择功能 (1-5): ")

        if choice == '1':
            sid = input("请输入要查询的学号: ")
            system.find_student(sid)
        elif choice == '2':
            num = input("请输入需要点名的学生数量: ")
            system.random_roll_call(num)
        elif choice == '3':
            system.generate_seating_chart()
        elif choice == '4':
            print("提示：生成准考证需要先有考场安排。正在临时生成座位数据...")
            seated = system.generate_seating_chart()
            if seated:
                system.generate_admission_tickets(seated)
        elif choice == '5':
            print("退出系统。")
            break
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()