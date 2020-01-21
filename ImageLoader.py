from ctypes import *
import ctypes as C

jaiFactoryDLL = cdll.LoadLibrary("C:/Program Files/JAI/SDK/bin/Jai_Factory")

FACTORY_HANDLE = C.pointer(C.c_int())
CAM_HANDLE = C.c_void_p()
STREAM_HANDLE = C.c_void_p()

J_CAMERA_ID_SIZE = 512
m_bEnableStreaming = False

m_sCameraId = []
for i in range(J_CAMERA_ID_SIZE):
	m_sCameraId.append(C.c_int8(0))

bHasChange = C.c_bool()
iSize = C.c_uint32()
iNumDev = C.c_uint32()


jaiFactoryDLL.J_Factory_Open.argtypes = [POINTER(c_char), POINTER(C.c_int)]
jaiFactoryDLL.J_Factory_UpdateCameraList.argtypes = [POINTER(C.c_int), POINTER(C.c_bool)]


def J_Factory_Open(data, factoryHandle):
	return jaiFactoryDLL.J_Factory_Open(byref(data), byref(factoryHandle.contents))


def J_Factory_UpdateCameraList(factoryHandle, bData):
	return jaiFactoryDLL.J_Factory_UpdateCameraList(byref(factoryHandle.contents), byref(bData))


def openFactoryAndCamera():

	retval = J_Factory_Open(C.c_char(1), FACTORY_HANDLE)
	if retval != 0:  # 0 is the return code for success
		print("Could not open factory!")
		print(retval)

	print(FACTORY_HANDLE.contents)
	print(bHasChange.value)

	retval = J_Factory_UpdateCameraList(FACTORY_HANDLE, bHasChange)
	if retval != 0:  # 0 is the return code for success
		print("Could not update camera list!")

	retval = jaiFactoryDLL.J_Factory_GetNumOfCameras(FACTORY_HANDLE, POINTER(iNumDev))
	if retval != 0:  # 0 is the return code for success
		print("Could not get number of cameras!")

	if iNumDev.value == 0:
		print("Invalid number of cameras!")

	iSize = C.c_uint32(J_CAMERA_ID_SIZE)
	retval = jaiFactoryDLL.J_Factory_GetCameraIDByIndex(FACTORY_HANDLE, 0, m_sCameraId, POINTER(iSize))
	if retval != 0:
		print("Could not get the camera ID!")

	retval = jaiFactoryDLL.J_Camera_Open(FACTORY_HANDLE, m_sCameraId, POINTER(CAM_HANDLE))
	if retval != 0:
		print("Could not open the camera!")

	numStreams = C.c_uint32(0)
	retval = jaiFactoryDLL.J_Camera_GetNumOfDataStreams(CAM_HANDLE, POINTER(numStreams))
	if retval != 0:
		print("Error with J_Camera_GetNumOfDataStreams.")

	if 0 == numStreams:
		m_bEnableStreaming = False
	else:
		m_bEnableStreaming = True

	if iNumDev.value > 0:
		print("Opening camera succeeded!")
	else:
		print("Invalid number of Devices!")
		return False

	return True


openFactoryAndCamera()
