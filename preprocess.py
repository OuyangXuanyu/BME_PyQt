'''
    这里存放了预处理的函数
'''

import numpy as np
import pywt
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt 
import matplotlib
import pandas as pd
from scipy import signal 
from scipy.fft import fft, fftfreq





def butter_band_LH(signalInput,flag_filter_analysis,fs,cutoff_freq_high=0.2,cutoff_freq_low=100 ):
    '''if analysis the filter first low second high'''
    b_low, a_low = signal.iirfilter(N=5, Wn=cutoff_freq_low/(fs/2), btype='low', ftype='butter')  
    filtered_signal_low = signal.lfilter(b_low, a_low, signalInput)  
    
    b_high, a_high = signal.iirfilter(N=5, Wn=cutoff_freq_high/(fs/2), btype='high', ftype='butter')  
    filtered_signal_high = signal.lfilter(b_high, a_high, filtered_signal_low)  
    if flag_filter_analysis:
        filterAnalysis(b_low, a_low,fs)
        filterAnalysis(b_high, a_high,fs)
    return filtered_signal_high

def butter_band_Low(signalInput,flag_filter_analysis,fs,cutoff_freq_low=100):
    '''if analysis the filter first low second high'''
    b_low, a_low = signal.iirfilter(N=5, Wn=cutoff_freq_low/(fs/2), btype='low', ftype='butter')  
    filtered_signal_low = signal.lfilter(b_low, a_low, signalInput)  
    
    if flag_filter_analysis:
        filterAnalysis(b_low, a_low,fs)
    return filtered_signal_low

def filterAnalysis(b,a,sr):
    '''
    b为分母,a为分子 列表形式给出,sr为采样率
    '''
    w, h = signal.freqz(b, a)  
    mag_response = 20 * np.log10(np.abs(h)) 
    plt.figure(figsize=(10, 5))  
    plt.plot(w / (np.pi*2)*sr, mag_response)  
    plt.title('Magnitude Frequency Response')  
    plt.xlabel('Frequency (Hz)')  
    plt.ylabel('Magnitude (dB)')  
    plt.grid(True)  
    plt.show() 
    zeros = np.roots(b)  
    poles = np.roots(a) 
    plt.figure(figsize=(5, 5))    
    ax = plt.gca()   
    ax.set_aspect('equal', 'box')   
    ax.spines['left'].set_position('zero')   
    ax.spines['bottom'].set_position('zero')    
    ax.spines['right'].set_color('none')    
    ax.spines['top'].set_color('none')    
    ax.xaxis.set_ticks_position('bottom')   
    ax.yaxis.set_ticks_position('left')    
    ax.set_xlim(-3, 3)    
    ax.set_ylim(-3, 3)     
    plt.plot(zeros.real, zeros.imag, 'o', label='Zeros', markersize=8)  
    plt.plot(poles.real, poles.imag, 'x', label='Poles', markersize=8)  
    unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linewidth=3)  
    ax.add_patch(unit_circle)  
    plt.title('Pole-Zero Plot on the Unit Circle')  
    plt.xlabel('Real')  
    plt.ylabel('Imag')  
    plt.legend()   
    plt.grid(True)    
    plt.show()


'''
    ---------以上是lgx提供的函数，不过都没用上-------------
'''

'''
    封装适用于该数据ECG信号预处理的函数
'''
import os
import pyedflib
import matplotlib.pyplot as plt
import numpy as np

'''
    函数名称：bandstop_filter
    功能：带阻滤波器
    输入：data-原始数据，lowcut下截止，highcut上截止，fs采样率，order阶数
    输出：经过带阻滤波器之后的数据
    使用例子：filtered_data = bandstop_filter(ECG_try,59,61,256)
'''

def bandstop_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='bandstop')
    y = filtfilt(b, a, data)
    return y

'''
    函数名称：medfilt_ecg
    功能：中值滤波去除基线漂移
    输入：original_ecg-原始数据，window_size窗函数大小
    输出：经过中值滤波之后的数据
    参考链接：https://blog.csdn.net/chrnhao/article/details/120420343
    使用例子：
    fliter = int(0.8*256)
    final_filtered_ecg = medfilt_ecg(filtered_data, fliter)
'''
import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import medfilt
from preprocess import butter_band_Low
from numpy import polyfit, polyval
def medfilt_ecg(original_ecg, window_size):
    # 确保窗大小变为奇数 
    fliter = int(0.8*256)
    window_size = window_size+1 if window_size % 2 == 0 else window_size
    give_up_size = int(fliter / 2)
    ecg_baseline = medfilt(original_ecg, window_size)
    totality_bias = np.sum(ecg_baseline[give_up_size:-give_up_size])/(len(original_ecg)-2*give_up_size)
    filtered_ecg = original_ecg - ecg_baseline
    final_filtered_ecg = filtered_ecg[give_up_size:-give_up_size]-totality_bias
    return final_filtered_ecg


'''
    函数名称loss_fliter
    功能：巴特沃斯低通滤波
    输入：data-原始数据，frequency-采样率，highpass截止频率
    输出：经过低通滤波之后的数据
    参考链接：https://blog.csdn.net/chrnhao/article/details/124941513
    使用例子：
    fliter_ecg = loss_fliter(final_filtered_ecg)#滤波
'''
#Frequence 为信号的采样频率
#highpass 低通滤波器可以通过的最高频率

def loss_fliter(data, frequency=256, highpass=35):
    [b, a] = signal.butter(2, highpass / frequency * 2, 'lowpass')
    Signal_pro = signal.filtfilt(b, a, data)
    return Signal_pro


'''
    函数名称high_fliter
    功能：巴特沃斯高通滤波
    输入：data-原始数据，frequency-采样率，lowpass截止频率
    输出：经过高通滤波之后的数据
    参考链接：https://blog.csdn.net/chrnhao/article/details/124941513
    使用例子：
    fliter_ecg_2 = high_fliter(fliter_ecg)#滤波
'''
#Frequence 为信号的采样频率
#lowpass 高通滤波器可以通过的最低频率

def high_fliter(data, frequency=256, lowpass=0.5):
	#3是滤波器阶数 
	#lowpass / frequency * 2 计算机截至频率
	#[b, a]为设计好的滤波器的系统函数的系数
    [b, a] = signal.butter(2, lowpass / frequency * 2, 'highpass')
	# 将设计好的系数和待滤波的信号扔进filtfilt中返回值为滤波之后的结果
    Signal_pro = signal.filtfilt(b, a, data)
    return Signal_pro



def FFT(Fs, data):
    """
    对输入信号进行FFT
    :param Fs:  采样频率
    :param data:待FFT的序列
    :return:
    使用例子：
    x_ditong,result_ditong = FFT(256,fliter_ecg)
    # 绘制频谱图
    plt.figure(figsize=(16, 9))
    plt.plot(x_ditong, result_ditong)
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title('Spectrum of data_full')
    plt.show()
    """
    L = len(data)  # 信号长度
    N = np.power(2, np.ceil(np.log2(L)))  # 下一个最近二次幂，也即N个点的FFT
    result = np.abs(fft(x=data, n=int(N))) / L * 2  # N点FFT
    axisFreq = np.arange(int(N / 2)) * Fs / N  # 频率坐标
    result = result[range(int(N / 2))]  # 因为图形对称，所以取一半
    return axisFreq, result

'''
    函数名称：带阻滤波器
    用于去除工频干扰
    filtered_data = bandstop_filter(ECG_try,59,61,256)
'''
def bandstop_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='bandstop')
    y = filtfilt(b, a, data)
    return y
