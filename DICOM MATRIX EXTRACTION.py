#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nibabel as nib  
import numpy as np  

# Load the NIfTI file  
nifti_file_path = "C:\\Users\\Sijal\\Desktop\\my-projects\\DATASETS\\PROSTATE-UCSF\\ordinary\\MRI_Images\\0006_a.nii.gz"  
nifti_data = nib.load(nifti_file_path)  

# Extract the image data as a NumPy array  
image_data = nifti_data.get_fdata()  

print(image_data)


# In[ ]:




