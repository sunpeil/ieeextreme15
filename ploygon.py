import numpy as np

if __name__ == '__main__':
    T = int(input())
    for iii in range(T):
        N = int(input())
        # N边形
        x = np.zeros(N)
        y = np.zeros(N)
        z = np.zeros(N)
        for k in range(N):
          x[k], y[k], z[k] = [int(i) for i in input().split(" ")]
        # 用