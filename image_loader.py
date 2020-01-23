from ctypes import *
import ctypes as c

pv_stream_dll = cdll.LoadLibrary("C:/Users/petersk/Desktop/SDK/PvStreamSample")

#pv_stream_dll.SelectAndConnectToDevice.argtypes = []
#pv_stream_dll.OpenStreamAndAcquireImages.argtypes = []
#pv_stream_dll.DisconnectFromDevice.argtypes = []

def select_and_connect_to_device():
	""" Detect cameras and attempt to connect to one.
	:return: True if successful, False if not
	"""

	retval = pv_stream_dll.SelectAndConnectToDevice()
	if retval != 0:  # 0 is the return code for success
		print("Could not connect to device!")
		return False

	return True


def open_stream_and_acquire_images():
	""" Open a stream from a camera and get images from it.
	:return: True if successful, False if not
	"""

	retval = pv_stream_dll.OpenStreamAndAquireImages()
	if retval != 0:
		print("Could not open stream!")
		return False

	return True


def disconnect_from_device():
	""" Disconnect from a camera that we are already connected to.
	:return: True if successful, False if not
	"""

	retval =  pv_stream_dll.DisconnectFromDevice()
	if retval != 0:
		print("Could not disconnect from device!")
		return False

	return True
