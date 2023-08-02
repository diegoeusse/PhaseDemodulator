import keras.backend as K

def tv_loss_plus_var_loss(y_true, y_pred):
  """
  Define the composite loss function that includes total variation of errors 
  loss and variance of errors loss
  """
  # total variation loss
  y_x = y_true[:, 1:256, :, :] - y_true[:, 0:255, :, :]
  y_y = y_true[:, :, 1:256, :] - y_true[:, :, 0:255, :]
  y_bar_x = y_pred[:, 1:256, :, :] - y_pred[:, 0:255, :, :]
  y_bar_y = y_pred[:, :, 1:256, :] - y_pred[:, :, 0:255, :]
  L_tv = K.mean(K.abs(y_x - y_bar_x)) + K.mean(K.abs(y_y - y_bar_y))

  # variance of the error loss
  E = y_pred - y_true
  L_var = K.mean(K.mean(K.square(E), axis=(1, 2, 3)) - K.square(K.mean(E, axis=(1, 2, 3))))

  loss = L_var + 0.1 * L_tv
  return loss