import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
rng = numpy.random
 
# 파라매터들 변수를 조정 합니다.
# 변화 수치, 전체 실행 수, 몇 번마다 화면에 로그를 보여 줄지를 정합니다.
learning_rate = 0.01
training_epochs = 1000
display_step = 50
 
# 훈련용 데이터를 지정합니다.
train_X = numpy.asarray([1, 2, 5, 7])
train_Y = numpy.asarray([4, 7, 16, 22])
n_samples = train_X.shape[0]
 
# 텐서플로우 변수들을 만듭니다.
X = tf.placeholder("float")
Y = tf.placeholder("float")
 
W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")
 
# 모델 'y = Wx + b' 를 정의합니다.
pred = tf.add(tf.multiply(X, W), b)
 
# least square 공식을 이용하여 최소값을 만들 요소를 지정합니다. 
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
 
# 기울기를 보정하는 경사하강법이란것을 사용하고, 비용을 최소화 하는 방향으로 학습 합니다.
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
 
# 초기화를 합니다.
init = tf.global_variables_initializer()
 
# 텐서플로우를 기동 합니다.
with tf.Session() as sess:
    sess.run(init)
 
    # 데이터를 넣습니다.
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})
 
        # 50번 마다 로그 뿌려서 찾는 값 변화를 보여 줍니다.
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b))
 
    # 완료가 되면 결과를 출력합니다.
    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')
 
    # 찾은 결과를 그래프로 보여줍니다.
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()
