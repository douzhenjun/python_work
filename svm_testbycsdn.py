'''
逻辑回归：from sklearn.linear_model import LogisticRegression

朴素贝叶斯：from sklearn.naive_bayes import GaussianNB

K-近邻：from sklearn.neighbors import KNeighborsClassifier

决策树：from sklearn.tree import DecisionTreeClassifier

支持向量机：from sklearn import svm
'''
#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.utils import check_random_state
from sklearn import svm, datasets
import sklearn.model_selection as ms
import matplotlib.pyplot as plt
#数据地址 :http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

#load data
iris = datasets.load_iris()
rng = check_random_state(42)
perm = rng.permutation(iris.target.size)
iris_data = iris.data[perm]
iris_target = iris.target[perm]

#拆分数据
x_train, x_test, y_train, y_test = ms.train_test_split(iris_data, iris_target, random_state = 1, train_size = 0.6)

#训练模型
for k in ('linear', 'rbf'):
    clf = svm.SVC(kernel=k).fit(x_train, y_train)
    #打印预测精度    
    print(np.mean(clf.predict(x_train) == y_train))
'''
kernel='linear'时，为线性核，C越大分类效果越好，但有可能会过拟合（defaul C=1）
kernel='rbf'时（default），为高斯核，gamma值越小，分类界面越连续；gamma值越大，分类界面越“散”，分类效果越好，但有可能会过拟合。
decision_function_shape='ovr'时，为one v rest，即一个类别与其他类别进行划分，
decision_function_shape='ovo'时，为one v one，即将类别两两之间进行划分，用二分类的方法模拟多分类的结果。
'''
#画图
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

#画出前两个特征的散点图
x1_min, x1_max = iris_data[:, 0].min(), iris_data[:, 0].max() #第0列的范围
x2_min, x2_max = iris_data[:, 1].min(), iris_data[:, 1].max() #第一列的范围

plt.scatter(iris_data[:, 0], iris_data[:, 1], c = iris_target)
#plt.scatter(x_test[:, 0], x_test[:, 1], s=120, zorder=10 )  # 圈中测试集样本
plt.xlabel(u'花萼长度', fontsize=13)
plt.ylabel(u'花萼宽度', fontsize=13)
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.title(u'鸢尾花SVM二特征分类', fontsize=15)
plt.show()
