position=3-1
idx=0
len_list=(len(int_list))
while len_list>0:
   idx=(position+idx)%len_list
   print(int_list.pop(idx))
   len_list-=1
num=[10,20,30,40,50,60,80,10,20]
remove num(nums)
