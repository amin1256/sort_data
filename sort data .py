import random #libray to select random



class human: #an oop to type of my data
    def __init__(self , name , major):
        self.name = name 
        self.major = major
        if major == 'football':
            print(name)


info_name = input('please type the list of player : ')
info_name = info_name.split()
info_major = input('type the major of player list : ')
human(info_name , info_major)
# get information from the users

a = random.sample(info_name , k=2) # create a first row of data
print('A = %s' % (a))

for word in a:
    if word in info_name:
        info_name.remove(word)
print('B = %s' % (info_name)) # create a second row of data and diffrent from first one


