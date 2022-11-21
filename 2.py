def no_of_occ(str1,str2):
    last_char =str2[len(str2)-1]
    count=0
    
    for i in range(len(str1)):
        if(str1[i] == last_char):
            count+=1
    print(count)


no_of_occ('going to go to goa','go')