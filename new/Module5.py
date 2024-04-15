import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import random
digits = datasets.load_digits()

counterSwag = 0
while(counterSwag < 10):
    totalsize = len(digits.data)
    predictLabel = []
    predict = []
    Random_x = []
    Random_y = []
    counter = 1

    #Random
    indices = list(range(len(digits.data)))
    random.shuffle(indices)

    digits.data = [digits.data[i] for i in indices]
    digits.target = [digits.target[i] for i in indices]

    #Random
    for i in range(totalsize):
        if counter == 1 or counter == 2:
            Random_x.append(digits.data[i])
            Random_y.append(digits.target[i])
            counter += 1
        elif counter == 3:
            predict.append(digits.data[i])
            predictLabel.append(digits.target[i])
            counter = 1

    predictRange = len(predict)

    # print(totalsize)
    clf = svm.SVC(gamma=0.001, C=100)
    Random_x,Random_y = Random_x, Random_y
    clf.fit(Random_x,Random_y)

    goodCounter = 0
    for i in range(predictRange):
        prediction = clf.predict([predict[i]])
        # print(i,prediction, predictLabel[i])
        if prediction == predictLabel[i]:
            goodCounter += 1
        # else:
        #     print("false",(i,prediction, predictLabel[i]))
        # image = predict[i].reshape(8, 8)
        # plt.imshow(image, cmap=plt.cm.graRandom_y_r, interpolation='nearest')
        # plt.show()
        

    percentage = goodCounter / predictRange * 100
    counterSwag += 1
    print(counterSwag,":    ",round(percentage,3),"%")
