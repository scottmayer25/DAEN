# Perform the following problems using R:
# Create a vector of courses (e.g., MATH 101) you have taken previously. Make sure you have at least 8 courses. Name the vector myCourses
# Get the length of the vector myCourses
# Get the first two courses from myCourses
# Get the 3rd and 4th courses from myCourses
# Sort myCourses using a methods
# Sort myCourse in the reverse direction

myCourses <- c("DAEN 500", "CS 504", "OR 531", "AIT 580", "STAT 515", "BUS 300", "ECON 301", "MATH 203")

length(myCourses)

myCourses[1:2]

myCourses[3:4]

sort(myCourses)

sort(myCourses, decreasing = TRUE)
