def chekStudentSuccess(name, score):
    if score >= 90:
        print(f'{name} has excellent lecel')
    elif 75 <= score < 90:
        print(f'{name} has good level')
    elif 60 <= score < 75:
        print(f'{name} has normal level')
    else:
        print(f'{name} has poor level')

def chekPupilSeccess(name,score):
    if score >= 10:
        print(f'{name} has excellent lecel')
    elif 7 <= score < 10:
        print(f'{name} has good level')
    elif 4 <= score < 7:
        print(f'{name} has normal level')
    else:
        print(f'{name} has poor level')
