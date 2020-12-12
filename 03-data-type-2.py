# 목록 list, tuple
# 서전 dict - dictionary
# 집합 set

# list
print("list")
list_a = [1, 2, 3]
print(list_a)
print(type([1, 2, 3]))
# index는 0부터 시작한다.
print(list_a[0])
print(list_a[1])
print(list_a[2])

#slice 는 마지막 index는 포함하지 않는다.
print(list_a[0:2])

list_a.append(4)
print(list_a)

list_a.remove(2)
print(list_a)

list_a.clear()
print(list_a)

# tuple (1, )
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))
# tuple_a.append(4) tuple은 한 번 생성 후 내부 값 변경이 되지 않음.


# dict (map) {}
# key & value

dict_a = { "apple" : "a type of fruits",
 "pen" : "a thing to write"
 }
print(dict_a)
print(dict_a["apple"])
# edit value
dict_a["pen"] = "something to write"
print(dict_a)

# set se([])
set_a = set([1, 2, 3])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

# 집합 - 교집합, 합집합, 차집합, 여집합
# 중복 제거
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
