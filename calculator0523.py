#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 2018-05-23
# Personal Tax Calculator


import sys # 导入系统模块
print(sys.argv) # 打印命令参数

# 异常处理：用户输入的参数必须为单个、正确的薪水！参数的数量不正确、输入小于或等于0、无法转换成整数，都需要打印参数错误提示。
try:
    len(sys.argv) == 2 # 参数的个数必须为2（包括参数名词在内）
    salary = int(sys.argv[1]) # 薪水等于传入的第一个参数
    assert salary > 0 # 输入薪水必须大于0
except ValueError:
    print('数据类型错误')
    exit()
except AssertionError:
    print('输入薪水必须>0')
    exit()

# 定义所需的变量
tax_point = 3500 # 个税起征点
tax_salary = int(salary) - tax_point # 应纳税所得额公式,社会保险暂不考虑

# 按照公式计算个税
if tax_salary <= 0:
    print(format(0, ".2f"))
elif 0 <= tax_salary <= 1500:
    tax = format((tax_salary * 0.03 - 0), ".2f")    
    print(tax)
elif 1500 < tax_salary <= 4500:
    tax = format((tax_salary * 0.10 - 105), ".2f")
    print(tax)
elif 4500 < tax_salary <= 9000:
    tax = format((tax_salary * 0.20 - 555), ".2f")
    print(tax)
elif 9000 < tax_salary <= 35000:
    tax = format((tax_salary * 0.25 - 1005), ".2f")
    print(tax)
elif 35000 < tax_salary <= 55000:
    tax = format((tax_salary * 0.30 - 2755), ".2f")
    print(tax)
elif 55000 < tax_salary <= 80000:
    tax = format((tax_salary * 0.35 - 5505), ".2f")
    print(tax)
elif tax_salary > 80000:
    tax = format((tax_salary * 0.45 - 13505), ".2f")
    print(tax)
