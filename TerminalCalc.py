#Function for BODMAS calculations - takes a string as input involving NO brackets 
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


def bodmas (nobracket_str):
    
    i=0
    j=0
    k=0
    p=0
    while(i<len(nobracket_str)): #This will remove all the division operators '/' after solving them 

        if (nobracket_str[i] == '/') :

            nobracket_str = Calculate_string(nobracket_str , i)
            
            i=0

        i+=1

    while(j<len(nobracket_str)): #This will remove all the multiplication operators '*' after solving them

        if (nobracket_str[j] == '*') :

            nobracket_str = Calculate_string(nobracket_str , j)
            
            j=0

        j+=1
    
    while(k<len(nobracket_str)): #This will remove all the addition operators '+' after solving them

        if (nobracket_str[k] == '+') :

            nobracket_str = Calculate_string(nobracket_str , k)
            
            k=0

        k+=1
    
    while(p<len(nobracket_str)): #This will remove all the subtraction operators '-' after solving them

        if (nobracket_str[p] == '-') :

            nobracket_str = Calculate_string(nobracket_str , p)
            
            p=0
        
        p+=1
    

    return nobracket_str
    

op_string = input ('''Enter the full operation to be performed -
                          Make sure to use the correct operators as follows :
                          / ---> for division
                          * ---> for multiplication
                          + ---> for addition
                          - ---> for subtraction
                          
                          Enter the operation here :- ''')


print ("The output of the full operation according to BODMAS is ===>", bodmas(op_string))




