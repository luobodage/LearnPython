import tensorflow as tf
import random
import numpy as np

datas = []
labellist = []

for i in range(500):
    num = random.randrange(1, 10)  # 生成一个一到十之间的数 不包括十
    one_hot = np.zeros(shape=9)  # 生成一个长为9的全零行
    one_hot[num - 1] = 1  # 寻址变为1
    datas.append(one_hot)
    labellist.append(one_hot)

# keras要求输入的是array的形式所以需要对list进行array处理
datas = np.array(datas)
labellist = np.array(labellist)

# 设置log的路径方便后面的网络分析
log_dir = './logs'
tensorboard_call = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# 一个三层网络
inputes = tf.keras.layers.Input(shape=(9,))  # 输入层
x = tf.keras.layers.Dense(64, activation='relu')(inputes)  # activation 激活函数relu 64 十神经元数量
x = tf.keras.layers.Dense(64, activation='relu')(x)  # 再来一次
perdictions = tf.keras.layers.Dense(9, activation='softmax')(x)  # 创建输出层
model = tf.keras.models.Model(inputs=inputes, outputs=perdictions)
# 交叉熵函数
model.compile(optimizer='sgd', loss=tf.keras.losses.CategoricalCrossentropy())
# 训练
model.fit(datas, labellist, epochs=100, verbose=1, callbacks=[tensorboard_call])
for i in range(10):
    num = random.randrange(1, 10)
    one_hot = np.zeros(shape=9)
    one_hot[num - 1] = 1
    predict = np.argmax(model.predict(np.expand_dims(one_hot, axis=0)))+1
    print("predict num is %d ,real num is  %d" % (predict, num))
