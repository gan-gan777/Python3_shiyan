#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2018-03-24
# Personal Tax Calculator

import sys

# 个税计算公式：
# 1. 应纳税所得额 = 工资金额 - 各项社会保险 - 起征点（3500元）
# 2. 应纳税额 = 应纳税所得额 * 税率 - 速算扣除数
# 公式1中的“各项社会保险费”暂不考虑。

# 个税起征点
proint = int(3500)

# 异常处理：参数数量不准确、输入为负数、输入内容无法转成整数型，都需要打印参数错误提示。
try:
    len(sys.argv) == 2    # 参数个数必须为2（连同参数名称在内）
    gongzi != 0    # 输入工资不能<=0
    gongzi = int(sys.argv[1])    # 输入的“工资字符”必须能转成整型 
    
except:
    print("Parameter Error")

TI = 'Taxable Income'
TP = 'Tax Payable'

TI = int(str) - proint
if TI <= 0:
    print(format(0,".2f"))
elif TI <= 1500 and TI > 0:
    tax = format((TI * 0.03 - 0),".2f")
    print(tax)
elif TI > 1500 and TI <= 4500:
    tax = format((TI * 0.1 - 105),".2f")
    print(tax)
elif TI > 4500 and TI <= 9000:
    tax = format((TI * 0.2 - 555),".2f")
    print(tax)
elif TI > 9000 and TI <= 35000:
    tax = format((TI * 0.25 - 1005),".2f")
    print(tax)
elif TI > 35000 and TI <= 55000:
    tax = format((TI * 0.30 - 2755),".2f")
    print(tax)
elif TI > 55000 and TI <=80000:
    tax = format ((TI * 0.35 - 5505),".2f")
    print(tax)
elif TI > 80000:
    tax = format((TI * 0.45 - 13505),".2f")
    print(tax)
