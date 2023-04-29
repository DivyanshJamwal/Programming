from sklearn import metrics

C = 'Cat'
D = 'Dog'
F = 'Fox'

y_true = [C,C,C,C,C,C, F,F,F,F,F,F,F,F,F,F, D,D,D,D,D,D,D,D,D]
y_pred = [C,C,C,C,D,F, C,C,C,C,C,C,D,D,F,F, C,C,C,D,D,D,D,D,D]

print(metrics.confusion_matrix(y_true,y_pred))
print(metrics.classification_report(y_true,y_pred,digits=3))