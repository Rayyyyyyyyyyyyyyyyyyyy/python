# n=1
# while n<5:
#     if n==3:
#         break
#     n+=1
# print(n)

#m=0
# for x in [0,1,2,3]:
#     if x %2==0: #判斷式
#         continue
#     m+=1
# print(m)

# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)    #印出迴圈中的 
#     n+=1
# print('最後的 n:',n) #印出迴圈結束後的 n


#  continue
n=0
for x in [0,1,2,3]:
    if x%2==0: # x是偶數
        continue #直接進到下一迴圈
    print(x)
    n+=1
print('最後的 n:',n)

# else
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) #印出1+2+....+10的結果

# 綜合範例:找出整數平方根
# 輸入 9. 得到 3
# 輸入 11. 得到[沒有]整數的平方根

# n=input('輸入一個正整數:')
# n=int(n) #轉換輸入為數字
# for i in range(n): #i =  0~n-1
#     if i*i==n:
#         print('整數平方根',i)
#         break #用break 強制結束迴圈,不會執行else
# else:
#     print('沒有整數平方根')

# n 是答案 先輸入的是答案 在推回去找相匹配數字