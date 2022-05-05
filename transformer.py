##-IMPORTS-##

#import pyodbc 

import sys
import json

'''



 to connect with sql we need to - 

import pyodbc

and repalce  with open(sys.argv[-2],'r') as data: 

with 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=database_name;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

same for the second transform 

'''

##-- Transform functions Start --##
##--first transform function  to capitalize first letter--##

def captial_first_letter(file_name):
    
    output=""
    
    for line in file_name:
    
        output += line.title()
        #print(output)
    
    f = open('Output_first_Transform.txt','w')
    
    
    ##--Write the data into output.txt--##

    f.write(output)

    
    
    ##--another approch in which we put text file to list and then do the capitalize operation--##
    
    """
    intia_list = []
    final_list = []

    for  line in file_name:
        line_strip = line.strip()
        line_Split = line_strip.split()
        intia_list.append(line_Split)
    
    
    for i in intia_list:
        for j in i:
            final_list.append(j)
            
    
    L_upper = [i.capitalize() for i in final_list]
    #print(L_upper)    
    #print(g)
    le =  len(final_list)
    f = open('output.txt','w')
    for i in range (0,le):
        f.write(L_upper[i]+"  ")
    """
    
    
    
##-- second transform function to frequrncy  of words --##

def freq_of_words(file_name):
    d1 = dict()
    for line in file_name:
        words = line.split()
        for word in words:
            if word in d1:
                d1[word] = d1[word]+1
            else:
                d1[word] = 1
    
    
    f = open('Output_second_Transform.txt','w')
    
    ##--Write data into Output_second_Transform--##
    f.write(json.dumps(d1))
                
    


##-- End of Transform functions--##
    
if __name__ == '__main__':
    
    ##--Load the file to transform for 1st fucntion--##
    with open(sys.argv[-2],'r') as data:
        
        ##--function call to capitalize first letter--## 
        captial_first_letter(data)
        print("Your file has been created check the directory for Output_first_Transform.txt")
        
    ##--Load the file to transform for 2nd fucntion--##
    with open(sys.argv[-1],'r') as data:
        
         ##--function call to frequency  of words--## 
        freq_of_words(data)
        print("Your file has been created check the directory for Output_second_Transform.txt")
