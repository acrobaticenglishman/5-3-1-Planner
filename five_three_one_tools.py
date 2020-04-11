import math

# Recursive function to calculate which plates and how many you will need to add to one side of the bar based on a target weight.
def weight_plate(weight_plate_list_this, weight_target_this, weight_plate_index_this, plates_final_list_this, units='kg', bar = 0):

    # Subtracts the weight of half the bar from the calculation. By default the bar weight is 20. Because I'm english and we use KG not freedom units. Get with it America.
    weight_target_this = weight_target_this - (bar / 2)

    # Translates the final string output to be in 'lbs' instead of kg.
    # If anything other than 'lbs' or 'kg' is entered, will default to kg.
    if units == 'lbs':
        units = 'lbs'
    else:
        units = 'kg'

    # Gets the number of plates needed for the current weight.
    plate_needed_this = math.floor(weight_target_this / weight_plate_list_this[weight_plate_index_this])
    # Resets the value of 'weight_target_this' to be minus the value of the plates we've already found.
    weight_target_this = weight_target_this - (weight_plate_list_this[weight_plate_index_this] * plate_needed_this)

    # Appends the value of the plate to a list once for every plate needed.
    for i in range(plate_needed_this):
        plates_final_list_this.append(weight_plate_list_this[weight_plate_index_this])

    # Logic to make plate plural or singular based on the value of 'plates_needed_this'.
    # output_line_ending = ' plates on each side.'
    # if plate_needed_this == 1:
    #     output_line_ending = ' plate on each side'
    # if plate_needed_this >= 1:
    #     print ('You will need {X} {PLATE}{UNIT}'.format(
    #         X=plate_needed_this,
    #         PLATE = weight_plate_list_this[weight_plate_index_this],
    #         UNIT = units)
    #         + output_line_ending)

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
    output = '\nYou will need the following plates on each side of the bar: ' + str (plates_final_list_this) + '\n'
    stars = len (output) * '*'
    return plates_final_list_this

# Takes an input from the user to generate a list of weights they have available to them.
def define_weight_plate_list():
    print ("Please enter the weights you have available to you in this format: 25, 20, 10 \nSeperate each weight with a ,")
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

    return list_of_weights

# Function to be passed to the main script to iniate the weight plate calculator, and to have the user input the relevant arguments.
def call_weight_plate():
        message = '\nOk! Couple questions!\n'
        lines = len(message) * ('-')
        print(lines + message + lines)
        target_weight = input('What is your target weight including the weight of the bar? ')
        print('What unit is that? Answer kg or lbs')
        unit_of_choice = input()
        print ('And how much does the bar weigh?')
        bar_weight = int (input())
        print('Do you want to specify what plates you have available to you?\nAnswer y or n')
        answer = input()
        plates_final_list = []
        if answer == 'y':
            weight_plate_list = define_weight_plate_list()
        elif answer == 'n':
            weight_plate_list = [45, 25, 20, 15, 10, 5, 2.5]
        final_weight_plate_list = weight_plate(weight_plate_list_this=weight_plate_list,
                                weight_target_this=int(target_weight) / 2,
                                weight_plate_index_this=0,
                                plates_final_list_this=plates_final_list,
                                units=unit_of_choice,
                                bar=bar_weight)
        final_weight_plate_list = [str (weight) + str(unit_of_choice) for weight in final_weight_plate_list ]
        output = 'You will need the following plates on each side of the bar:'
        print (output, final_weight_plate_list)
