
import time
import random
names=['sun','mun','bun','dun','pun']
subjects=['python','php','perl','java']
def people_list(num):
    results=[]
    for i in range(num):
        person={
            'id':i,
            'names':random.choice(names),
            'subjects':random.choice(subjects)

        }
    yield person
t1=time.clock()
people=people_list(1000)
t2=time.clock()
print("Time Taken",t2-t1)