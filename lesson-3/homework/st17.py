st={1,2,3,4,5,3,2,312,213}
new_st=set()
for i in st:
    if i%2==1:
        new_st.add(i)
print(new_st)