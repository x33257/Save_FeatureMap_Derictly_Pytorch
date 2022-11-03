# Save_FeatureMap_Derictly_Pytorch
This is a small and easy tool. You can use this save the feature map in the different layers of you deep learning net.
# How does it work？
It is used for ONE channal GRAY image.
The principle of this code is realy simple。As we know in pytorch the image is saved as tensor。It’s size always is B,C,H,W.
The code transfer the tensor B,C,H,W into cvMat B,H,W,C。then save as images of each channal in cvMat
# You can use it like this

    import show_feature_map as sfm
    sfm.catch_feature_map(input_tensor,name_of_layer)
You can add this at the any layer you want to get the feature map like the bottom picture.
The result will save at rf'./feature_map_results/{name_of_layer}'
![image](https://user-images.githubusercontent.com/54056224/199717362-0da8c09a-2e11-4d8d-94d9-48659c72993e.png)
