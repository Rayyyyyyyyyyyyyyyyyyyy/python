x=1249817*12312
print(x)
x=123**3
print(x)
x=x-3
print(x)
x+=1 # x=x+1

# 字串運算
s='hello'
print(s)
s='hell\'o'+'world' 'pekae'
# \是跳脫 隔開 +是串接 空白也可
print(s)
#\n 是換行 '''三個''' 也可以換行
s='''qweq


qweq'''
print(s)
s='hello'*3+'world'
# *數字 重複數字次數
print(s)
# 字串會對內部的字元編號(索引) 從0開始算
s='12345678910111213141516'
print(s[0])
print(s[1:4])
print(s[1::2])
# (s[1:4]) 包含開頭不包結尾所以是123字元
# (s[1:]) 只給開頭不給結尾 就是開頭往後所有
# (s[:4]) 只給結尾不給開頭 就是開頭為止前面所有