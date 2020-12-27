#!/usr/bin/env python
# coding: utf-8


# In[6]:


number_50 = 50
my_number = None
if number_50 > 100:
     less_than_50 = 100
    # if number_50 is greater than 100, assign the `my_number` variable to the number 100
elif number_50 > 50:
     less_than_50 = 50
    # if number_50 is greater than 50, assign the `my_number` variable to the number 50
else:
    less_than_50 = 0
    # else assign the `my_number` variable to 0


# In[7]:


#Below, use conditionals to tell whether it is hot outside or not. If it is hot, assign the string "It is so hot out!"
#to the variable is_it_hot. If it is not hot, assign the string "This is nothing! Bring on the heat.". 
#For our purposes, anything over 80 degrees is considered hot.

temperature = 85
is_it_hot = None
if temperature > 85 :
    print("It is so hot out!")
elif temperature < 85 :
    print("This is nothing! Bring on the heat.")
else :
    print("hot")
# conditionals go here


# In[8]:


#Next, let's see what day of the week it is. There are 7 days in the week starting with Sunday at day `1` and 
#ending with Saturday at day `7`. Use conditional statements to assign the day of the week to the variable 
#`day_of_the_week` based on the number below assigned to the variable `today_is`.
#For example, if the day is `2`, we would assign `day_of_the_week` the value `"Monday"`.

today_is = 4
day_of_the_week = None
if today_is == 1:
    day_of_the_week = "Sunday"
elif today_is == 2:
    day_of_the_week = "Monday"
elif today_is == 3:
    day_of_the_week = "Tuesday"
elif today_is == 4:
    day_of_the_week = "Wednesday"
elif today_is == 5:
    day_of_the_week = "Thursday"
elif today_is == 6:
    day_of_the_week = "Friday"
elif today_is == 7:
    day_of_the_week = "Saturday"
# conditionals go here


# In[10]:


#"Finally, let's take a string and see if it ends with a certain substring. 
#If it does, assign the variable ends_with to True, and if it does not, assign it to False. 
#For example, if have the string "School" and we want to know if it ends with the sub-string "cool". 
#In this case it does not, so, we would assign False to the variable ends_with.
string = "Python"
sub_string = "on"
ends_with = None
if string.endswith(sub_string):
    ends_with = True
else:
    ends_with = False
#conditionals go here


# In[ ]:




