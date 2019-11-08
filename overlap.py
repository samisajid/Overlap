import random

def overlap(a,b):
    ''' This function takes two lists or tuples each containing two elements and identify wether these intervals overlap or not'''
    amax=max(a)
    amin=min(a)
    bmax=max(b)
    bmin=min(b)
    #This verification covers all the cases where the intervals can overlap
    if amin<bmax<amax or amin<bmin<amax or bmin<amin<bmax or bmin<amax<bmax or \
    (bmin==amin and bmax==amax):
        print(f"{a} and {b} overlap")
        return True
    else:
        print(f"{a} and {b} do not overlap")
        return False
    
if __name__=='__main__':
    #A test case with random chosen values of each interval to test the above function
    iteration=20
    for i in range(iteration):
        overlap((random.randint(-999999,999999),random.randint(-999999,999999)),\
                (random.randint(-999999,999999),random.randint(-999999,999999)))
