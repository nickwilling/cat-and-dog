import  tensorflow as tf
import numpy as np
#定义变量 初始值是0，名字叫counter
state = tf.Variable(0, name="counter")
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign()
init = tf.initialize_all_variables()    #must have if define variables
with tf.Session() as sess:
    sess.run(init)  #一定要run才会被激活，初始
    for _ in range(3):
        sess.run(update)
        print(sess.run(state)) #直接print state是没有用的，一定要把session的指针放到state上run一下才会有state的结果