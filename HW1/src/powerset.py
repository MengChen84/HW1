# 程式碼皆由用chatGTP撰寫
def powerset(s):
    
    if len(s) == 0:
        return {()}
    else:
        
        first_element = s[0]# 取出集合的第一個元素
        
        remaining_powerset = powerset(s[1:])# 計算去除第一個元素後剩餘集合的冪集
        
        
        with_first = {tuple(sorted((first_element,) + subset)) for subset in remaining_powerset}# 將第一個元素添加到剩餘冪集中的每個子集中
        
        
        return remaining_powerset | with_first# 返回包含有第一個元素和沒有第一個元素的所有子集


num_elements = int(input("請輸入陣列大小："))


elements = []# 初始化一個空的列表來存儲元素


for i in range(num_elements):# 逐個從使用者那裡獲取元素
    element = input(f"請輸入第 {i+1} 個陣列內容：")
    elements.append(element.strip())

elements = tuple(elements)# 將列表轉換為 tuple


result = powerset(elements)# 計算冪集


# 輸出
formatted_result = {tuple(sorted(subset)) for subset in result}
print( formatted_result)
