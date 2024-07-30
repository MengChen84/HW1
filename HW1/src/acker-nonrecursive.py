# 程式碼皆由用chatGTP撰寫
def ackermann_non_recursive(m, n):
                
    stack = []# 初始化一個空的堆疊
    
    stack.append((m, n))# 將初始值 (m, n) 推入堆疊
    
    
    while stack:# 當堆疊不為空時
        
        m, n = stack.pop()# 取出堆疊頂部的值
        
       
        if m == 0: # 如果 m 等於 0
            
            if stack:# 如果堆疊不為空，更新堆疊頂部的值
                stack[-1] = (stack[-1][0], n + 1)
            
            else:# 否則，返回 n + 1
                return n + 1
        
        elif n == 0:# 如果 n 等於 0，將 (m-1, 1) 推入堆疊
            stack.append((m - 1, 1))
       
        else: # 否則，將 (m-1, None) 和 (m, n-1) 推入堆疊
            stack.append((m - 1, None))
            stack.append((m, n - 1))
    
    return n

m = int(input("請輸入 m 的值: "))
n = int(input("請輸入 n 的值: "))

result = ackermann_non_recursive(m, n)
print(f"acker-nonrecursive({m}, {n}) = {result}")
