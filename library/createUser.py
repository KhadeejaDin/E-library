__author__ = 'Administrator'
import pickle
from User import User

if __name__ == '__main__':

    super_user = User("kaiying","111111")
    super_user.superUser = True
    user = User("joe","1")
    super_user.superUser = False
    my_list = [super_user,user]
    with open('user_data.pkl', 'w') as output:
        pickle.dump(my_list, output)
