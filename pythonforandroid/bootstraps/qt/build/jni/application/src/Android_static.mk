LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := main_x86_64

LOCAL_SRC_FILES := start.c

# LOCAL_STATIC_LIBRARIES := SDL2_static

include $(BUILD_SHARED_LIBRARY)
# $(call import-module,SDL)LOCAL_PATH := $(call my-dir)
