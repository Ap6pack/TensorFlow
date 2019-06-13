import tensorflow as tf
from math import pi

mean = 0.0
sigma = 1.0

x = 758400

norm_Dist = (tf.exp(tf.negative(tf.pow(x - mean, 2.0) /
                    (2.0 * tf.pow(sigma, 2.0) ))) *
 (1.0 / (sigma * tf.sqrt(2.0 * pi) )))

print(norm_Dist)
