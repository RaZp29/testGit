#Reading CSV files

import csv

with open('example.csv') as csvfile:
#with open('Arbetsbok1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)

''''Above, we've shown how to open a CSV file and read each row, as well as reference specific data on each row.

Next, we will show how to pull out specific data from the spreadsheet and save it to a list variable:
'''
print
'''
with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    # now, remember our lists?

    whatColor = input('What color do you wish to know the date of?:')
    coldex = colors.index(whatColor)
    theDate = dates[coldex]
    print('The date of', whatColor, 'is:', theDate)
'''

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    '''
    try:
        whatColor = input('What color do you wish to know the date of?:')
        coldex = colors.index(whatColor)
        theDate = dates[coldex]
        print('The date of',whatColor,'is:',theDate)

    # in python 2, this is read exception Exception, e. It's just helpful
    # to know this for porting old scripts if you need to.


    except Exception as e:
        print(e)
        

    # So this will try a block of code, and, if there is an exception, it
    # will continue to run...
    
    print('Stillllllll running though!')
    '''


    # we could put the try anywhere. The weak point, however, starts
    # in my opinion immediately when we accept user input... no longer
    # is this is a closed-program, so I would personally code this block
    # here, but you could put the try right about the print statement
    # of where we search for the color and we KNOW it will throw an error
    # if not in the list.
    try:
        whatColor = input('What color do you wish to know the date of?:')

        if whatColor in colors:
            coldex = colors.index(whatColor)
            theDate = dates[coldex]
            print('The date of',whatColor,'is:',theDate)
        else:
            # now we can handle a specific scenario, instead
            # of handling it with a "catch-all" error.
            # now we have error handling and
            # proper logic. Yay.
            print('This color was not found.')

    # in python 2, this is read exception Exception, e. It's just helpful
    # to know this for porting old scripts if you need to.


    except Exception as e:
        print(e)
        


