#Write a python function called is_username_available that checks if a new username can be used
#convert the list of existing_usernames into a set inside your function to ensure a fast lookup.
#check if the new_username exists in that set
#return true if the username is availabe
#return false if the username is already taken(already in the set)

def is_username_available(existing_usernames,new_username):
    if existing_usernames == new_username:
        print("Username unavailable")
    else:
        print("Username available")
existing_usernames = {"Ram","Hari","Sita","Geeta","Shyam"}
new_username_byuser = input("Enter username :\n")
new_username = existing_usernames.copy()
new_username.add(new_username_byuser)

is_username_available(existing_usernames,new_username)




