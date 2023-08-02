import keras.backend as K
import tensorflow as tf

# ip -> y_pred
# iv -> y_true

def get_loss(iv, ip):
  """
  Define the composite loss function that includes total variation of errors 
  loss and variance of errors loss
  """
  # total variation loss
  y_x = iv[:, 1:256, :, :] - iv[:, 0:255, :, :]
  y_y = iv[:, :, 1:256, :] - iv[:, :, 0:255, :]
  y_bar_x = ip[:, 1:256, :, :] - ip[:, 0:255, :, :]
  y_bar_y = ip[:, :, 1:256, :] - ip[:, :, 0:255, :]
  L_tv = K.mean(K.abs(y_x - y_bar_x)) + K.mean(K.abs(y_y - y_bar_y))

  # variance of the error loss
  E = ip - iv
  L_var = K.mean(K.mean(K.square(E), axis=(1, 2, 3)) - K.square(K.mean(E, axis=(1, 2, 3))))

  # MSE - L1
  L1 = K.mean(K.square(E))

  # MAE - L2
  L2 = K.mean(K.square(E))

  # SSIM
  ssim = tf.image.ssim(ip, iv, max_val=1)
  L_ssim = 1 - ssim

  # PSNR
  psnr = tf.image.psnr(ip, iv, max_val=1)
  L_psnr = 1 - psnr*0.01

  # Loss
  loss = (0.125)*(L_var + 0.1 * L_tv) + (0.125)*L1 + (0.125)*L2 + (0.5)*L_ssim + (0.125)*L_psnr
  return loss