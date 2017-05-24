l=['a','aaa','ab','ad','aab','a','ab']
l1=[]
l.sort()#sorting list.

for x in l[:]:
    if x in l1[:]:
        print 'removing duplicate', x
        l.remove(x)
        
    else:
        l1.append(x)

print 'final list',l
        
        
    
