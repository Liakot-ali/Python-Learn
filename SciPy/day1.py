import scipy.special as ss
import scipy.fftpack as sf
import numpy as np
a = ss.exp10(45)
b = ss.sindg(10)
print(a, b)

# fourier transform
x = np.array([1, 2, 3, 4])
nf = sf.fft(x)
ifft = sf.ifft(x)
print(nf, ifft)