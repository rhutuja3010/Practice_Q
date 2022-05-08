unique=[]
EMP=[]
sub={}
i=1
while i<=5:
    submission_time=input("YYYY:MM:DD HH:MM:SS EM00:----")
    
    if submission_time>="2020:08:01 09:00:00" and submission_time<="2022:12:31 17:30:00":
        
        if submission_time not in unique:
            
            unique.append(submission_time)
            
            print(unique)
    else:
        print("sorry,,,Your submission time out ")    
    i+=1



# unique=[]
# m=[]
# sub={}
# i=1
# while i<=5:
#     submission_time=input("YYYY:MM:DD HH:MM:SS EM00:----")
#     meatting_start_time=input("YYYY:MM:DD HH:MM:SS:.....")
#     if submission_time>="2020:08:01 09:00:00" and submission_time<="2022:12:31 17:30:00":
        
#         if submission_time not in unique:
            
#             unique.append(submission_time)
#             m.append(meatting_start_time)
#             print(unique,"\n",m)
#     else:
#         print("sorry,,,Your submission time out ")    
#     i+=1

