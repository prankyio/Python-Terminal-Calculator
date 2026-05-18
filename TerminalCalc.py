#Function for performing the BODMAS calculations - takes a string(involving NO brackets) and operator's index as input 
def Calculate_string ( nobracket_str , oi ):  #oi = operator index    

    prev_oi =0
    next_oi=0

    #Calculating Left_num
    for i in range (oi-1 ,-1 , -1):

        if (nobracket_str[i] == '/' or nobracket_str[i] == '*' or nobracket_str[i] == '+' or nobracket_str[i] == '-') :
            
            prev_oi = i

            break;
    if prev_oi == 0 :
        left_num = float(nobracket_str[0:oi])
    else:
        left_num = float(nobracket_str[prev_oi + 1 : oi])

    #Calculating Right_num
    for i in range (oi+1 , len(nobracket_str), 1):

        if (nobracket_str[i] == '/' or nobracket_str[i] == '*' or nobracket_str[i] == '+' or nobracket_str[i] == '-') :
            
            next_oi = i

            break;
    if next_oi == 0 :
        right_num = float(nobracket_str[oi+1:len(nobracket_str)])
    else:
        right_num = float(nobracket_str[oi + 1 : next_oi])



    #performing the operation

    if nobracket_str[oi] == '/':

        result = left_num/right_num 
    
    if nobracket_str[oi] == '*':

        result = left_num*right_num

    if nobracket_str[oi] == '+':

        result = left_num+right_num

    if nobracket_str[oi] == '-':

        result = left_num-right_num


        #👇FINAL MODIFIED STRING INCLUDING THE RESULT OF THE OPERATION PERFORMED👇

    if prev_oi!=0 and next_oi!=0 :

        output_str = nobracket_str[0:prev_oi+1] + str(result) + nobracket_str[next_oi : len(nobracket_str)]
    
    elif prev_oi == 0 and next_oi!=0:

        output_str = str(result) + nobracket_str[next_oi : len(nobracket_str)]
    
    elif prev_oi!=0 and next_oi == 0:

        output_str = nobracket_str[0:prev_oi+1] + str(result)

    elif prev_oi == 0 and next_oi == 0:

        output_str = str(result)
    
    # DEBUG CODE -- print("Leftnum =>" , left_num , "Rightnum =>", right_num , "outputstr=>", output_str,"\n")
    
    
    return output_str


#Function which decides the order of operations - takes a string(involving NO brackets) as input 
def bodmas (nobracket_str):
    
    i=0
    k=0

    while(i<len(nobracket_str)): #This will remove all the division'/' and multiplication'*' operators after solving them 

        if (nobracket_str[i] == '/' or nobracket_str[i] == '*') :

            nobracket_str = Calculate_string(nobracket_str , i)
            
            i=0

        i+=1

    while(k<len(nobracket_str)): #This will remove all the addition'+' and subtraction'-' operators after solving them

        if (nobracket_str[k] == '+' or nobracket_str[k] == '-') :

            nobracket_str = Calculate_string(nobracket_str , k)
            
            k=0

        k+=1
    

    return nobracket_str
    

#Function to Solve And remove brackets 
def BracketSolver(fullstring):

    Br_list=[0]

    while(Br_list!=[]): #Outer_loop

        Br_list=[]
        j =0
        skip_outer=False


        for i in range(0,len(fullstring)): #Creating New Br_list for modified fullstring in each iteration

            if fullstring[i] in ("{" , "}" , "[" , "]" , "(" , ")" ):

                Br_list.insert(j , [fullstring[i],i] )
                j+=1


        #Solving & Removing the closest/Smallest bracket Precedence wise, {} 👉 [] 👉 ()

        '''
            📌 Br_list[i][0] and Br_list[i+1][0] used to check whether 
                opening and closing brackets are adjacent or not (i.e there is no other bracket between them)
            
            📌 Br_list[i][1] and Br_list[i+1][1] are used to access the indexes of those 
                opening and closing brackets IN THE fullstring
            
        '''
        
        for i in range(0,len(Br_list)):

            if Br_list[i][0] == "{" and Br_list[i+1][0]=="}" : 

                 result = bodmas (fullstring[ Br_list[i][1]+1  : Br_list[i+1][1]  ])

                 fullstring= fullstring[0 : Br_list[i][1] ] + result + fullstring[ Br_list[i+1][1]+1 : ]
                 skip_outer = True
                 break

        if skip_outer:
            continue
        
        for i in range(0,len(Br_list)):

            if Br_list[i][0] == "[" and Br_list[i+1][0]=="]" :

                 result = bodmas (fullstring[ Br_list[i][1]+1  : Br_list[i+1][1]  ])

                 fullstring= fullstring[0 : Br_list[i][1] ] + result + fullstring[ Br_list[i+1][1]+1 : ]
                 skip_outer= True
                 break
        
        if skip_outer:
            continue
        
        for i in range(0,len(Br_list)):

            if Br_list[i][0] == "(" and Br_list[i+1][0]==")" : 

                 result = bodmas (fullstring[ Br_list[i][1]+1  : Br_list[i+1][1]  ])

                 fullstring= fullstring[0 : Br_list[i][1] ] + result + fullstring[ Br_list[i+1][1]+1 : ]
                 skip_outer= True
                 break

        if skip_outer:
            continue
    
    

    if Br_list==[] :
            return bodmas(fullstring)
        



op_string = input ('''Enter the full operation to be performed -
                          Make sure to use the correct operators as follows :
                          / ---> for division
                          * ---> for multiplication
                          + ---> for addition
                          - ---> for subtraction
                          
                          AND 
                          
                          Correct brackets as follows:
                          {} ---> for braces {curly brackets}
                          [] ---> for square brackets
                          () ---> for parantheses
                          
                          Enter the operation here :- ''')


print ("The output of the full operation according to BODMAS is ===>", BracketSolver(op_string))




