name_tuple = ('bobbie1','bpbbie2')

user_tuple = ('bobbie',29,'beijing','edu')

name,*other = user_tuple

name_tuple = ('bobbie',[])
name_tuple[1].append(22)
print(name_tuple)


user_info_dict = {}
user_info_dict[user_tuple] = 'bobbie'
print(user_info_dict)