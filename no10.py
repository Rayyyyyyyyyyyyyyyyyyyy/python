# # 載入sys模組
# import sys
# # 使用sys模組
# print(sys.platform)
# print(sys.maxsize)
# print(sys.path)

# # 載入sys模組  s 是別名
# import sys as s
# # 使用sys模組
# print(s.platform)
# print(s.maxsize)
# print(s.path)

# 載入內建的 sys 模組並取得資訊
# import sys as system
# print(system.platform)
# print(system.maxsize)

# 鍵入 no10test 模組,載入使用
# import no10test
# result=no10test.distance(1,1,5,5)
# print(result)
# result=no10test.slope(1,2,5,6)
# print(result)s

# 調整搜尋模組的路徑
import sys
sys.path.append("test") # 在模組搜尋路徑列表中[新增路徑]
print(sys.path) # 印出模組的搜尋路徑
print('---------------')
import no10test
print(no10test.distance(1,1,5,5))
