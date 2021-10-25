import numpy as np
from scipy.signal import correlate2d

def pool(img,max_d):
    img0 = np.array(img)
    imgres = np.zeros([max_d*3,max_d*3])
    x,y = len(img), len(img[0])
    imgres[max_d:max_d+x,max_d:max_d+y] = img0
    return imgres



def change(img):
    img0=img
    img1=np.fliplr(img)
    img2 = np.flipud(img)
    img3=np.rot90(img0)
    img4 = np.rot90(img1)
    img5 = np.rot90(img2)
    img6 = np.rot90(img3)
    img7= np.rot90(img4)
    img8 = np.rot90(img5)
    img9 = np.rot90(img6)
    img10 = np.rot90(img7)
    img11 = np.rot90(img8)
    return [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11]


if __name__ == '__main__':
    data=[]
    simis=[]
    casenum=int(input())
    n=0;
    while n<casenum:
        img1=[]
        img2=[]
        simi=0
        s=input().split()
        x1=int(s[0])
        y1=int(s[1])
        for a in range(x1):
            ds = []
            for i in input():
                if i == '#':
                    ds.append(1)
                else:
                    ds.append(0)
            img1.append(list(ds))
        s = input().split()
        x2 = int(s[0])
        y2 = int(s[1])
        for a in range(x2):
            ds = []
            for i in input():
                if i == '#':
                    ds.append(1)
                else:
                    ds.append(0)
            img2.append(list(ds))

        if not x1+y1>x2+y2:
            img1,img2=img2,img1
        max_d = max([x1,x2,y1,y2])
        im1,im2 = pool(img1,max_d), pool(img2,max_d)
        for img in change(im1):
            simi=max(simi,correlate2d(img, img2).max())
        simis.append(int(simi))
        n+=1

    for i in simis:
        print(i)