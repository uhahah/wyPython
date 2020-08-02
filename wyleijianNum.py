# arr=[];
# array=[];
# for j in range(0,9):
#     i=6
#     q=51
#     for i in range(6,11):
#         array.append(i+j*5)
#         i+=1
#     for q in range(51,56):
#         array.append(q+j*5)
#         q+=1
#     arr.append(array)
#     array=[]
# print(arr)

arr=[]
for j in range(0,9):
    array=list(range(6+5*j,11+5*j))
    array += list(range(51+5*j, 56+5*j))
    arr.append(array)
print(arr)