first_indentation_counter = 0
second_indentation_counter = 0
third_indentation_counter = 0
fourth_indentation_counter = 0
fifth_indentation_counter = 0

for i in range (0,5):
    print ("First Indentation".format(first_indentation_counter))
    for j in range (0,3):
        print ("Second Indentation".format(second_indentation_counter))
        for k in range (0, 10):
            print ("third indentation".format(third_indentation_counter))
    print ("Forth indentation".format(fourth_indentation_counter))
print("fifth indentation".format(fifth_indentation_counter))

