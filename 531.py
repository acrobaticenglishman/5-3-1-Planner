import pandas as pd
from pandas import ExcelWriter
import math
import sys

# 5/3/1 is a workout program where your loads are based on a percentage of your one rep max for four exercises: the squat, deadlift, bench press and overhead press.
# This program will ask a user for their best rep max, be it one rep or more, and will calculate the loads for their workouts, and create a spreadsheet containing their workout.
# There are two other functions. One allows the user to specify the plates they have available to them. The second will tell the user what plates they need on either side of the bar
# in order to load the correct amount of weight.

# The exercise class. Takes the following paramaters:(name of the exercise, max reps, max weight, unit).
# Unit is optional, will default to KG if nothing is specified.
class exercise:

    def __init__(self, name, reps, weight, unit='kg'):
        self.name = name.title()
        self.reps = reps
        self.weight = weight
        self.one_rep = math.floor(self.weight * (1 + (self.reps / 30)))
        self.training_max = math.floor(self.one_rep * .90)
        self.unit = unit
    # This returns the string when the object is printed.

    def __str__(self):
        return 'Your calculated one rep max is {ONE_REP_MAX} and your training max is {TRAINING_MAX} based on your best {EXERCISE_NAME} of {REPS}x{WEIGHT}{UNIT}'\
            .format(ONE_REP_MAX=self.one_rep,
                    TRAINING_MAX=self.training_max,
                    EXERCISE_NAME=self.name,
                    REPS=self.reps,
                    WEIGHT=self.weight,
                    UNIT=self.unit)

    def create_workout(self):
        # 5/3/1 is a four week program. With 3 sets per workout with varying loads based on a percentage of your training max.
        # Your training max is 90% of your one rep max.
        weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
        sets = ['Set 1', 'Set 2', 'Set 3']
        initial_percentages = [.65, .75, .85, .70, .80, .90, .75, .85, .95, .40, .50, .60]
        workout = []
        full_workout = {'Week 1': [], 'Week 2': [], 'Week 3': [],'Week 4': []}

        # Creates a list containing all the weights for each week by multpiplying the exercise-objects training max value by the percentage for that set.
        # Casts those weights to a string, and adds the specified unit.
        for i in range(len(sets) * len(weeks)):
            weight = round(initial_percentages[i] * self.training_max)
            workout.append(str(weight) + str(self.unit))

        # Goes through the list of weights for each workout, and adds every set of 3 to the corresponding key for each week.
        # i.e first set of three values in workout become the value pairs for the week 1 key.
        for i, key in zip(range(0, 12, 3), full_workout):
            full_workout[key] = workout[i:i + 3]

        # returns a dataframe with the weeks as the columns and the corresponding weights.
        workout_title = (str (self.name) + ' Workout')
        # Creates a dataframe containing the data in the dictionary 'workout'.
        workout_dataframe = pd.DataFrame.from_dict(full_workout)
        # Adds the column 'sets' from the list 'sets'.
        workout_dataframe['sets'] = sets
        # Resets the index to use the 'sets' column.
        workout_dataframe = workout_dataframe.set_index('sets')
        # Returns the workout as a dataframe
        return workout_dataframe

# Manual creation of exercise objects.
    # If uncommented allows you to skip 'create_exercise_objects_with_input'
# squat = exercise('Squat', 1, 100)
# deadlift = exercise('Deadlift', 1, 100)
# bench = exercise('Bench', 1, 100)
# ohp = exercise('Overhead Press', 1, 100)

# Function to allow user to create their 5/3/1 workout if exercise objects do not already exist.
    # Objects are created by the user in the process of the function.
