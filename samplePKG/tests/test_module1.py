import samplePKG as s

def testAdd():
    assert s.myAdd(1,2)==3
    assert s.myAdd(5,6)==11

def testSub():
    assert s.mySub(2,1)==1
    assert s.mySub(1,2)==1
    assert s.mySub(2,2)==0
