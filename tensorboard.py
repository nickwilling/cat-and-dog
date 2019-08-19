#报no module named tensorflow的时候一定要先 activate tensorflow
#然后再tensorboard --logdir=logs


import  tensorflow as tf
import  numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def add_layer(inputs, in_size, out_size,n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]),name='W')
            tf.summary.histogram(layer_name+'/weights',Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size]) + 0.1,name='b')
            tf.summary.histogram(layer_name + '/biases', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name + '/outputs', outputs)
        return outputs

x_data = np.linspace(-1,1,300)[:, np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32,[None,1],name='x_input')
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')
l1 = add_layer(xs, 1, 10,n_layer=1, activation_function=tf.nn.relu)
prediction = add_layer(l1, 10, 1,n_layer=2, activation_function=None)
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]),name='loss')
    tf.summary.scalar('loss',loss)
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter("log/",sess.graph)
sess.run(init)#上面只是定义，并没有进行运算
for i in range(1000):
    sess.run(train_step,{xs:x_data,ys:y_data})
    if i % 50==0:
        print(sess.run(loss, {xs: x_data, ys: y_data}))
        result = sess.run(merged,{xs:x_data,ys:y_data})
        writer.add_summary(result,i)


