
def ackermann(m, n): #遞迴函式
    if m == 0: # 如果 m 等於 0，返回 n + 1
        return n + 1
    elif n == 0:# 如果 n 等於 0，計算 A(m-1, 1)
        return ackermann(m - 1, 1)
    else:    # 否則，計算 A(m-1, A(m, n-1))
        return ackermann(m - 1, ackermann(m, n - 1))
    
m=int(input("請輸入 m 的值: "))
n=int(input("請輸入 n 的值: "))
result = ackermann(m, n)
print(result)
