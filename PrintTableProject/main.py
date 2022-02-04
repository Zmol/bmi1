tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# 4
numLists = (len(tableData[1]))

# def printTable():
#   for i in numLists:
#      numLists[i] =

# [0][0][0]
#colWidths = [0] * len(tableData)
colWidths = [8,5,4]
colWidthsMax = max(colWidths, key=len)
print(colWidthMax)
for sublst in tableData:
    for items in sublst:
        print()

for sublst in tableData:
    print(len(sublst))
    colWidths[0]=int(max(sublst, key=len))

# print(a)
print(colWidths)

#def get_max_str(lst):
#    return(max(lst, key=len)

 #get_max_str(tableData)


#for sublst in tableData:
#    print(len(sublst))
#    for item in sublst:
#        if len(item) > a:
#            a = len(item)
#    print(sublst)
