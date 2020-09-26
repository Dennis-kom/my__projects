from tkinter import *

root = Tk()
ram = []

root.title("Calculator")

e = Entry(root, width=15, bg="White", borderwidth=5)
e.grid(row=0, column=1)
s_error = 'syntax error'
m_error = 'matn error'


# checking - calculation proirity aritmethic sign
def first_priority_sign(ch):
    return ch == '*' or ch == '/'


# checking if current value is a digit
def is_sign(ch):
    return ch == '-' or ch == '+' or ch == '*' or ch == '/'

# avoiding wrog signs
def sign_secuence(s1,s2):
    if (s1 == '-' and s2 == '-') or (s1 == '+' and s2 == '-'):
        return  True
    else:
        return False

# aritmethic conversation and calculation
def arimetic(a,s,b):
    num1 = float(a)
    num2 = float(b)

    if s == '+':
        return num1 + num2
    if s == '-':
        return num1 - num2
    if s == '*':
        return num1 * num2
    if s == '/':
        return num1 / num2

def convert_to_number(num_set):
    return float(num_set)


# avoiding divide by zero
def valid_calc(a,s,b):
    if s == '/' and b == 0.0:
        return False
    return True


def result_calc(row):
    global m_error
    t_float = 1.1
    t_string = 'c'
    final_result = []
    tmp_l = []
    tmp_r = []

    # search and resolve first priority expressions
    i = 0
    while i < len(row):
        if type(row[i]) == type(t_string) and first_priority_sign(row[i]):
            cur_idx = i
            if valid_calc(row[i-1], row[i], row[i+1]):
                cur_res = arimetic(row[i-1], row[i], row[i+1])
            else:
                return m_error

            tmp_l = row[0:cur_idx-1]
            tmp_r = row[i+2:len(row)]

            tmp_l.append(cur_res)
            row = tmp_l + tmp_r
            i -= 2
        else:
            i += 1

    # search resolve second priority expressions
    i = 0
    while i < len(row):
        if type(row[i]) == type(t_string):
            cur_res = arimetic(row[i - 1], row[i], row[i + 1])
            tmp_l = row[0:i - 1]
            tmp_r = row[i + 2:len(row)]

            tmp_l.append(cur_res)
            row = tmp_l + tmp_r
            i -= 2
        else:
            i += 1

    return row[0]







# define numbers and signs
def revoke_numbers(ram):
    global s_error
    minus = '-'
    state_val = {"initial": 0, "buffering_num": 1, "sign_intake": 2}
    buffer = ""
    result = []
    i = 0
    state = state_val["initial"]

    while i < len(ram):
        if not state and is_sign(ram[i]):
            if ram[i] == minus:
                buffer += minus
                state += 1
                i += 1
            else:
                return s_error

        elif (not state or state == state_val["buffering_num"]) and ram[i].isdigit():
            buffer += ram[i]
            state = state_val["buffering_num"]
            i += 1
            if i > len(ram)-1:
                result.append(float(buffer))
        elif state == state_val["buffering_num"] and is_sign(ram[i]):
            # last symbol is sign or two signs came each after other
            if i == len(ram) - 1 or (i < len(ram) - 1 and is_sign(ram[i+1])):
                return s_error
            if i < len(ram):
                state = state_val["sign_intake"]
                result.append(float(buffer))
                result.append(ram[i])
                state = state_val["buffering_num"]
                buffer = ""
                i += 1

    return result


def engine(ram):
    global s_error
    tec = revoke_numbers(ram)
    if tec == s_error:
        return s_error
    else:
        return result_calc(tec)


# buttons definition
def click_one():
    ram.append('1')
    e.insert(END, '1')
def click_two():
    ram.append('2')
    e.insert(END, '2')
def click_three():
    ram.append('3')
    e.insert(END, '3')
def click_four():
    ram.append('4')
    e.insert(END, '4')
def click_five():
    ram.append('5')
    e.insert(END, '5')
def click_six():
    ram.append('6')
    e.insert(END, '6')
def click_seven():
    ram.append('7')
    e.insert(END, '7')
def click_eight():
    ram.append('8')
    e.insert(END, '8')
def click_nine():
    ram.append('9')
    e.insert(END, '9')
def click_zero():
    ram.append('0')
    e.insert(END, '0')
def click_plus():
    ram.append('+')
    e.insert(END, '+')
def click_minus():
    ram.append('-')
    e.insert(END, '-')
def click_multiplication():
    ram.append('*')
    e.insert(END, '*')
def click_divide():
    ram.append('/')
    e.insert(END, '/')
def click_clear():
    del ram[len(ram)-1]
    e.delete(len(ram)-1,END)
def click_clear_all():
    ram.clear()
    e.delete(0, END)
def click_eql():
    print("IN click : {}".format(ram))
    e.insert(END, '=')
    e.delete(0, END)
    e.insert(END, engine(ram))


# button implenteation
one = Button(root,text="1", padx=5, pady=5,command=click_one).grid(row=4, column=0)
two = Button(root,text="2", padx=5, pady=5,command=click_two).grid(row=4, column=1)
three = Button(root,text="3",padx=5, pady=5,command=click_three).grid(row=4, column=2)
four = Button(root,text="4",padx=5, pady=5,command=click_four).grid(row=5, column=0)
five = Button(root,text="5",padx=5, pady=5,command=click_five).grid(row=5, column=1)
six = Button(root,text="6",padx=5, pady=5,command=click_six).grid(row=5, column=2)
seven = Button(root,text="7",padx=5, pady=5,command=click_seven).grid(row=6, column=0)
eight = Button(root,text="8",padx=5, pady=5,command=click_eight).grid(row=6, column=1)
nine = Button(root,text="9",padx=5, pady=5,command=click_nine).grid(row=6, column=2)
zero = Button(root,text="0",padx=5, pady=5,command=click_zero).grid(row=7, column=0)

plus = Button(root,text="+",padx=5, pady=5,command=click_plus).grid(row=7, column=1)
minus = Button(root,text="-",padx=5, pady=5,command=click_minus).grid(row=7, column=2)
mult = Button(root,text="x",padx=5,pady=5,command=click_multiplication).grid(row=8,column=0)
divide = Button(root,text="/",padx=5,pady=5,command=click_divide).grid(row=8,column=1)
eql = Button(root,text="=",padx=5, pady=5,command=click_eql).grid(row=8, column=2)
clear = Button(root,text='del',padx=5,pady=5,command=click_clear).grid(row=9,column=0)
clear_all = Button(root,text="c",padx=5,pady=5,command=click_clear_all).grid(row=9,column=1)


root.mainloop()





