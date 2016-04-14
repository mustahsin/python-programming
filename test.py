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
    s = person(word)
    personclass[word] = s



for i in range(1,num_lines):
    a = f.readline()
    wordarr = a.split()
    print wordarr

    name = wordarr[0]
    give = int(wordarr[1])
    divide = int(wordarr[2])

    plus_money = give/divide

    for i in range(3,3+divide):
        friend = wordarr[i]
        personclass[friend].addcash(plus_money)

    personclass[name].minuscash(give)

for key in personclass:
    print personclass[key].name ," : ", personclass[key].cash






# for i in range(0,num_lines):
#     for word in f.readline().split():
#         print(word)

