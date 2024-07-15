#Create a list and turn it into a global variable where they can be
#  printed outside. Get list of all the cohort and loop into it and append more cohorts into the list.


# Define a global list for cohorts
cohort_list = ["Cohort 13", "Cohort 14", "Cohort 30"]

def add_cohort(cohort_name):
    global cohort_list  # Access the global cohort list
    cohort_list.append(cohort_name)

def add_more_cohorts(new_cohorts):
    global cohort_list  # Access the global cohort list
    for cohort in new_cohorts:
        cohort_list.append(cohort)

# Function to print all cohorts
def print_cohorts():
    global cohort_list  # Access the global cohort list
    print("List of all cohorts:")
    for cohort in cohort_list:
        print(cohort)

# Add more cohorts to the list
more_cohorts = ["Cohort 17", "Cohort 15", "Cohort 18"]
add_more_cohorts(more_cohorts)

# Print all cohorts
print_cohorts()


# A global list cohort_list is defined.
# The add_cohort function allows adding a single cohort to the global list.
# The add_more_cohorts function takes a list of new cohorts and appends them to the global list.
# The print_cohorts function prints all cohorts in the global list.
# The more_cohorts list is created with additional cohort names, which are added to the global list using the add_more_cohorts function.
# Finally, the print_cohorts function is called to print the updated list of cohorts.