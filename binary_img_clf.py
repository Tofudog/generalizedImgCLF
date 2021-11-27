import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from keras.models import Sequential
from keras.layers import Conv2D ,MaxPooling2D, Dropout, Flatten,\
Dense,Activation,BatchNormalization,Input

import numpy as np
from scipy import interp
from itertools import cycle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import roc_auc_score

from zipfile import ZipFile

parent_dir = "kagglecatsanddogs_3367a.zip"
kaggle = ZipFile(parent_dir)

class CreateModel:
    
    # Part of *args is train_datagen and test_datagen
    def __init__(self, data, **kwargs):
        self.data = data
        self.train_datagen = None
        self.val_datagen = None
        
        # Iter through dict is auto through keys
        for key in kwargs:
            if key=="train_datagen":
                self.train_datagen = kwargs.get(key)
            elif key in "val_datagen":
                self.val_datagen = kwargs.get(key)
        
    
    def setData(self, parent_dir, image_dir, locate_dir):
        assert (train_datagen is None) and (val_datagen is None)
        
        if (parent_dir[-4:] == ".zip"):
            from zipfile import ZipFile
            file = ZipFile(parent_dir)
            file.extractall(image_dir)
            # Classes dog and cat split eff
            
            
    def getDatagen(self, ):
        
    

class BinaryClassifier:
    
    def __init__(self, model):
        self.model = model
    
    def __repr__(self):
        try:
            return self.model.summary()
        except NameError as ne:
            print("It is ne")
        except Exception as e:
            print(f"{type(e)}: Something went wrong")
            
    def __del__(self):
        pass
    
    # Possibly more layers or another hyperparam when mult
    def __mul__(self, other):
        pass

    def next(*args):
        pass


def main():
    pass

if __name__ == '__main__':
    main()




































      
      
      
      
      
    