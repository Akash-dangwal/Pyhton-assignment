#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("Travel.csv")
df


# In[3]:


# Q1. What is the distribution of customerages, and how does age relate to product purchase (ProdTaken)?
average_prod_taken_by_age = df.groupby('Age')['ProdTaken'].mean()
average_prod_taken_by_age


# In[4]:


4. # Q2. How does the type of contact(type of contact)influence the likelihood of purchasing a travel product?
average_prod_taken_by_contact = df.groupby('TypeofContact')['ProdTaken'].mean()
average_prod_taken_by_contact


# In[5]:


# Q3. Is there a correlation between the city tier(citytier)and monthly income (monthly income) of customers?
correlation = df['CityTier'].corr(df['MonthlyIncome'])
correlation


# In[6]:


# Q4 What is the average duration of a pitch (duration of pitch)for customers who purchased a product versus those who did not?
mean_duration_purchased = df[df['ProdTaken'] == 1]['DurationOfPitch'].mean()
mean_duration_not_purchased = df[df['ProdTaken'] == 0]['DurationOfPitch'].mean()
print("Average duration of pitch for customers who purchased a product:", mean_duration_purchased)
print("Average duration of pitch for customers who did not purchase a product:", mean_duration_not_purchased)


# In[7]:


7.# Q5. How do occupation types(occupation)distribute among customers,and is there an occupation type that is more likely to purchase a travel product?
occupation_distribution = df['Occupation'].value_counts()
average_prod_purchase_by_occupation =df.groupby('Occupation')['ProdTaken'].mean()
print("Occupation distribution among customers:",occupation_distribution)
print("\nAverage product purchase rate by occupation:",average_prod_purchase_by_occupation)


# In[8]:


# Q6. Are there any gender-based preferences for the type of product pitched (ProductPitched)?
gender_product_pitch_distribution =df.groupby('Gender')['ProductPitched'].value_counts()
gender_product_pitch_distribution


# In[9]:


# Q7. What is the relationship between the number of trips(number of trips)taken by a customer and their likelihood to purchase a new travel product?
average_prod_purchase_by_trips =df.groupby('NumberOfTrips')['ProdTaken'].mean()
average_prod_purchase_by_trips


# In[10]:


# Q8.Does having a passport(passport)correlate with a higher number of trips taken or a higher likelihood of purchasing a travel product?
correlation_trips_passport = df['Passport'].corr(df['NumberOfTrips'])
correlation_purchase_passport = df['Passport'].corr(df['ProdTaken'])
print("Correlation between having a passport and the number of trips taken:", correlation_trips_passport)
print("Correlation between having a passport and the likelihood of purchasing a travel product:", correlation_purchase_passport)


# In[11]:


# Q9.How satisfied are customers with the pitch (pitch satisfaction score),and does this satisfaction influence product purchase?
average_satisfaction_score = df.groupby('PitchSatisfactionScore')['ProdTaken'].mean()
average_satisfaction_score


# In[12]:


# Q10. Among customers with children (number of children visiting),how does the number of children impact travel product purchases?
df_with_children = df[df['NumberOfChildrenVisiting'] > 0]
average_prod_purchase_by_children = df_with_children.groupby('NumberOfChildrenVisiting')['ProdTaken'].mean()
average_prod_purchase_by_children


# In[18]:


# Q11. Gender preferences for product types: how does gender influence the preference for different types of travel products pitched (product pitched)?
gender_product_pitch_distribution = df.groupby('Gender')['ProductPitched'].value_counts()
gender_product_pitch_distribution


# In[13]:


# Q12. Impact of marital status on travel preferences: does marital status affect the choice of travel product, and if so, how do different marital statuses correlate with product
marital_status_product_pitch_distribution = df.groupby('MaritalStatus')['ProductPitched'].value_counts()
marital_status_product_pitch_distribution


# In[14]:


# Q13. Relationship between number of children and travel product interest: how does the number of children visiting (number of children visiting) impact the likelihood of purchasing a travel product?
average_prod_purchase_by_children =df.groupby('NumberOfChildrenVisiting')['ProdTaken'].mean()
average_prod_purchase_by_children


# In[21]:


df


# In[15]:


# Q14. Income level and product choice: how does the monthly income (monthly income) of customers influence their choice of travel products, and is there a preferred product for different income levels?
income_bins = [0, 10000, 20000, 30000, 40000, float('inf')]
income_labels = ['0-10k', '10k-20k', '20k-30k', '30k-40k','40k+']
df['IncomeLevel'] = pd.cut(df['MonthlyIncome'],
bins=income_bins, labels=income_labels, right=False)
income_product_pitch_distribution = df.groupby('IncomeLevel')['ProductPitched'].value_counts()
income_product_pitch_distribution


# In[ ]:




