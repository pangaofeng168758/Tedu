"""
    输入一个美元,汇算成人民币为多少钱
"""
#字符串不能和浮点数(小数)相乘
# money = input("请输入美元:")
# rmb = float(money) * 6.572
# print(type(rmb))
# print("换算成人民币:",rmb)
# rmb = money*6
# rmb = money*6
# print(type(rmb))
# print("换算成人民币:",rmb)


# 63320
num_h = 63320//3600
num_m = 63320%3600//60
num_s = 63320%3600%60

print(num_h,num_m,num_s)