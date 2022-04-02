import numpy as np

def calculate(list):

    min_values = 9
    try:
        nm_list = np.array(list)
        n = nm_list.reshape(3, 3)
        nf = nm_list.flatten()

    except:
        raise ValueError ("List must contain nine numbers.") 

      
    #add to dictionary function
    calculations = {}

    def add_to(name, array):
        lst = [i.tolist() for i in array]

        calculations[name] = lst


    #create the matrix with the correct dimensions
    nm_list = np.array(list)
    n = nm_list.reshape(3, 3)
    nf = nm_list.flatten()


    #mean
    c_mean = np.mean(n, axis=0)
    r_mean = np.mean(n, axis=1)
    t_mean = np.mean(nf)
    m = [c_mean, r_mean, t_mean]

    add_to('mean', m)

    #variance
    c_var = np.var(n, axis=0)
    r_var = np.var(n, axis=1)
    t_var = np.var(nf)
    v = [c_var, r_var, t_var]

    add_to('variance', v)

    #standard deviation
    c_std = np.std(n, axis=0)
    r_std = np.std(n, axis=1)
    t_std = np.std(nf)
    s = [c_std, r_std, t_std]

    add_to('standard deviation', s)

    #max

    c_max = np.max(n, axis=0)
    r_max = np.max(n, axis=1)
    t_max = np.max(nf)
    m = [c_max, r_max, t_max]

    add_to('max', m)

    #min

    c_min = np.min(n, axis=0)
    r_min = np.min(n, axis=1)
    t_min = np.min(nf)
    mn = [c_min, r_min, t_min]

    add_to('min', mn)


    #sum
    c_sum = np.sum(n, axis=0)
    r_sum = np.sum(n, axis=1)
    t_sum = np.sum(nf)
    sm = [c_sum, r_sum, t_sum]

    add_to('sum', sm)








    return calculations
