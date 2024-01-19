################ Function Definitions ################
print("Class Report Cards")
print("")

#Greet the User and Show Options
print("Hello! What Would You Like To Do Today?")
print("Please Select From The Following Options:")
print("")

def displayMenu():

#Option to Add a Student
  print("1. Add a Student")

# Option to Remove a Student
  print("2. Remove a Student")

# Option to Add a Students' Quiz Grade
  print("3. Add Quiz Grade for Student")

# This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  #Exit the Program
  print("6. Quit")
  
  # Prompts the user to enter a numeric grade
def getNumberGradeFromUser():
    val = None
    while val is None:
      try:
        test = float(input("Enter a Grade: "))
        val = test
      except:
        val = None
    return val
  #Define each letter grade with a numerical range 
def lettergrade (grade):
      if grade >= 90:
          return 'A'
      elif grade >= 80:
          return 'B'
      elif grade >= 70:
          return 'C'
      elif grade >= 60:
          return 'D'
      else:
          return 'F'

################ Main Program ################

# Create a dictionary of names and grades in a key value pair
students = {'Rachael':[92, 86, 71, 88], 'Katherine':[85, 74, 91], 'Sam':[82, 80, 52, 77], 'Brandon':[76, 94, 57, 91], 'Raisa':[55, 95, 88, 78]}

displayMenu()
print("")
choice = input('Select an Option: ')
# Application Loop
while choice != '6':
 # Enter a student's name to add it to the roster 
  if choice == '1':
    name = input('Enter student name: ')
    students[name] = []
    print(f'{name} added!')
# Enter a student's name to remove it from the roster    
  elif choice == '2':
    name = input('Enter student name: ')
    if name in students:
      del students[name]
      print(f'{name} removed!')
    else:
      print(f'{name} is not in the gradebook!')
 # Enter a student's name to add a quiz grade to their list of grades
  elif choice == '3':
    name = input('Enter student name: ')
    if name in students:
      grade = getNumberGradeFromUser()
      students[name].append(grade)
      print(f'{grade} has been added to {name}\'s quiz grade!')
    else:
      print(f'{name} is not in the gradebook!')
 # Enter the student's name a get a list of their quiz grades 
 # ...
  elif choice == '5':
    name = input('Enter student name: ')
    if name in students:
      gpa = sum(students[name]) / len(students[name])
      letter = lettergrade(gpa)
      print(f'{name} has a grade of {letter}')
    else:
      print(f'{name} is not in the gradebook!')
  print()
  displayMenu()
  choice = input('Select an Option: ')
print('Gradebook is now closed')