""" Script used to train and test the model for prediction. It generates the confusion matrix and classification report

Usage:
  çresults/rf_classification.csvml_lgr_rf.py

"""
import pandas as pd
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC, SVR, LinearSVC
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import confusion_matrix
from sklearn.feature_selection import RFE
import time
from sklearn.metrics import classification_report

from sklearn.metrics import plot_confusion_matrix



df = pd.read_csv('data/cleaned_train_data.csv')
df.head(1)

df = df.drop(columns = 'Unnamed: 0', axis =0)


#plt.figure(figsize=(50,50))
#sns.heatmap( df.corr(), annot=True, cmap=plt.cm.Blues)
#plt.show()


X_train, X_valid, y_train, y_valid = train_test_split(df.drop(['C_SEV'], axis = 1),
                                                      df['C_SEV'],
                                                      test_size=0.2,
                                                      random_state = 100)


def fit_and_report(model, X, y, Xv, yv, mode = 'regression'):
    """
    The function computes test and training error for regression or classification ML models.
    
    ----------
    Argument
        
        model : Takes in a class of a ML model
        
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Training data of predictor
        
        y : array-like of shape (n_samples,) or (n_samples, n_targets)
        Training data of target

        Xv : {array-like, sparse matrix} of shape (n_samples, n_features)
        Validation data of predictor
        
        yv : array-like of shape (n_samples,) or (n_samples, n_targets)  
        Validation data of target
        
        mode : string of models which can be regression or classification
    
    ----------
    Return:
        errors : a list of training and test error
    
    ----------
    Default
        mode : takes in regression as default
    
    
    ----------
    Example
        fit_and_report(svm, X_train, y_train, X_valid, y_valid)
        >>>[13.783656508723558, 23.16818277751387]
    """
    model.fit(X, y)
    if mode.lower().startswith('regress'):
        errors = [mean_squared_error(y, model.predict(X)), mean_squared_error(yv, model.predict(Xv))]
    if mode.lower().startswith('classif'):
        errors = [1 - model.score(X,y), 1 - model.score(Xv,yv)]        
    return errors


lgr = LogisticRegression(solver = 'liblinear')
t = time.time()
lgr_rfe = RFE(estimator= lgr, n_features_to_select=100)
errors_lgr_rfe = fit_and_report(lgr_rfe, X_train, y_train,
                                         X_valid, y_valid, 
                                         mode='classification')
lgr_time = time.time() - t
print('Train error %0.5f'%(errors_lgr_rfe[0]))
print('Test error %0.5f'%(errors_lgr_rfe[1]))



rf = RandomForestClassifier(n_estimators=5)
t = time.time()
rf_rfe = RFE(estimator= rf, n_features_to_select=100)

rf_time = time.time() - t
errors_rf_rfe = fit_and_report(rf_rfe, X_train, y_train,
                                         X_valid, y_valid, 
                                         mode='classification')

print('Train error %0.5f'%(errors_rf_rfe[0]))
print('Test error %0.5f'%(errors_rf_rfe[1]))



# svm = SVC(kernel = 'rbf', gamma = 'scale')
# svm_rfe = RFE(estimator= svm, n_features_to_select=100)
# t = time.time()
# errors_svm_rfe = fit_and_report(svm, X_train, y_train,
#                                          X_valid, y_valid, 
#                                          mode='classification')
# svm_time = time.time() - t
# print('Train error %0.5f'%(errors_svm_rfe[0]))
# print('Test error %0.5f'%(errors_svm_rfe[1]))


# In[13]:


summary = pd.DataFrame({'Logistic Regression':[errors_lgr_rfe[0], errors_lgr_rfe[1], lgr_time],
              'Random Forest' : [errors_rf_rfe[0],errors_rf_rfe[1], rf_time]},
             index = ['Train score', 'Test score', 'Time'])
summary



confusion_matrix_lgr_train = confusion_matrix(y_train, lgr_rfe.predict(X_train))
confusion_matrix_lgr_valid = confusion_matrix(y_valid, lgr_rfe.predict(X_valid))
report_lgr = classification_report(y_valid, lgr_rfe.predict(X_valid), output_dict = True)

confusion_matrix_rfe_train = confusion_matrix(y_train, rf_rfe.predict(X_train))
confusion_matrix_rfe_valid = confusion_matrix(y_valid, rf_rfe.predict(X_valid))
report_rf = classification_report(y_valid, rf_rfe.predict(X_valid), output_dict = True)



# **Confusion matrix for logistic regression approach**
confusion_matrix_lgr_train

confusion_matrix_lgr_valid


# **Confusion matrix for logistic random forest approach**
confusion_matrix_rfe_train
confusion_matrix_rfe_valid


# **Classification report for logistic regression**
print(report_lgr)
print(report_rf)

df_rf_classification = pd.DataFrame(report_rf)
df_rf_classification.to_csv(r'results/rf_classification.csv')

df_rf_classification = pd.DataFrame(report_lgr)
df_rf_classification.to_csv("results/lgr_classification.csv")




