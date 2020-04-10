import pandas as pd
from pandas import ExcelWriter
import math
import sys

# 5/3/1 is a workout program where your loads are based on a percentage of your one rep max for four exercises: the squat, deadlift, bench press and overhead press.
# This program will ask a user for their best rep max, be it one rep or more, and will calculate the loads for their workouts, and create a spreadsheet containing their workout.
# There are two other functions. One allows the user to specify the plates they have available to them. The second will tell the user what plates they need on either side of the bar
# in order to load the correct amount of weight.

# The exercise class. Takes the following paramaters:(name of the exercise, max reps, max weight, unit).
# Unit, wee is optional, will default to KG if nothing is specified.
class exercise:

    def __init__(self, name, reps, weight, unit='kg'):
        self.name = name.title()
        self.reps = reps
        self.weight = weight
        self.one_rep = math.floor(self.weight * (1 + (self.reps / 30)))
        self.training_max = math.floor(self.one_rep * .90)
        self.unit = unit
        percentages = [.65, .75, .85, .70, .80, .90, .75, .85, .95, .40, .50, .60]
        self.weights = [round (percentage * self.training_max) for percentage in percentages]
        weeks_list = ['Week ' + str(week + 1) for week in range(4)]
        sets_dict = {"Set " + str(set + 1): 0 for set in range(3)}
        self.workout_dict = {week: dict(sets_dict) for week in weeks_list}

    # Automatically creates a workout for the exercise object in multiple formats.
    def create_workout(self, output='dataframe'):
        reps = ['x5', 'x5', 'x5', 'x3', 'x3', 'x3', 'x5', 'x3', 'x1', 'x3', 'x3', 'x3']
        # Function that adjusts the second level dictionary containing the sets, from the top level dictionary self.workout_dict
        def change_val(dictionary_this, i_this, reps_i_this, reps):
            # Loops through the nested dictionary, the weights values, and the reps list and adds one at a time.
            for key, weight, rep in zip(dictionary_this.keys(), self.weights[i_this: i_this + 3], reps[reps_i_this: reps_i_this + 3]):
                    # print (f'Key = {key}. Weight = {weight}. Rep = {rep}')
                dictionary_this[key] = str (weight) + reps[reps_i_this]
            return dictionary_this

        # Sets the index values to be inputted into the recursive change_val function.
        i = -3
        reps_i_this = -3

        # Loops through the key values for the highest level dictionary.
        for week in self.workout_dict.keys():
            # modifies the index values to be inputted into the recursive change_val function.
            i+= 3
            reps_i_this +=3
                # print (f'\nFor loop: This is {week}, i_this is {i}, weights are {self.weights[i : i + 3]}, they key being used is {week}, the reps index is {reps_i_this}')
            # Updates the values in the dictionary.
            self.workout_dict[week] = change_val(self.workout_dict[week], i, reps_i_this, reps)
                # print (f'The values for {week} are {self.workout_dict[week]}')

            # Returns the workout as either a dataframe or a dictionary
            dataframe = pd.DataFrame.from_dict(self.workout_dict).rename_axis(str(self.name) + ' Workout', axis=1)
            dictionary = self.workout_dict
        # Depending on the output specified when the method was called, will return the workout as either a dataframe, dictionary or both.
        if output.lower() == 'dataframe':
            return dataframe
        elif output.lower() == 'dictionary':
            return dictionary
        elif output.lower() == 'both':
            return dictionary, dataframe

    # This returns the string when the object is printed.
    def __str__(self):
        return f'Your calculated one rep max is {self.one_rep} and your training max is {self.training_max} based on your best {self.name} of {self.reps}x{self.weight}{self.unit}'

# Function to allow user to create their 5/3/1 workout via manual text input in the terminal.
    # Objects are created by the user in the process of the function.
def create_exercise_objects_with_input():
    # Function creates an 'exercise-object' for each of the four exercises in the program by asking the user for certain information regarding each exercise.
    def create_exercise_object(exercise_name):
        # Creating an exercise-object.
        try:
            # Takes an input from the user in the format reps x weight. Splits the input into 2 variables on the 'x'.
            print (f'Enter your best reps & weight for the {exercise_name}')
            reps, weight = input().split('x')

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

# Function to check with user if they would like a spreadsheet during creation via text
def ask_for_spreadsheet():
    question = '\nWould you like to create a spreadsheet with your workouts?\n'
    stars = '*' * len(question)
    print (stars + question + stars)
    answer = input("Enter 'Y' or 'N'\n").lower()
    if answer.lower() == 'y':
        return True
    if answer.lower() == 'n':
        return False
# Creates a spreadsheet with seperate sheets containing the workouts for each exercise.
def create_workout_spreadsheet(list_of_exercises):
    # Can modify the file name output.
    file_name = '531 Workout.xls'
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    with ExcelWriter(file_name) as writer:
        for exercise in list_of_exercises:
            exercise_workout_dataframe = exercise.create_workout()
            # Write each dataframe to a different worksheet.
            exercise_workout_dataframe.to_excel(writer, sheet_name=str(exercise.name) + ' Workout')
        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        output = 'Your workout has been saved as {FILE_NAME}. Enjoy!'.format(FILE_NAME=file_name)
        print('-' * len(output))
        print (output)
        print ('-' * len(output))

