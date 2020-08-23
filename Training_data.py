#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from PIL import Image
import numpy as np


# In[2]:


IMG_SIZE = 128
IMG_CHANNELS = 3
DIR = 'Cubism/'


# In[6]:


training_data = []
print('Reading')
for images in os.listdir(DIR):
    path = os.path.join(DIR,images)
    image = Image.open(path).resize((IMG_SIZE,IMG_SIZE), Image.ANTIALIAS)
    training_data.append(np.array(image))
    
print('Resizing')
training_data = np.reshape(
    training_data, (-1, IMG_SIZE, IMG_SIZE, IMG_CHANNELS))

training_data = training_data / 127.5 - 1

print('Saving')
np.save('cubism_data.npy', training_data)

