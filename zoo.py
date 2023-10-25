"""
设计一个简单的动物园系统，其中包含不同类型的动物（如狗、猫和鸟）。每个动物都有自己的属性（如名字、年龄）和行为（如发出声音）。使用封装、继承和多态来完成。
"""
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass


# 定义 Dog 子类
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} 发出汪汪叫声！")


# 定义 Cat 子类
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} 发出喵喵叫声！")


# 定义 Bird 子类
class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} 发出鸟叫声！")


# 创建动物对象并调用方法
dog = Dog("狗狗", 3)
cat = Cat("猫咪", 2)
bird = Bird("小鸟", 1)

dog.make_sound()
cat.make_sound()
bird.make_sound()