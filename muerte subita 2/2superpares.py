print filter(lambda x: x%2==0 and x/10)%2==0 and (x/100)%2==0 and (x/1000)%2==0,[2,50,32,46,87,1234,2468,3222,2666,2134,4244])

print map(lambda h: reduce(lambda i,p:(int(i)*10)+int(p) ,h), filter(lambda z: reduce(lambda w,t: (int(w)%2)+(int(t)%2), z)==0 , map(lambda x: list(str(x)), [812,123,24,15,16,17,864286, 2468,444])))
