from collections import defaultdict

users = ["bobbie1","bobbie2","bobbie3",'bobbie2','bobbie3']

# user_dict = {}
# for user in users:
#     if user not in user_dict:
#         user_dict[user] = 1
#     else:
#         user_dict[user] +=1

# for user in users:
#     user_dict.setdefault(user,0)
#     user_dict[user] +=1


# default_dict = defaultdict(int)
# for user in users:
#     default_dict[user] +=1

group_dict = {
     "group":{
         "name":"",
         "nums":0
     }
 }

def gen_default():
    return {
         "name":"",
         "nums":0
     }

default_dict = defaultdict(gen_default)

default_dict["group1"]
print(default_dict)