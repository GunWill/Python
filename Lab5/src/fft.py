import numpy as np

def fft(x):
    #Computes FFT of a 1-D array using Cooley Tukey
    x = np.asarray(x, dtype = complex) #Converts input to a numpy array of complex numbers for complex math
    N = len(x) #Numbers of input samples

    
    if N == 0: #If array is empty, raise an erorr - need at minimum one sample
        raise ValueError("Input array must not be empty") 

    if (N & (N-1)) != 0: #Use bitwise AND to see if len(x) is a power of 2
        raise ValueError(f"Input length {N} is not a power of 2, requires power of two length")

    if N <= 1:
        return x.copy() #FFT of a single sample is the sample

    bits = int(np.log2(N)) #Calculate how many bits are needed for bit reversal permutation

    indices = np.zeros(N, dtype=int)
    for i in range(N):
        #Convert i to a binary string of bits, reverse it, convert back to int
        indices[i] = int(f"{i:0{bits}b}"[::-1], 2)
    x = x[indices] #Reorder according to reversed indices

    #Setp 2: Iterative butterfly stages
    s=1
    while(1 << s) <=N:
        #m is the size of the butterfly group
        m = 1 << s

        #wm is twiddle factor base
        wm = np.exp(-2j * np.pi / m)

        #Iterate over each group in the array
        for k in range(0, N, m):
            #w starts at 1
            w = 1.0 + 0j

            for j in range(m//2):
                t = w * x[k + j + m //2]
                u = x[k +j]

                # Butterfly operation:
                x[k + j] = u + t #even indexed value is the u + t

                x[k + j + m //2] = u-t #odd indexed value is u - t

                w *= wm

        s += 1 #Move to the next stage

    return x #Return final result

    
    