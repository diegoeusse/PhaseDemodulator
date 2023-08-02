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

  # MSE
  mse = K.mean(K.square(E))

  # SSIM
  ssim = tf.image.ssim(ip, iv, max_val=1)
  L_ssim = 1 - ssim

  # PSNR
  psnr = tf.image.psnr(ip, iv, max_val=1)
  L_psnr = 1 - psnr*0.01

  # Loss
  loss = (1/3)*mse + (1/3)*L_ssim + (1/3)*L_psnr
  return loss