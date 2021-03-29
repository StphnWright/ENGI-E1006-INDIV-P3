**ENGI E1006 - Intro to Computing for Engineers & Applied Scientists**

You are welcome to discuss the problems with other students but the code you submit for take-home projects must be
your own work. Please review the academic honesty policy for this course (at the end of the syllabus page).

Do not use Python modules other than those explicitly mentioned. 

Upload the following file to Courseworks:

project3.py

**Farmers Market Database (100 pts)**

Download the file markets.txt which contains geographic information for over 7000 farmers markets in the US
(source http://explore.data.gov/d/wfna-38ey). Each line contains information about one farmers market. Data fields are
separated by a single "#" symbol. The fields are (in this order): state, market name, street address, city, zip code,
longitude, latitude.

Your task is to write a tool that lets users search for farmers markets in their town or zip code. Download and complete
the skeleton file project3.py.

a) Write the function read_markets(filename) that, given a filename, opens the file in the format described and reads in
the data. Each farmers market should be represented as a tuple of 5 strings. You should ignore the longitude and latitude entries.

The function should return two objects (i.e. a tuple of length 2):

  1) A **dictionary** mapping zip codes (keys) to **lists** of farmers market tuples (values)
  2) A **dictionary** mapping towns (keys) to sets of zip codes (values). Think about why it makes sense to use a set of
  zip codes instead of a list.

b) Write a function print_market(market) that takes a farmers market tuple as its parameter and returns a human-readable
string. Use string formatting to return the string. Despite the name, this function should not print the information. Just
return a formatted string. Here is an example: 

    Columbia University Greenmarket
    E. Side of Broadway between 114th & 115th Streets
    New York, New York 10027
    
c) Write the main program that first reads in the markets.txt once (using the function from part (a)), and then asks the user
repeatedly to enter a zip code or a town name (in a while loop until the user types “quit”). For each request, the program should
print all farmers markets for this town or zip code (using the function from part (b)). If town names are ambiguous (because the
town name exists in multiple US states), all entries should be printed. If a zip code or town name does not exist, the program should
print "Not found."

Hints: 

  You need to verify if the user input is a zip code (i.e. contains only numbers). If so, simply print all farmers markets in that
  zip code. If the user typed in the name of a town, loop over all zip codes for this town name and then use a nested loop to print
  all farmers markets for each zip code.
  
  The data set is messy -- there are entries with missing zip codes and other missing information. You can mostly ignore these for the
  purpose of the assignment. Your program should still work for entries that are correctly formatted in the file.
