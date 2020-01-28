#Define the maximum entropy thresholding function 
def max_entropy(im_arr, mask_arr):

    """Maximum entropy thresholding function 
    Inputs:
    im_arr: array,
        the mr image array
    mask_arr: array
        the binary mask array
        
    Outputs:   
    threshold_val: float,
        the threshold value
    """
    #Convert intensity values into int values
    im_arr = im_arr.astype(int)
    
    #List of intensity values
    vals = list(np.unique(im_arr[mask_arr == 1]))  
    vals_hist = list(np.copy(vals))   
    vals_hist.append(max(vals) + 1)

    #Compute the image histogram
    hist, bin_edges = np.histogram(im_arr[mask_arr == 1], bins=vals_hist)

    #Normalize the histogram
    p_i = hist / hist.sum()
    
    #Test each threshold value partionning the histogram into 2 classes
    e_thresh = []
    for cnt, threshold_val in enumerate(vals[0:len(vals) - 1]):
        s0 = p_i[0:cnt + 1].sum()
        e0 = -(p_i[0:cnt + 1] / s0 * np.log(p_i[0:cnt + 1] / s0)).sum()
        s1 = p_i[cnt + 1:].sum()
        e1 = -(p_i[cnt + 1:] / s1 * np.log(p_i[cnt + 1:] / s1)).sum()
        e_tot = e0 + e1
        e_thresh.append(e_tot)
    threshold_val = vals[np.argmax(e_thresh)]
    
    return threshold_val
