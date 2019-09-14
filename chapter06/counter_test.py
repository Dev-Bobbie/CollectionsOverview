from collections import Counter


users = ["bobbie1","bobbie2","bobbie2","bobbie3","bobbie2"]

user_counter = Counter("fsfsdfdsfdsfs")
user_counter2 = Counter("dsdsdsd")
user_counter.update(user_counter2)

# topn的问题 堆
print(user_counter.most_common(2))
# print(user_counter)