def create_exercise_objects_with_input():
    # Function creates an 'exercise-object' for each of the four exercises in the program.
    def create_exercise_object(exercise_name):
        # Creating an exercise-object.
        try:
            # Takes an input from the user in the format reps x weight. Splits the input into 2 variables on the 'x'.
            reps, weight = input(
                "Enter your best reps & weight for the {EXERCISE_NAME}: \n".format(
                    EXERCISE_NAME=exercise_name)).split('x')

            # Cast the inputted information to the needed types.
            exercise_name = str(exercise_name)
            reps = int(reps)
            weight = int(weight)

            # Returns an exercise object and prints the one rep and training max to the terminal.
            exercise_info = exercise(exercise_name, reps, weight)
            print (exercise_info)
            print ('-'  * len(str (exercise_info)))
            return exercise_info

        except ValueError:
            print("Sorry, that is not a valid rep & weight scheme. Please try again.")
            create_exercise_object(str(exercise_name))
    # List of exercises in the program.
    list_of_exercises = ['Squat', 'Deadlift', 'Bench', 'Overhead Press']

    print ('Hello there! Welcome to your 5/3/1 planner. The four exercises are Squat, Deadlift, Bench and Overhead Press. \n')
    print ("When entering your best reps and weight, please use the format 'reps' x 'weight'")

    exercise_name = list_of_exercises[0]
    squat = create_exercise_object(exercise_name)

    exercise_name = list_of_exercises[1]
    deadlift = create_exercise_object(exercise_name)

    exercise_name = list_of_exercises[2]
    bench = create_exercise_object(exercise_name)

    exercise_name = list_of_exercises[3]
    ohp = create_exercise_object(exercise_name)

    return squat, deadlift, bench, ohp

# Redundant
# Function to create 5/3/1 workout if exercise objects already exist.
def create_531_with_objects(squat, deadlift, bench, ohp):
    # Creates a dataframe containing the workout for each exercise.
    squat_workout = squat.create_workout()
    deadlift_workout = deadlift.create_workout()
    bench_workout = bench.create_workout()
    ohp_workout = ohp.create_workout()
    # Returns four dataframes
    return squat_workout, deadlift_workout, bench_workout, ohp_workout


# Takes an input from the user to generate a list of weights they have available to them.
def define_weight_plate_list():
    question = 'Would you like to specify the plates you have available to you?'
    print (question)
    answer = input("Enter 'Y' or 'N'\n").lower()
    print ('-' * len(question))
    if answer == 'y':
        print ("Please enter the weights you have available to you in this format: '25, 20, 10'. \nSeperate each weight with a ,")
        # Seperates the users input on the comma to create a list of weights.
        # Casts the individual elements of the list to an integer value.
        try:
            list_of_weights = input().split(',')
            for i in range (len (list_of_weights)):
                list_of_weights[i] = int(list_of_weights[i])
        # If there is an error on the users entry, the user can choose to either use the default values by entering '1'.
        # Or they can try again by entering '2'.
        # Any other input will restart from the beginning.
        except ValueError:

            print ("I'm sorry, something went wrong.")
            print ('Would you like to use the default values? [25, 20, 15, 10, 5, 2.5] or try again?')
            print ('For default values, please enter 1\nTo try again, please enter 2')
            answer = input('Enter 1 or 2\n')
            if answer == '1':
                list_of_weights = [25, 20, 15, 10, 5, 2.5]
            elif answer == '2':
                print ('\n')
                define_weight_plate_list()
            else:
                print ("\n" * 20 + "Sorry, something went wrong. Lets try again!")
                define_weight_plate_list()

        # Returns a list containing the chosen weights, sorted in descending order.
        list_of_weights.sort(reverse=True)
        return (list_of_weights)
    else:
        output = 'Ok, well thanks for using our 5/3/1 workout planner and happy training!'
        print (output + '\n' + '-' * len(output))
        sys.exit()

