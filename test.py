# def chekStudentSuccess(name, score):
#     if score >= 90:
#         print(f'{name} has excellent lecel')
#     elif 75 <= score < 90:
#         print(f'{name} has good level')
#     elif 60 <= score < 75:
#         print(f'{name} has normal level')
#     else:
#         print(f'{name} has poor level')
#
# def chekPupilSeccess(name,score):
#     if score >= 10:
#         print(f'{name} has excellent lecel')
#     elif 7 <= score < 10:
#         print(f'{name} has good level')
#     elif 4 <= score < 7:
#         print(f'{name} has normal level')
#     else:
#         print(f'{name} has poor level')

userLogs = ['admin','user123','student4']
userBYears = [2000,2010,2005]

def listMaker1(myList):
    result = []
    for item in myList:
        result.append(item.title())
    return result

def listMaker2(myList):
    result = []
    for item in myList:
        result.append(2023-item)
    return result

newList1 = listMaker1(userLogs)
newList2 = listMaker2(userBYears)
print(newList1)
print(newList2)