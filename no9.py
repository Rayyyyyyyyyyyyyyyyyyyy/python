# # 參數 msg 預設資料為 'hello'
# def say(msg='hello'):
#     print(msg)

# # 印出 hello function
# say("hello function")
# say()


# def divide(n1,n2):
#     result=(n1/n2)
#     print(result)

# divide(12,2)
# divide(n2=34,n1=17)

# 函式接受無限參數 msgs
# def say(*msgs):
#     # 以 Tuple 的方式處理
#     for msg in msgs:
#         print(msg)

# say('hello','arbitrary','arguments')

# 參數的預設資料

def power(asd,qwe=0):
    print(asd**qwe) #*一個是乘 **兩個是平方
power(3,2)
power(4)

# def wer(n1,n2):
#     print(n1/n2)
# wer(6,2)
# wer(n2=10,n1=2)

# 無限\不定 參數資料

# def avg(*ns):
#     sum=0
#     for n in ns:
#       sum=sum+n
#     print(sum/len(ns))

# avg(3,4)
# avg(3,5,10)
# avg(1,4,-1,-8)