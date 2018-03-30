#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2018-03-30
# Personal Tax Calculator

import sys    # 导入系统模块
insurance = float(0.165)    # 五险一金占工资比例
TT = int(3500)    # 纳税起征点金额

# 个税计算公式：
# 1. 应纳税所得额 = 工资金额 - 各项社会保险 - 起征点（3500元）
# 2. 应纳税额 = 应纳税所得额 * 税率 - 速算扣除数

# 英语单词翻译：
# Wages：工资；
# Pre-tax wages：税前工资，简写为“Pre_wages”；
# After-tax wages：税后工资，简写为“Aft_wages”；
# Insurance：保险税率；
# Rapid：速算扣除数；
# Tax_rate：税率；
# Taxable Income：应纳税所得额，简写为“TI”；
# Tax Payable：应纳税额，简写为“TP”；
# Tax Threshold：个税起征点,简写为“TT”；

# 税后工资计算公式
def furmula(Pre_wages, rapid, tax_rate)
    try:
        ins_amount = Pre_wages * insurance    # 五险一金费用总额
        TI = Pre_wages - ins_amount - TT    # 应纳税所得额计算公式
        TP = TI * tax_rate - rapid    # 应纳税额计算公式
        Aft_wages = format((Pre_wages - ins_amount - TP), ".2f")    # 税后工资计算公式
        return Aft_wages
    except:
        print("参数错误")

# 多员工工资计算
def Calc(id, Aft_wages)
    TI = Pre_wages - ins_amount - TT
    Aft_wages_dict = {}
    if TI <= 0:
        Aft_wages = furmula(Pre_wages, 0, 0)
    elif TI > 0 and <= 1500:
        Aft_wages = furmula(Pre_wages, 0, 0.03)
    elif TI > 1500 and TI <= 4500:
        Aft_wages = furmula(Pre_wages, 105, 0.1)
    elif TI > 4500 and TI <= 9000:
        Aft_wages = furmula(Pre_wages, 555, 0.2)
    elif TI > 9000 and TI <= 35000:
        Aft_wages = furmula(Pre_wages, 1005, 0.25)
    elif TI > 35000 and TI <= 55000:
        Aft_wages = furmula(Pre_wages, 2755, 0.3)
    elif TI > 55000 and TI <=80000:
        Aft_wages = furmula(Pre_wages, 5505, 0.35)
    elif TI > 80000:
        Aft_wages = furmula(Pre_wages, 13505, 0.45)
    print(id, end='')
    print(':', end='')
    print(Aft_wages)

# 用户传参
for arg in sys.argv[1:]:
    deployee_list = arg.split(':')
    calc(int(deployee_list[0]), int(deployee_list[1]))
