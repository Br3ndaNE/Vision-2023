import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

totalsize = len(digits.data)
predictLabel = []
predict = []
X = []
y = []
counter = 1

for i in range(totalsize):
    if counter == 1 or counter == 2:
        X.append(digits.data[i])
        y.append(digits.target[i])
        counter += 1
    elif counter == 3:
        predict.append(digits.data[i])
        predictLabel.append(digits.target[i])
        counter = 1

print(len(digits.data))
print(len(X))
print(len(predict))
predictRange = len(predict)

# print(totalsize)
clf = svm.SVC(gamma=0.001, C=100)
X,y = X, y
clf.fit(X,y)

# print("Predict:")
# print(clf.predict(digits.data[-5:-4])) #Beetje flauw, maar hij wil perse 2d-array hebben ook als er maar 1 element inzit
# plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
# plt.show()
goodCounter = 0
for i in range(predictRange):
    prediction = clf.predict([predict[i]])
    print(i,prediction, predictLabel[i])
    if prediction == predictLabel[i]:
        goodCounter += 1
    # image = predict[i].reshape(8, 8)
    # plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    # plt.show()

percentage = goodCounter / predictRange * 100
print(percentage,"%")
