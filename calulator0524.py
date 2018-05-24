#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 2018-05-24
# 税后工资计算器

import sys
print(sys.argv)

def calc(pre_salary): # 计算税后工资的函数
    social_insurance = pre_salary * 0.165 # 社保
    taxable_income = pre_salary - social_insurance - 3500 # 应纳税所得额
    # 按条件计算应纳税额 
    if taxable_income <= 0:
        tax = 0
    elif 0 < taxable_income <= 1500:
        tax = taxable_income * 0.03
    elif 1500 < taxable_income <= 4500:
        tax = taxable_income * 0.10 - 105
    elif 4500 < taxable_income <= 9000:
        tax = taxable_income * 0.20 - 555
    elif 9000 < taxable_income <= 35000:
        tax = taxable_income * 0.25 -1005
    elif 35000 < taxable_income <= 55000:
        tax = taxable_income * 0.30 - 2755
    elif 55000 < taxable_income <= 80000:
        tax = taxable_income * 0.35 - 5505
    elif 80000 < taxable_income:
        tax = taxable_income * 0.45 - 13505
    return pre_salary - social_insurance - tax 

for arg in sys.argv[1:]: # 显示工号：税后工资
    uid, pre_salary = arg.split(':') # 将参数提取成一个个单独的列表
    try:
        pre_salary = int(pre_salary)
    except ValueError:
        print('Parameter Error')
    else:
        aft_salary = calc(pre_salary)
        print(uid + ':' + format(aft_salary), '.2f')
