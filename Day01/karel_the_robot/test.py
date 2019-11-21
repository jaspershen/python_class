print("hello")
1==3
1+3



a = 1
b = 1.0
d = [1,2]
e = (1,2)
f = {"x":1, "y":2}

##directonary
dog_d = {}
dog_d = {"big":3, "small":2, "golden":1, "spotted": 1}


##how many keys
len(dog_d)

##

dog_d["big"]


dog_d["small"]

dog_d["small"] = 4
dog_d['small']

dog_d

pow(3, dog_d['small'])

##return the contents of teh dictionary as a list of tuples

dog_d.items()

dog_d.keys()

dog_d.values()

test = list(dog_d.items())

type(test)
dog_d.keys()

list(dog_d.keys())[0]

dog_d.items()

list(dog_d.items())

type(list(dog_d.items())[0])


test = list(dog_d.items())[0]


type(test)

test

test

test[0]

test[1]

##what's the different btween list and tuple

##add a new key to dic

dog_d["short hair"] = 5

dog_d

dog_d[1]

##more comples data structure lists as values to keys

pig_d = {'starts':[3,4,5], "end":[13,20,35]}
pig_d

pig_d["starts"]

type(pig_d["starts"])

test2 = list[ (2,3),(3,5) ]

from pipe import  *

genes_d = {"EFX1":{"accession_ID": "EBS", "chromosome":19},"coordinate":[1328,140]}

genes_d

import pipe

genes_d


genes_d["EFX1"]

type(genes_d["EFX1"])


if "EFX1" in genes_d:
    print(True)
else:
    print(False)


## special print characters
##TAB \t
## neline \n



"EFX1" in genes_d

genes_d["EFX1"]['coordinate']



test = genes_d["EFX1"]


type(test)

test

genes_d

##condition
#if else
#

tomato_color = "red"


if(tomato_color == "red"):
    print("yes, it is red")
else:
    print("not, it is not red")




dna_string = "AGCT"


len(dna_string)

from pipe import  *

dna_string | len


[1,2,3] | add

if 1 == 1 or 2 != 1:
    print("Yes")
else:
    print("No")



##sets, use '{}'to construct a set
a_set = {1,2,3,4,"cat", "dog", 9,10,5,2,3,4,5,6,6}

type(a_set)

a_set

a_set | type
