tpl=(1,2,3,2,1,2,3,2,1,2,3,8,6,5,3,-1,-8,-10)
nested=tuple((tpl[i],tpl[i+1]) for i in range(0,len(tpl),2))
print(nested)