tuple_1=("ram","teja","krishna","ramana","loki","raju","rocky")
tuple_2=(1022,2354,9856,4257,420,457,819)


user_name=input("enter your user id:: ")
user_password = int(input("enter your password :: "))
if tuple_1:
    index = tuple_1.index(user_name)
    if tuple_2[index] == user_password:
        print("ligin succesfully completed.  welcome to.......")
    else:
        print("user password is wrong")
else:
    print("user name is wrong")
