# Exercise 6                            
# Write a Python program which allows you to evaluate a note entered on the keyboard 
# (if the note is greater than 10 then it displays validated otherwise not validated (NB: the note between 0 and 20). 

note=input(""" (NB: the note between 0 and 20)
Enter a note: """)
if len(note)<=20 and len(note)>=10:
    print(f"The note is validated. the note is {note} and the length is {len(note)}")
else:
    print (f"Not validated. the note is {note} and the length is {len(note)}")
