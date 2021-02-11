def ZhiShu(num):
    for i in range(2,num-1):
        if num % i ==0:
            return "不是质数"
        else:
            return "质数"


print(ZhiShu(23))
print(ZhiShu(44))
