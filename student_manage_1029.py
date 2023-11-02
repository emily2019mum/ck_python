"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""


'''
作业：
实现学生管理系统：

学生信息包含：
    - 编号（sid), 姓名（name), 年龄（age), 性别（gender) 四个信息
    - 每个学生信息使用字典形式保存
    - 使用列表保存所有学生的信息 

1. 实现菜单函数，输出下列信息，返回用户输入的编号，并进行输入校验。

    print("****************************************")
    print("*				学生管理系统			 *")
    print("*  	    1. 添加新学生信息              *")
    print("* 	    2. 通过学号修改学生信息		 *")
    print("*		3. 通过学号删除学生信息		 *")
    print("*		4. 通过姓名删除学生信息		 *")
    print("* 	    5. 通过学号查询学生信息          *")
    print("*		6. 通过姓名查询学生信息          *")
    print("*		7. 显示所有学生信息             *")
    print("*		8. 退出系统			  		 *")
    print("****************************************")
    select_op = input("输入编号选择操作：")

2. 实现控制函数，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
3. 实现添加学生函数，函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
4. 实现修改函数，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
5. 实现删除函数，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
6. 实现删除函数，参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
7. 实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
8. 实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
9. 实现函数，输出所有学生信息
'''

# 学生信息字典列表
students = []

# 菜单函数
def display_menu():
    print("*" * 40)
    print("*             学生管理系统             *")
    print("*   1. 添加新学生信息                *")
    print("*   2. 通过学号修改学生信息          *")
    print("*   3. 通过学号删除学生信息          *")
    print("*   4. 通过姓名删除学生信息          *")
    print("*   5. 通过学号查询学生信息          *")
    print("*   6. 通过姓名查询学生信息          *")
    print("*   7. 显示所有学生信息             *")
    print("*   8. 退出系统                     *")
    print("*" * 40)
    select_op = input("输入编号选择操作：")
    return select_op

# 1.添加学生函数
def add_student(sid, name, age, gender):
    for student in students:
        if student['sid'] == sid:
            return False  # 学号重复，添加失败
    new_student = {'sid': sid, 'name': name, 'age': age, 'gender': gender}
    students.append(new_student)
    return True  # 添加成功

# 2.修改学生信息（通过学号）
def modify_student(sid, name, age, gender):
    for student in students:
        if student['sid'] == sid:
            student['name'] = name
            student['age'] = age
            student['gender'] = gender
            return True  # 修改成功
    return False  # 学号不存在，修改失败

# 3.通过学号删除学生信息
def delete_student_by_sid(sid):
    removed_students = [student for student in students if student['sid'] == sid]
    if len(removed_students) > 0:
        students[:] = [student for student in students if student['sid'] != sid]
        return True  # 删除成功
    return False  # 学号不存在，删除失败

# 4.通过姓名删除学生信息
def delete_students_by_name(name):
    removed_students = [student for student in students if student['name'] == name]
    if len(removed_students) > 0:
        students[:] = [student for student in students if student['name'] != name]
        return True  # 删除成功
    return False  # 姓名不存在，删除失败

# 5.通过学号查询学生信息
def find_student_by_sid(sid):
    for student in students:
        if student['sid'] == sid:
            return student
    return None  # 学号不存在

# 6.通过姓名查询学生信息
def find_students_by_name(name):
    found_students = [student for student in students if student['name'] == name]
    if len(found_students) > 0:
        return found_students
    return None  # 姓名不存在

# 7.显示所有学生信息
def display_students():
    for student in students:
        print("学号: {}, 姓名: {}, 年龄: {}, 性别: {}".format(student['sid'], student['name'], student['age'], student['gender']))

# 主控制函数
def main():
    while True:
        choice = display_menu()

        if choice == '1':
            sid = input("请输入学号: ")
            name = input("请输入姓名: ")
            age = input("请输入年龄: ")
            gender = input("请输入性别: ")
            success = add_student(sid, name, age, gender)
            if success:
                print("添加成功！")
            else:
                print("学号重复，添加失败！")

        elif choice == '2':
            sid = input("请输入要修改的学号: ")
            name = input("请输入新姓名: ")
            age = input("请输入新年龄: ")
            gender = input("请输入新性别: ")
            success = modify_student(sid, name, age, gender)
            if success:
                print("修改成功！")
            else:
                print("学号不存在，修改失败！")

        elif choice == '3':
            sid = input("请输入要删除的学号: ")
            success = delete_student_by_sid(sid)
            if success:
                print("删除成功！")
            else:
                print("学号不存在，删除失败！")

        elif choice == '4':
            name = input("请输入要删除的学生姓名: ")
            success = delete_students_by_name(name)
            if success:
                print("删除成功！")
            else:
                print("姓名不存在，删除失败！")

        elif choice == '5':
            sid = input("请输入要查询的学号: ")
            student = find_student_by_sid(sid)
            if student:
                print("学号: {}, 姓名: {}, 年龄: {}, 性别: {}".format(student['sid'], student['name'], student['age'], student['gender']))
            else:
                print("学号不存在！")

        elif choice == '6':
            name = input("请输入要查询的学生姓名: ")
            found_students = find_students_by_name(name)
            if found_students:
                print("查询到以下同名学生：")
                for student in found_students:
                    print("学号: {}, 姓名: {}, 年龄: {}, 性别: {}".format(student['sid'], student['name'], student['age'], student['gender']))
            else:
                print("姓名不存在！")

        elif choice == '7':
            display_students()

        elif choice == '8':
            print("退出系统。")
            break

        else:
            print("无效选择，请重新输入。")

if __name__ == '__main__':
    main()
