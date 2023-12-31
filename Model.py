#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import os


# # Data Import

# Defining given_essays as the official Kaggle train dataset and PaLM_generated_essays as a dataset exclusively LLM generated. Two datasets could be concatenated to make our training dataset and proportion of student written vs LLM generated would be approximately equal.

# In[3]:


given_essays = pd.read_csv('train_essays.csv')
PaLM_generated_essays = pd.read_csv('LLM_generated_essay_PaLM.csv')
#essays = pd.concat([essays, generated_essays])


# ArguGPT is a balanced corpus of 4,038 argumentative essays generated by 7 GPT models in response to essay prompts from three sources. Not the same prompts as the Kaggle dataset but nice variety of LLMs. Needs to be combined with human generated dataset. More info: https://www.kaggle.com/datasets/alejopaullier/argugpt

# In[6]:


argugpt_essays = pd.read_csv(r"ArguGPT\argugpt.csv")


# The DAIGT data is given in 4 csv files with over 30,000 rows in each. I am concatenating all the files here. Data comprised of:
# * Text generated with ChatGPT by MOTH (https://www.kaggle.com/datasets/alejopaullier/daigt-external-dataset)
# * Persuade corpus contributed by Nicholas Broad (https://www.kaggle.com/datasets/nbroad/persaude-corpus-2/)
# * Text generated with Llama-70b and Falcon180b by Nicholas Broad (https://www.kaggle.com/datasets/nbroad/daigt-data-llama-70b-and-falcon180b)
# * Text generated with ChatGPT by Radek (https://www.kaggle.com/datasets/radek1/llm-generated-essays)
# * Official train essays
# * Essays generated with various LLMs \
# \
# 
# Kinda the ultimate dataset. More info here: https://www.kaggle.com/datasets/thedrcat/daigt-proper-train-dataset/

# In[18]:


os.listdir('DAIGT')
daigt = pd.DataFrame()
for file in os.listdir('DAIGT'):
    daigt = pd.concat([daigt, pd.read_csv(r"DAIGT//%s" % file)])
    print(r"DAIGT//%s" % file)
#daigt_1 = pd.read_csv(r"DAIGT\train_drcat_01.csv")


# In[19]:


daigt


# # EDA

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Train Test Split

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Feature Engineering

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Model creation/testing

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




