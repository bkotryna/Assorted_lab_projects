import sys, os
os.chdir('C:\Kotryna\Asmen\Python\csv file handling')
cwd = os.getcwd()
print("cwd is: ", cwd)

# open a .csv file
import pandas as pd
file1 = pd.read_csv('file1.csv')

#sort the data based on name - machine - date
sorted_file1 = file1.sort_values(['name','machine', 'date', 'duration'],ascending=[True,True,True,True])
print(sorted_file1)

# extract unique people's names into a list
unique_names = sorted_file1['name'].unique().tolist()
print(unique_names)
unique_machines = sorted_file1['machine'].unique().tolist()
print(unique_machines)

prices = {"Dragon":10, "Dinosaur":100}

# select rows that have a particular person's name
# store these new dataframes in a list
list_by_person = []
for i in unique_names:
    a = sorted_file1[sorted_file1["name"] == i]
    list_by_person.append(a)
#print(list_by_person[0])

# access new per_person dataframes one by one and do lots of things to them
for number in range(len(list_by_person)):

    person_data = list_by_person[number].reset_index()
    person_data = person_data.drop("index", axis=1)
    print(person_data)
    # retrieve the name of the example case
    person_name = person_data["name"].unique().tolist()
    output_name = person_name[0]
    print(output_name)
    
    # group by machine and return total duration for each machine
    person_data.groupby(['machine'])['duration'].sum()
    #print(person_data.groupby(['machine'])['duration'].sum())
    dict_by_machine = {}
    for i in unique_machines:
        a = person_data[person_data["machine"] == i]["duration"].sum().tolist()
        dict_by_machine.update({i:a})
    print(dict_by_machine)    
    
    # calculate price per machine for the person
    price_per_machine = {}
    for machine in dict_by_machine:
        a = prices[machine]
        b = dict_by_machine[machine]
        c = a*b
        price_per_machine.update({machine:c})
    print(price_per_machine)
    
    # calculate total for the person
    total = 0
    for machine in price_per_machine:
        total += price_per_machine[machine]
    output_total = total
    print(output_total)


    # just to test, make a csv file for each person
        
    # make a file name that informs of the person's name
    filename = "data_from_" + str(output_name) + ".csv"
    print(filename)
    
    # append a blank row to the dataframe
    blank_row = ["---", "---", "---", "---"]
    person_data.loc[len(person_data)] = blank_row
    print(person_data)
    
    # append cost per machine and total cost to the dataframe    
    for machine in unique_machines:
        new_row = ["price per machine", machine, "GBP", price_per_machine[machine]]
        print(new_row)
        person_data.loc[len(person_data)] = new_row
        #print(person_data)
    
    print(person_data)
    print(len(person_data))

    # append a blank row to the dataframe    
    person_data.loc[len(person_data)] = blank_row

    # append row with total price to pay for the person
    total_row = ["total for all machines","","GBP", output_total]
    print(total_row)
    
    person_data.loc[len(person_data)] = total_row
    print(person_data)

    # write out the file
    person_data.to_csv(filename, index = False)




