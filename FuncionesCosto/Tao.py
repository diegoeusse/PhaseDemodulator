import keras.backend as K
import tensorflow as tf

# ip -> y_pred
# iv -> y_true

def get_loss(ip, iv):
  """
  Define the composite loss function that includes total variation of errors 
  loss and variance of errors loss
  """

  E = ip - iv

  # L1
  L1 = K.mean(K.abs(E))

  # L2
  L2 = K.mean(K.square(E))

  # MS-SSIM
  ssim = tf.image.ssim(ip, iv, max_val=1)
  L_ssim = 1 - ssim

  # Parametros
  a = 0.5
  b = 0.25

  # Loss
  loss = a*L_ssim + b*L1 + (1-a-b)*L2
  return loss