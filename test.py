import numpy as np


def init_net():
    net = {}
    net['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    net['b1'] = np.array([0.1, 0.2, 0.3])
    
    net['W2'] = np.array([[0.1, 0.4], [0.2,0.5], [0.3, 0.6]])
    net['b2'] = np.array([0.1, 0.2])

    net['W3'] = np.array([[0.1, 0.3], [0.2,0.4]])
    net['b3'] = np.array([0.1, 0.2])


    return net




def forward(net, x):
    w1, w2, w3 = net['W1'], net['W2'], net['W3']                                      
    b1, b2, b3 = net['b1'], net['b2'], net['b3']

    a1 = np.dot(x, w1) 

    print(a1)



x = np.array([1.0, 0.5])
y = forward(init_net(), x)
print(y)
                                        
