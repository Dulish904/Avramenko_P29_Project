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
#
# userLogs = ['admin','user123','student4']
# userBYears = [2000,2010,2005]
#
# def listMaker1(myList):
#     result = []
#     for item in myList:
#         result.append(item.title())
#     return result
#
# def listMaker2(myList):
#     result = []
#     for item in myList:
#         result.append(2023-item)
#     return result

class Student:
    spec = 'Python'
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1=Student("Bob", 21)
student2=Student("Anya", 22)
print('Info about 1 studen')
print(student1.name)
print(student1.age)

print('Info about 2 studen')
print(student2.name)
print(student2.age)
