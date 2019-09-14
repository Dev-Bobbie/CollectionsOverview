
from collections import OrderedDict

user_dict = OrderedDict()

user_dict["b"] = "bobbie2"
user_dict["a"] = "bobbie1"
user_dict["c"] = "bobbie3"

# print(user_dict.popitem())
# print(user_dict.pop("a"))
user_dict.move_to_end('b')
print(user_dict)