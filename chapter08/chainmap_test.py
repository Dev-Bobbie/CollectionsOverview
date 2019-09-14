from collections import ChainMap

user_dict1 = {"a":"bobbie1","b":"bobbie2"}
user_dict2 = {"b":"bobbie3","d":"bobbie3"}

new_dict = ChainMap(user_dict1,user_dict2)
new_dict = new_dict.new_child({"aa":"aa","bb":"bb"})
print(new_dict.maps)
for key,value in new_dict.items():
    print(key,value)