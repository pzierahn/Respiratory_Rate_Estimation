import numpy as np
import scipy.signal as signal


def find_peaks(data: np.ndarray, sample_rate: int, height=None, threshold=None, max_rr=45) -> np.ndarray:
    """
    Find peaks in the data.
    :param data: Respiratory signal
    :param sample_rate: Sampling rate
    :param height: Required height of peaks
    :param threshold: Required threshold of peaks
    :param max_rr: Maximum respiratory rate
    :return: Peaks
    """
    distance = 60 / max_rr * sample_rate

    peaks, _ = signal.find_peaks(
        data,
        height=height,
        threshold=threshold,
        distance=distance)

    return peaks


def frequency_from_peaks(data: np.ndarray, sample_rate: int, height=None, threshold=None, max_rr=45) -> float:
    """
    Peak Counting Method
    :param data:
    :param sample_rate:
    :param height:
    :param threshold:
    :param max_rr:
    :return:
    """

    peaks = find_peaks(data, sample_rate, height, threshold, max_rr)
    return len(peaks) / (len(data) / sample_rate)
