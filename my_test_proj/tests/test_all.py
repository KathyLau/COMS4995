#import the method from project folder
from my_test_proj import inc
from my_test_proj import searchbar
from my_test_proj import dist
from my_test_proj import borough


#this is a sample test from prof paine's project
def test_inc():
    assert inc(1) == 2, "did not pass test_inc"
    
#below are some possible test ideas to use on ""code"" in map.py

#test 1 - checks if a string is taken in from the searchbar - should always end up being a string
def test_searchbar():
    searchedvalue = isinstance(searchbar(), str)
    if searchedvalue:
        print("Pass test 1")
    else
        print("Fail test 1")

#test 2 - check if any duplicates in list of shops
def anydup(thelist):
  seen = set()
  for x in thelist:
    if x in seen: print("Fail test 2")
    seen.add(x)
  return print("Pass test 2")
    

#test 3 - check if a searched value for distance is an int
def test_dist():
    distvalue = isinstance(dist(), int)
    if distvalue:
        print("Pass test 1")
    else
        print("Fail test 1")


#test 4 - check if list is empty
def emptyList(thelist):
    if not a:
        print("Fail test 3")
    else:
        print("Pass test 3")

#test 5 - check if searched value for borough is a string
def test_borough():
    b = isinstance(borough(), str)
    if b:
        print("Pass test 1")
    else
        print("Fail test 1")
              
            
