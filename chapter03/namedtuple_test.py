from  collections import namedtuple

User = namedtuple("User",["name","age","height","edu"])

# user = User(name='bobbie',age=25,height=170)

user_tuple = ('bobbie',25,170)
user = User(*user_tuple,"master")

user_info_dict = user._asdict()
print(user_info_dict)
print(user)
# print(user.age,user.name,user.height)   