#Define the maximum entropy thresholding function 
def max_entropy(seg_arr, gt_arr, spacings):

     d_gt_seg = ndimage.morphology.distance_transform_edt(1 - seg_arr,
                                                          sampling=spacings)
     d_seg_gt = ndimage.morphology.distance_transform_edt(1 - gt_arr,
                                                          sampling=spacings)
     score = np.max([d_gt_seg[gt_arr == 1].max(), d_seg_gt[seg_arr == 1]].max())
    return score
