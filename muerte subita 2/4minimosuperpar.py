for dato in map(lambda x: min(x) , map(lambda y: filter(lambda z: z%2==0 and (z/10)%2==0 and (z/100)%2==0 and (z/1000)%2==0,y) , [[92,37,12,48],[71,45,66,40],[111,8246,257],[1000,228]])):
    print dato
