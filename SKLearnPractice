from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import array as arr
        # Little Data
C = np.array([40, 60, 100, 15, 30])
F = np.array ([104,140, 212, 59, 86])
m = len (F) # Size of the arrays
print (C)
#Cannot use Rank 1 matrix in scikit learn
new_C = np.array([25, 60, 100, 15, 30])
        # Our desire value to be converted into Faranheit
theValue = new_C[0]
    #Gotta reshape them: our old data of imputs and our new one
new_C = new_C.reshape((m,1))
C = C.reshape((m,1))
print (C)

#Creating a model
reg = LinearRegression()
#Fitting Training Data
reg = reg.fit(C,F)
#Faranheit Prediction in based of the model
F_Pred = reg.predict(new_C)

r2_score = reg.score(C,F)
# 25 is 77

print (r2_score)
print (theValue, " Celsius in Faranheit is ",F_Pred[0])



