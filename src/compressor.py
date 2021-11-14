import numpy as np
from numpy import sqrt
import time
from PIL import Image
import random

def simultaneous_power_iteration(A,k):
  n, m = A.shape
  Q = np.random.rand(n,k)
  Q, _ = np.linalg.qr(Q)

  for i in range(200):
      Z = A.dot(Q)
      Q, R = np.linalg.qr(Z)

  return np.diag(R), Q

def addRandomNoise(arr):
  _THRESHOLD = 1e-10
  newArr = arr.copy()
  for i in range(len(arr)):
    newArr[i] = random.uniform(_THRESHOLD, 10 * _THRESHOLD) if arr[i] < _THRESHOLD else arr[i]
  return newArr

def matrix_compress(M, rate):
  M = np.array(M).copy()
  n, m = M.shape
  if n < m:
    nn = max(1, int((m*n) * rate/(100*(m+n+1))))
    L = M @ M.T
    Sn, Un = simultaneous_power_iteration(L, nn)
    Sn = addRandomNoise(Sn)
    Sn = sqrt(np.abs(Sn))
    U = np.zeros((n,n))
    U[:n, :nn] = Un
    S = np.zeros((n,m))
    S[:nn, :nn] = np.diag(Sn)
    Vn = np.linalg.inv(np.diag(Sn)) @ Un.T @ M
    V = np.zeros((m,m))
    mm, _ = Vn.shape
    V[:mm, :m] = Vn
  else:
    mm = max(1, int((m*n) * rate/(100*(m+n+1))))
    R = M.T @ M
    Sn, Vn = simultaneous_power_iteration(R, mm)
    Sn = addRandomNoise(Sn)
    Sn = sqrt(np.abs(Sn))
    S = np.zeros((n,m))
    S[:mm, :mm] = np.diag(Sn)
    V = np.zeros((m,m))
    V[:m, :mm]= Vn
    Un = M @ Vn @ np.linalg.inv(np.diag(Sn))
    _,nn =Un.shape
    U = np.zeros((n,n))
    U[:n, :nn] = Un
    V = V.T
  return np.clip((U @ S @ V),0,255)

def compress(original,compressed,rate):
    start_time = time.time()
    image = Image.open(original)

    if image.mode == 'P' or image.mode == 'L':
        img_array = np.asarray(image.convert("RGBA"))
    else:
        img_array = np.asarray(image)

    if img_array.shape[-1] == 3:
      R,G,B = np.squeeze(np.split(img_array, img_array.shape[-1], -1), axis=-1).astype(float)
    elif img_array.shape[-1] == 4:
      R,G,B,A = np.squeeze(np.split(img_array, img_array.shape[-1], -1), axis=-1).astype(float)
    else:
      raise Exception("Image type not supported")
    R = matrix_compress(R, rate)
    G = matrix_compress(G, rate)
    B = matrix_compress(B, rate)
    if img_array.shape[-1] == 3:
      res = np.dstack((R,G,B)).astype(np.uint8)
    else:
      res = np.dstack((R,G,B,A)).astype(np.uint8)

    resimg = Image.fromarray(res)
    

    resimg.save(compressed)

        
    return time.time() - start_time
  
def main():
  path = "../static/uploads/cb4bdcfabdf99ea5.png" #e74653fdec5ddc5f.jpg" "static\uploads\
  time = compress(path,path,10)
  print(time)

if __name__ == "__main__":
  main()