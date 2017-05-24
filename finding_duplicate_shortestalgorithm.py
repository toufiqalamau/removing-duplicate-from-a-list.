l=['a','aaa','ab','ad','aab','a','ab']
l1=[]#empty list.
l2=[]#list of removed duplicates.
l.sort()#sorting list.

for x in l[:]:
    if x in l1[:]:
        l.remove(x)
        l2.append(x)
        
    else:
        l1.append(x)

print 'duplicate items: ',l2#this will show the removed items.
        
    
