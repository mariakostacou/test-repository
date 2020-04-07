a_list = [10, 12, 14, 14, 16, 28, 28, 30]
def removeDuplicates(ex_list):
    new_list=[]
    for item in ex_list:
        if item not in new_list:
            new_list.append(item)
    return(new_list)
a_list = removeDuplicates(a_list)
print(a_list)
def sortList(ex_list):
    for i in range(len(ex_list)):
        for j in range(0,len(ex_list)-i-1):
            if ex_list[j]<ex_list[j+1]:
                swap=ex_list[j]
                ex_list[j]=ex_list[j+1]
                ex_list[j+1]=swap
    return(ex_list)
sorted_list=sortList(a_list)
print(sorted_list)

a_dict= {"a":10, "b":12, "c":14, "d":14, "e":16, "f":28, "g":28, "h":30}
def removeDuplicatesDict(ex_dict):
    new_dict={}
    for key,item in ex_dict.items():
        if item not in new_dict.values():
            new_dict[key]=item
    return(new_dict)
a_dict=removeDuplicatesDict(a_dict)
print(a_dict)

def sortDict(ex_dict):
    for i in range(len(ex_dict.items())):
        for j in range(0,len(ex_dict.items())-i-1):
            if ex_dict.items(j)<ex_dict.items(j+1):
                swap=ex_dict.items(j)
                ex_dict.items(j)=ex_dict.items(j+1)
                ex_dict.items(j+1)=swap
    return(ex_dict)

sorted_dict=sortDict(a_dict)
print(sorted_dict)
             

