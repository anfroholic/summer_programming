# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

hello = "world"


"""
int
bool
float
str
"""
# public String return_this(String this){}
def returns_this(this):
    return this
# this is a comment :O

def make_anon(llama):
    return lambda panda: panda * llama

double_panda = make_anon(3)

print(f'{double_panda(12) = }')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} I am {hello}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('hi, ' + name + "I am " + hello)
    print('{hello = }')
    print(f'{returns_this("this")} and some more stuff {hello = }')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
