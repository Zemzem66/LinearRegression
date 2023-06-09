########################################################################################################################
# REMARKS
########################################################################################################################
'''
## Coding
- please note, this no SE course and much of the code in ML is more akin to executing workflows
- please try to use the scripts as a documentation of your analysis, including comments, results and interpretations

## GRADING
- Please refer to the moodle course for grading information

## UPLOAD
- upload your solution on Moodle as: "yourLASTNAME_yourFIRSTNAME_yourMOODLE-UID___exercise_blockX.py"
- please no non-ascii characters on last/first name :)
- NO zipfile, NO data!, ONLY the .py file!

## PRE-CODED Parts
- all exercises might contain parts which where not yet discussed in the course
- these sections are pre-coded then and you are encouraged to research their meaning ahead of the course
- so, if you find something in the exercise description you haven´t heard about, look at the ode section and check if this is pre-coded

## ERRORS
- when you open exercise files you'll see error (e.g. unassigned variables)
- this is due to the fact that some parts are missing, and you should fill them in
'''


########################################################################################################################
# IMPORTS
########################################################################################################################


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt

########################################################################################################################
# IMPLEMENT AN OLS  PARAMETER ESTIMATION FOR LINEAR REGRESSION USING ONLY NUMPY
########################################################################################################################
'''
In this exercise we want you to visualise and understand linear regression.

data:
-----
winequality-red.csv
https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/
we want to estimate the quality as labelled by "expert-drinkers" based on only ONE feature (alcohol)

what you DONT need to care about:
---------------------------------
- missing data
- categorical/binary features

output:
-------
- use sklearn.linear_model to predict quality based on alcohol content
- plot alcohol content vs the quality predictions with red x-symbols
- plot alcohol content vs the true quality with blue filled circles
- draw a green line between predicted qualities and true qualities to visualise the residuals (= Size of the error we made)
- the result should look like this https://i.stack.imgur.com/zoYKG.png (But with different data!!)
- then label the x-axis and y-axis
- Calculate the Mean Squared Error (MSE)
'''

# read the data --------------------------------------------------
# -- predefined --
pth = r'winequality-red.csv'
df = pd.read_csv(pth, sep=";")

X = df['alcohol'].values.reshape(-1, 1)
y = df['quality'].values


# solution



# visualise the residuals


