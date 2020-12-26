# 定義一個印出hello的函式
# def sayhelo():
#     print('hello')

# # 呼叫上方定義的函式
# sayhelo()

# def add(n1,n2):
#     result=n1+n2
#     print(result)

# add(3,4)
# add(7,8)

# return 資料 (數字,字串,布林值,列表,字典)

# #函式回傳 None
# def say(msg):
#     print(msg)
#     return

# #呼叫函式,取得回傳值
# value=say('hello')
# print(value) #印出None

# 定義函式
# 函式內部的程式碼,沒有做函式呼叫,就不會執行
# def qwe():
#     print(3*4)

# # 呼叫函式
# qwe()

# def qwe(n1,n2):
#     print(n1*n2)
#     return n1*n2
# fdsf=qwe(3,4)
# print(fdsf)


# 程式的包裝 : 同樣的邏輯可以重複利用
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

calculate(10)
calculate(20)
calculate(30)
calculate(40)