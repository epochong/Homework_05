import random


def max_and_sum(*p) :
    return max(*p), sum(*p)


li = []
for i in range(1,11):
    for j in range(random.randint(1, 20)):
        li.append(random.randint(0, 100))
    print("第 ",i," 组:",li)
    max_val = max_and_sum(li)[0]
    sum_val = max_and_sum(li)[1]
    print("最大值为：", max_val, "和为：", sum_val)
    li = []