# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# обчислити площу трикутника якщо трикутник задано довжиною однієї з сторін та вистою опущеною на неї
# позначення
'''
сторона трикутника - float - triangle_side
висота трикутника - float - triangle_height
площа трикутника - float - area
'''
# введення
triangle_side = float(input('сторона трикутника'))
triangle_height = float(input('висота трикутника'))
# обчислюємо площу
area = 0.5*triangle_side*triangle_height
# виведемо результат
print('площа трикутника={0}cm'.format(area))


