def cal_after(sa):
    shebao = sa * 0.165
    shui_path = sa - shebao - 3500
    if shui_path <= 0:
        tax = 0
    elif shui_path <= 1500:
        tax = shui_path * 0.03
    elif shui_path <= 4500:
        tax = shui_path * 0.1 - 105
    elif shui_path <= 9000:
        tax = shui_path * 0.2 - 555
    elif shui_path <= 35000:
        tax = shui_path * 0.25 - 1005
    elif shui_path <= 55000:
        tax = shui_path * 0.30 - 2755
    elif shui_path <= 80000:
        tax = shui_path * 0.35 - 5505
    else:
        tax = shui_path * 0.45 - 13505
    return sa - shebao - tax

import sys
for i in sys.argv[1:]:
    l = i.split(':')
    print(l[0] + ':' + format(cal_after(int(l[1])), '.2f'))
