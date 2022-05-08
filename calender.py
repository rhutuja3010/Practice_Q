# print("officetime : 09:00 to 17:30")
# # a=officetime.split()
# # print(a)
# submission_time=input("YYYY-MM-DD HH:MM:SS EMP00")
# i=0
# while i<=5:
#     if submission_time>"2021:12:01 To 2022:12:31":

# # i=0
# # while i<=2:  
# # for i in submission_time:
# #     print(i)

# # employee=(input("enter the employee ID:---"))

# # for i in employee:
#     # print(i,end="")

#     # submission_time=str(input("enter the submission date and time:---"))
#     # for j in submission_time:
#     #     print(i,j,end="")
#     # break

# # start=int(input("entre the time :"))
# # end=int(input("enter the time :"))
# # print(start,end)

# unique=[]
# start_time=[]
# sub={}
# i=1
# while i<=5:
#     submission_time=input("YYYY:MM:DD HH:MM:SS EM00:----")
#     meatting_start_time=input("YYYY:MM:DD HH:MM:SS:.....")
#     # user=input("what do you what previous or next(n/p) :")
#     # if user=="p"
#     if submission_time>="2020:08:01 09:00:00" and submission_time<="2022:12:31 17:30:00":
#         user=input("Do you whant next meatting(yes/no) :")
#         if user=="yes": 
#             print(user)
        
        
#         if submission_time not in unique:
#             sub={}
#             unique.append(submission_time)
#             start_time.append(meatting_start_time)
#             print(unique,"\n",start_time)
#             sub.update({start_time:unique})
#     else:
#         print("sorry,,,Your submission time out ")    
#     i+=1


unique=[]
start_time=[]
sub={}
i=1
while i<=5:
    submission_time=input("YYYY:MM:DD HH:MM:SS EM00:----")
    meatting_start_time=input("YYYY:MM:DD HH:MM:SS:.....")
    # user=input("what do you what previous or next(n/p) :")
    # if user=="p"
    if submission_time>="2020:08:01 09:00:00" and submission_time<="2022:12:31 17:30:00":
        user=input("Do you whant next meatting(yes/no) :")
        if user=="yes": 
            print(user)
        else:
            print("I dont have")
        
        
        if submission_time not in unique :
            sub={}
            unique.append(submission_time)
            start_time.append(meatting_start_time)
            print(unique,"\n",start_time)
            # sub.update({start_time:unique})
    else:
        print("sorry,,,Your submission time out ")    
    i+=1
