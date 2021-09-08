# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:37:33 2020
****codigo baseado no artigo escrito por randerson112358,
disponivel em: https://medium.com/better-programming/titanic-survival-prediction-using-machine-learning-4c5ff1e3fa16
@author: Yuri Getaruck
"""

# descrição: este programa preve se um determinado passageiro morreria no titanic

# importando bibliotecas

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# carregando e analizando dados
titanic = sns.load_dataset('titanic')
a = titanic.head(10)
b = titanic.shape
c = titanic.describe()

sobreviventes = titanic['survived'].value_counts()

sns.countplot(titanic['survived'])

cols = ['who', 'sex', 'pclass', 'sibsp', 'parch', 'embarked']

n_rows = 2
n_cols = 3

# The subplot grid and the figure size of each graph
# This returns a Figure (fig) and an Axes Object (axs)
fig, axs = plt.subplots(n_rows, n_cols, figsize=(n_cols * 3.2, n_rows * 3.2))

for r in range(0, n_rows):
    for c in range(0, n_cols):
        i = r * n_cols + c  # index to go through the number of columns
        ax = axs[r][c]  # Show where to position each subplot
        sns.countplot(titanic[cols[i]], hue=titanic["survived"], ax=ax)
        ax.set_title(cols[i])
        ax.legend(title="survived", loc='upper right')

plt.tight_layout()  # tight_layout

sexos = titanic['sex'].value_counts()

# sobreviventes por sexo
d = titanic.groupby('sex')[['survived']].mean()

# sobreviventes por sexo e classe
e = titanic.pivot_table('survived', index='sex', columns='class')
titanic.pivot_table('survived', index='sex', columns='class').plot()

# sobrevivencia por classe
sns.barplot(x='class', y='survived', data=titanic)

# sobreviventes por classe sexo e taxa
age = pd.cut(titanic['age'], [0, 18, 80])
titanic.pivot_table('survived', ['sex', age], 'class')

# preços pagos por cada classe
plt.scatter(titanic['fare'], titanic['class'], color='purple', label='Passenger Paid')
plt.ylabel('Class')
plt.xlabel('Price / Fare')
plt.title('Price Of Each Class')
plt.legend()
plt.show()

# retirando colunas de dados julgadas nao atraentes para a solução
titanic = titanic.drop(['deck', 'embark_town', 'alive', 'class', 'alone', 'adult_male', 'who'], axis=1)

# removendo dados que possuem lacunas
titanic = titanic.dropna(subset=['embarked', 'age'])

# dados restantes
titanic.shape

# transformando dados nao numericos em numericos
from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()

titanic.iloc[:, 2] = labelencoder.fit_transform(titanic.iloc[:, 2].values)

titanic.iloc[:, 7] = labelencoder.fit_transform(titanic.iloc[:, 7].values)

# definindo varieaveis para treino
X = titanic.iloc[:, 1:8].values
Y = titanic.iloc[:, 0].values

# definido porcentagem de treino e teste
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# parte retirada do codigo do randerson112358, para realizar os diferentes scripts e descobrir a melhor acuracia
# determina tambem falsos positivos e falsos negativos
# -----------------------------------------------------------------------------------------------------------

# Create a function within many Machine Learning Models
def models(X_train, Y_train):
    # Using Logistic Regression Algorithm to the Training Set
    from sklearn.linear_model import LogisticRegression
    log = LogisticRegression(random_state=0)
    log.fit(X_train, Y_train)

    # Using KNeighborsClassifier Method of neighbors class to use Nearest Neighbor algorithm
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
    knn.fit(X_train, Y_train)

    # Using SVC method of svm class to use Support Vector Machine Algorithm
    from sklearn.svm import SVC
    svc_lin = SVC(kernel='linear', random_state=0)
    svc_lin.fit(X_train, Y_train)

    # Using SVC method of svm class to use Kernel SVM Algorithm
    from sklearn.svm import SVC
    svc_rbf = SVC(kernel='rbf', random_state=0)
    svc_rbf.fit(X_train, Y_train)

    # Using GaussianNB method of naïve_bayes class to use Naïve Bayes Algorithm
    from sklearn.naive_bayes import GaussianNB
    gauss = GaussianNB()
    gauss.fit(X_train, Y_train)

    # Using DecisionTreeClassifier of tree class to use Decision Tree Algorithm
    from sklearn.tree import DecisionTreeClassifier
    tree = DecisionTreeClassifier(criterion='entropy', random_state=0)
    tree.fit(X_train, Y_train)

    # Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
    from sklearn.ensemble import RandomForestClassifier
    forest = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
    forest.fit(X_train, Y_train)

    # print model accuracy on the training data.

    print('[0]Logistic Regression Training Accuracy:', log.score(X_train, Y_train))
    print('[1]K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
    print('[2]Support Vector Machine (Linear Classifier) Training Accuracy:', svc_lin.score(X_train, Y_train))
    print('[3]Support Vector Machine (RBF Classifier) Training Accuracy:', svc_rbf.score(X_train, Y_train))
    print('[4]Gaussian Naive Bayes Training Accuracy:', gauss.score(X_train, Y_train))
    print('[5]Decision Tree Classifier Training Accuracy:', tree.score(X_train, Y_train))
    print('[6]Random Forest Classifier Training Accuracy:', forest.score(X_train, Y_train))

    return log, knn, svc_lin, svc_rbf, gauss, tree, forest


# Get and train all of the models
model = models(X_train, Y_train)

from sklearn.metrics import confusion_matrix

for i in range(len(model)):
    cm = confusion_matrix(Y_test, model[i].predict(X_test))
    # extracting TN, FP, FN, TP
    TN, FP, FN, TP = confusion_matrix(Y_test, model[i].predict(X_test)).ravel()
    print(cm)
    print('Model[{}] Testing Accuracy = "{} !"'.format(i, (TP + TN) / (TP + TN + FN + FP)))
    print()  # Print a new line

