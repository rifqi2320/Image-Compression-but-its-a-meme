from PIL import Image
import numpy as np
import time

def compress(Mx, percent):
  U , S, Vt = np.linalg.svd(np.array(Mx).astype(float))
  N, _ = U.shape
  M, _ = Vt.shape
  U = [[U[j,i] if i < N * percent else 0 for i in range(N)] for j in range(N)]
  S = np.array([[S[i] if i == j else 0 for i in range(len(Vt))] for j in range(len(U))])
  Vt = [[Vt[j, i] if j < M * percent else 0 for i in range(M)] for j in range(M)]
  return np.asarray(np.around(U @ S @ Vt), dtype="uint8")

if __name__ == "__main__":
  start_time = time.time()
  nfile = input() # ganti input
  img_array = np.asarray(Image.open(nfile))
  R = [[x[0] for x in N] for N in img_array]
  G = [[x[1] for x in N] for N in img_array]
  B = [[x[2] for x in N] for N in img_array]
  percent = int(input())/100 # ganti input
  R = compress(R, percent)
  G = compress(G, percent)
  B = compress(B, percent)
  if (nfile.split(".")[-1]) == "png":
    A = [[x[3] for x in N] for N in img_array]
    res = np.array([[[R[i][j], G[i][j], B[i][j], A[i][j]] for j in range(len(R[0]))] for i in range(len(R))])
  else:
    res = np.array([[[R[i][j], G[i][j], B[i][j]] for j in range(len(R[0]))] for i in range(len(R))])
  print(f"Shape of image is: {len(R)}x{len(R[0])}")
  Image.fromarray(res).save(".".join(nfile.split(".")[:-1]) + "_reduced."+ nfile.split(".")[-1])
  print("Time taken: {:.2f} seconds".format(time.time() - start_time))
  
  