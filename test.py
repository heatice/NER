# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/16 16:29
@Auth ： ds
@File ：test.py
@IDE ：PyCharm
"""

import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
