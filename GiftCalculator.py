class person:
   'Common base class for all employees'
   cash = 0
   name=""

   def __init__(self, name):
      self.name = name
      self.cash =0

   def minuscash(self,money):
       self.cash = self.cash - money

   def addcash(self,money):
     self.cash = self.cash + money


f = open("E:/Mypractie/python/a.txt",'r')

num_lines = sum(1 for line in f)   # number of lines of the file
print num_lines
f.close()
f = open("E:/Mypractie/python/a.txt",'r')

person_dict = {}

print(person_dict)
personlist=[]
i=0

personclass={}

for word in f.readline().split():
    s = person(word)                             # creating a new object
    personclass[word] = s                        # appending it to the dictionary



for i in range(1,num_lines):                        
    a = f.readline()                              # taking one line
    wordarr = a.split()                           # this array containing words
    print wordarr

    name = wordarr[0]                             # first positon holds the person name who is giving
    give = int(wordarr[1])                        # how much money he looses
    divide = int(wordarr[2])                      # to how many people

    plus_money = give/divide                      # how much to add

    for i in range(3,3+divide):                   # how many people taking the money
        friend = wordarr[i]
        personclass[friend].addcash(plus_money)   # adding to their account

    personclass[name].minuscash(give)                # minus from giving person

for key in personclass:
    print personclass[key].name ," : ", personclass[key].cash






# for i in range(0,num_lines):
#     for word in f.readline().split():
#         print(word)

