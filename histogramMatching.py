from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
img1 = Image.open('./Photo/Lenna.png')
img2 = Image.open('./Photo/Test2.jpg')
img1 = np.array(img1)
img2 = np.array(img2)
def trans(img):
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def histogram(img):
    Hist = [0 for _ in range(0,256)]
    Hist = np.array(Hist)
    
    for i in range(np.shape(img)[0]):
        for j in range(np.shape(img)[1]):
            Hist[int(img[i][j])] += 1 
            
    return Hist
def sum_Hist(Hist):
    sum_Hist = [0 for _ in range(0,256)]
    s = 0
    for i in range(0,256):
        s += Hist[i]
        sum_Hist[i] = s
    return sum_Hist

def norm_Hist(Hist):
    num_pixel = Hist[255]
    norm = [0 for _ in range(0,256)]
    for i in range(0,256):
        norm[i] = Hist[i] * 255.0 / num_pixel 
    return norm

def hist_mapping(img,Hist):
    print(np.shape(img)[0],'*',np.shape(img)[1])
    Hist_mapping_img = [[0 for _ in range(0,np.shape(img)[1])] for _ in range(0,np.shape(img)[0])]
    for i in range(np.shape(img)[0]):
        for j in range(np.shape(img)[1]):
            Hist_mapping_img[i][j] = int(Hist[int(img[i][j])])
    return Hist_mapping_img

def get_inverse(Hist1,Hist2):
    lookup = [0 for _ in range(0,256)]
    for i in range(0,256):
        k = 255
        while Hist1[k] > Hist2[i]:
            k -= 1
            if k < 0:
                lookup[i] = 0
                break
        else:
            lookup[i] = k
    return lookup
def hist_match(target_img,reference_img):
    norm_hist1 = norm_Hist(sum_Hist(histogram(trans(target_img))))
    norm_hist2 = norm_Hist(sum_Hist(histogram(trans(reference_img))))
    print(np.shape(norm_hist1))  
    print(np.shape(norm_hist2))
    lookup = get_inverse(norm_hist2,norm_hist1)
    return hist_mapping(trans(target_img),lookup)
