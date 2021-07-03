import os, re, glob
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator # 이미지 증식을 위한 함수
import numpy as np
from keras.preprocessing import image # 이미지 데이터 전처리 위한 함수

groups_folder_path = './images/'
categories = ["E",  "N",  "S", "W"] # 방향 라벨 저장

num_classes = len(categories)

image_w = 28
image_h = 28

X = []
Y = []

for idex, categorie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idex] = 1  # 해당 순환 인덱스에 1값 대입
    image_dir = groups_folder_path + categorie + '/'

    for top, dir, f in os.walk(image_dir):
        cnt = 0  # 증식할 이미지 개수
        for filename in f:
            # print(image_dir + filename)
            img = cv2.imread(image_dir + filename)
            # 이미지 증식
            image_generator = ImageDataGenerator(
                rotation_range=10,
                zoom_range=0.50,
                shear_range=0.5,
                width_shift_range=0.10,
                height_shift_range=0.10,
                horizontal_flip=False,
                vertical_flip=False)

            img = cv2.resize(img, (28, 28)) # 이미지 resize
            # cv2.imshow('org', img)
            images = np.array([img])

            for i in range(10):  # 이미지당 10번 증식
                x_augmented = image_generator.flow(x=images, batch_size=1)[0]
                # cv2.imshow('aug', np.array(image.array_to_img(x_augmented[0])))

                X.append(x_augmented / 256) # x리스트에 정규화된 증식이미지 추가
                Y.append(label) # Y리스트에 라벨 추가

                cnt += 1

            print(image_dir)
            print(np.shape(X))
            print(np.shape(Y))

            if cnt == 100:
                break

X = np.array(X)
Y = np.array(Y)
# 리스트 x와 y를 np배열형으로 변환

# split메소드를 이용해 훈련이미지와 검증이미지를 분류한다
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
xy = (X_train, X_test, Y_train, Y_test)

print('X_train : ', np.shape(X_train))
print('X_test : ', np.shape(X_test))
print('X_train : ', np.shape(Y_train))
print('X_test : ', np.shape(Y_test))

# np.save("./img_data.npy", xy)