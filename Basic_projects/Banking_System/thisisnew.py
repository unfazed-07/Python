# def create_user_profile(**kwargs):
#     print(kwargs)
#     user_profile = {}
#     for key, value in kwargs.items():
#         user_profile[key]=value
#         return user_profile
# D={'name': 'Alice', 'age': 30, 'city': 'WonderLand'}
# create_user_profile(**D)

def print_info(*args, **kwargs):
    print(args)
    print(kwargs)

print_info(10,20,40,namerwer84="alice", age = 30, )