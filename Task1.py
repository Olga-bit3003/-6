#Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Используем скобки для смены приоритета операции
# num -> /^[+-]?\d+(\.\d+)?/
# group -> ( term )
# value -> num | group
# mul -> num [*/] mul
# mul -> num
# sum -> mul [+-] sum
# sum -> mul
# term -> sum

import re


def num(exp):
    exp = exp.lstrip()
    res = re.match("^[+-]?\d(\.\d+)?", exp)
    if res:
        return float(res.group(0)), exp[res.end():]
    else:
        return None, exp

def value(exp):
    res, rest = num(exp)
    if res != None:
        return res, rest
    res, rest = grouping(exp)
    return res, rest

def grouping(exp):
    exp = exp.lstrip()
    rest = ""
    if exp[0] == "(":
        rest = exp[1:]
    else:
        return None, exp
    numb, rest = term(rest)
    if rest[0] != ")":
        return None, exp
    return numb, rest[1:]

def mul_oper(exp):
    exp = exp.lstrip()
    res = re.match("[*/]", exp)
    if res:
        return res.group(0), exp[res.end():]
    else:
        return None, exp

def mul(exp):
    numb1, rest1 = value(exp)

    if numb1 == None:
        return None, exp

    op, rest2 = mul_oper(rest1)

    if op == None:
        return numb1, rest1

    numb2, rest2 = mul(rest2)

    if op == "*":
        return numb1 * numb2, rest2
    if op == "/":
        return numb1 / numb2, rest2

    return None, exp

def sum_oper(exp):
    exp = exp.lstrip()
    res = re.match("[+-]", exp)
    if res:
        return res.group(0), exp[res.end():]
    else:
        return None, exp

def sum(exp):
    numb1, rest1 = mul(exp)

    if numb1 == None:
        return None, exp

    op, rest2 = sum_oper(rest1)

    if op == None:
        return numb1, rest1

    numb2, rest2 = sum(rest2)

    if op == "+":
        return numb1 + numb2, rest2
    if op == "-":
        return numb1 - numb2, rest2

    return None, exp

def term(exp):
    return sum(exp)

print(term("(2 + 2) * 5 ")) # меняем приоритет ()
 