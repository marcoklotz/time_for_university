def main():
    ects_sum = (input('How many ECTS do you want to gain this semester? ')
    int time_per_ects = 30 #amount of hours per ECTS
    int weeks_per_semester = 13

    for i in range(0, ects_sum):
        if ects_sum < 30:
            print('This degree might take you longer than planed! ')
        elif ects_sum == 30:
            print('You are right on track to finish your studies on time! ')
        else:
            print('Very good! ')

    total_time_spent = float
    total_time_spent = (ects_sum * time_per_ects)/weeks_per_semester

    print('You have to put in' + total_time_spent + 'hours per week' )