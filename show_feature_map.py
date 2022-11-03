import torch
import cv2
import os
import numpy as np

def catch_feature_map(feature_map,layername:str):
    feature_size=feature_map.shape  #B,C,H,W
    save_dir = rf'./feature_map_results/{layername}'
    os.makedirs(save_dir, exist_ok=True)
    img = tensor_to_mat(feature_map)
    for n in range(feature_size[1]):
        image_name = rf'{save_dir}/{n}.png'
        cv2.imwrite(image_name,img[:,:,n])


def tensor_to_mat(img_tensor):
    img_tensor1=img_tensor.cpu().permute(0,2,3,1).contiguous().numpy()  #to N*C*H*W
    size_np=img_tensor1.shape
    img_mat=(img_tensor1[0:,:,:]*255).reshape(size_np[1],size_np[2],size_np[3]).astype('uint8')
    return img_mat
