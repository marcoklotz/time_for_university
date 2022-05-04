def time_for_university():
    ects_sum = 0
    ects_sum = int(input("How many ECTS do you want to gain this semester?: "))
    for i in range(0, ects_sum):
        if ects_sum < 30:
            print("This degree might take you longer than planed! ")
        elif ects_sum == 30:
            print("You are right on track to finish your studies on time! ")
        else:
            print("Very good! ")

def total_hours_per_week():
    time_per_ects = 30  # amount of hours per ECTS
    weeks_per_semester = 13
    total_time_spent = (ects_sum * 30)/13
    print("You have to put in {total_time_spent} hours per week", end='' )

if __name__== "__time_for_university__":
    time_for_university()