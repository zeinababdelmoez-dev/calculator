#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True : 

    first=float(input("Enter The First Number"))
    sec=float(input("Enter The Second Number"))
    op=input("Enter The Operator'+,-,*,/'").strip()
    if op =='+' :
        print( first+sec)
    elif  op =='-' :
        print( first-sec)
    elif  op =='*' :
        print( first*sec)
    elif  op =='/' :
        if sec==0:
            print ("cannot divission by zero")
        else :
            print( first/sec)
    else :
        print ("invalid operator can choose of'+,-,*,/'")
    again=input("would you calculate again? (yes, no)") 
    if again.lower() == "no":
        print("Thank you for using our calculation")
        break
        


# In[ ]:




