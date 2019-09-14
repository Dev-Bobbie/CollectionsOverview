from collections import deque


# deque GIL是线程安全的，list不是线程安全的
# user_list = deque(["bobbie",25,175])
# named_tuple = ("bobbie",29,175)
# user_list.append(named_tuple)

user_deque = deque(["bobbie",[25],175])
user_deque2 = deque(["bobbie2",[27],178])

user_deque.extend(user_deque2)
# user_deque.appendleft('bobbie2')
user_deque2 = user_deque.copy()
user_deque2[1].append(28)
print(user_deque,user_deque2)
print(id(user_deque),id(user_deque2))

print(user_deque)