# Recursive function to calculate which plates you need to add to one side of the bar based on a given weight.
def weight_plate(weight_plate_list_this, weight_target_this, weight_plate_index_this, plates_final_list_this, units='kg', bar = 0):

    # Subtracts the weight of the bar from the calculation. By default the bar weight is zero. It has to be specified by the user.
    weight_target_this = weight_target_this - (bar / 2)

    # Translates the final string output to be in 'lbs' instead of kg. If anything other than 'lbs' or 'kg' is entered, will default to kg.
    if units == 'lbs':
        units = 'lbs'
    else:
        units = 'kg'

    # Takes the floor of the target weight, divides it by the current weight plate in the list to get the number of plates needed for the current weight.
    plate_needed_this = math.floor(weight_target_this / weight_plate_list_this[weight_plate_index_this])
    # Resets the value of 'weight_target_this' to be minus the value of the plates we've already found.
    weight_target_this = weight_target_this - (weight_plate_list_this[weight_plate_index_this] * plate_needed_this)

    # Appends the value of the plate to a list once for every plate needed.
    for i in range(plate_needed_this):
        plates_final_list_this.append(weight_plate_list_this[weight_plate_index_this])

    # Logic to make plate plural or singular based on the value of 'plates_needed_this'.
    output_line_ending = ' plates on each side.'
    if plate_needed_this == 1:
        output_line_ending = ' plate on each side'
    if plate_needed_this >= 1:
        print ('You will need {X} {PLATE}{UNIT}'.format(X=plate_needed_this, PLATE = weight_plate_list_this[weight_plate_index_this], UNIT = units) + output_line_ending )

    # Sets a condition to continue the recursion.
    ok_to_continue = True
    # Continues as long as the index being checked is not larger than the length of the entire list of plates.
    if ok_to_continue == True:
        ok_to_continue = weight_plate_index_this + 1 <= len(weight_plate_list_this)
    # Continues as long as the target weight is greater than zero.
    if ok_to_continue == True:
        ok_to_continue = (weight_target_this > 0)
    # If the ok_to_continue value is true, will re-run the function with the next item in the weight_plate_list.
    if ok_to_continue == True:
        weight_plate(weight_plate_list_this, weight_target_this, weight_plate_index_this + 1, plates_final_list_this, units, bar - bar)

    # Returns a list of the final weights needed.
    return plates_final_list_this

# Creates a spreadsheet with seperate sheets containing the workouts for each exercise.
def create_workout_spreadsheet(squat_workout, deadlift_workout, bench_workout, ohp_workout):
    question = 'Would you like to create a spreadsheet with your workouts?'
    print (question)
    answer = input("Enter 'Y' or 'N'\n").lower()
    print ('-' * len(question))
    if answer == 'y':
        file_name = '531 Workout.xls'
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        with ExcelWriter(file_name) as writer:
            # Write each dataframe to a different worksheet.
            squat_workout.to_excel(writer, sheet_name=str(squat.name) + ' Workout')
            deadlift_workout.to_excel(writer, sheet_name=str(deadlift.name) + ' Workout')
            bench_workout.to_excel(writer, sheet_name=str(bench.name) + ' Workout')
            ohp_workout.to_excel(writer, sheet_name=str(ohp.name) + ' Workout')
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            output = 'Your workout has been saved as {FILE_NAME}. Enjoy!'.format(FILE_NAME=file_name)
            print (output)
            print ('-' * len(output))
    if answer == 'n':
        output = 'Ok! No sweat!'
        print (output + '\n' + '-' * len(output))




# Order to run the program:

# First, create the exercise objects.
squat, deadlift, bench, ohp = create_exercise_objects_with_input()
# Second, create the workouts for each exercise object.
squat_workout, deadlift_workout, bench_workout, ohp_workout = squat.create_workout(), deadlift.create_workout(), bench.create_workout(), ohp.create_workout()
# Third, creates the spreadsheet containing the workouts.
create_workout_spreadsheet(squat_workout, deadlift_workout, bench_workout, ohp_workout)
# Lastly, ask the user if they want to move forward with the optional steps.
# Optional steps:
    # Have the user specify the plates available to them.
weight_plate_list = define_weight_plate_list()
    # User can specify a weight and be told the weight needed on either side.

# Empty Variable for weight_plate function
plates_final_list = []
output = 'You will need the following plates on each side: '
plates_final_list = (weight_plate(weight_plate_list, 100, 0, plates_final_list, bar=20))
