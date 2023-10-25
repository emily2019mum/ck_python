"""
编写一个Python程序，创建一个几何图形计算程序，使用静态方法来计算矩形的面积和周长。
"""

class Geometry:
    @staticmethod
    def rectangle_area(width, height):
        return width * height

    @staticmethod
    def rectangle_P(width, height):
        return 2 * (width + height)


# 主程序
width = 4
height = 6
print(f"矩形的面积：{Geometry.rectangle_area(width, height)}")
print(f"矩形的周长：{Geometry.rectangle_P(width, height)}")