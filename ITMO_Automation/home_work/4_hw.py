# Задача 1

print('Задача 1')

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

obj1 = Rectangle(2, 5)
obj2 = Rectangle(10, 10)
obj3 = Rectangle(5, 10)
print(obj1.area(), obj1.perimeter())
print(obj2.area(), obj2.perimeter())
print(obj3.area(), obj3.perimeter())

print('\n')

# Задача 2

print('Задача 2')

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

num1 = Math(10, 20)
print(num1.addition())
print(num1.multiplication())
print(num1.division())
print(num1.subtraction())

print('\n')

# Задача 3

print('Задача 3')

class Button:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc


    def click(self):
        return "Клик по кнопке - {}".format(self.text)

Text_Box = Button('Text Box', '/Text_Box', '')
print(Text_Box.click())

Check_Box = Button('Check Box', '/Check_Box', '')
print(Check_Box.click())

Radio_Button = Button('Radio_Button', '/Radio_Button', '')
print(Radio_Button.click())

Web_Tables = Button('Web_Tables', '/Web_Tables', '')
print(Web_Tables.click())

Buttons = Button('Buttons', '/Buttons', '')
print(Buttons.click())

Links = Button('Links', '/Links', '')
print(Links.click())

Broken_Links = Button('Broken_Links', '/Broken_Links', '')
print(Broken_Links.click())

Upload_and_Download = Button('Upload_and_Download', '/Upload_and_Download', '')
print(Upload_and_Download.click())

Dynamic_Properties = Button('Dynamic_Properties', '/Dynamic_Properties', '')
print(Dynamic_Properties.click())