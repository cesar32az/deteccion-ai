import cv2
import numpy as np
import tensorflow_hub as hub 
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import get_file 

MODELS = {
    'inception_resnet_v2': ('google/imagenet/resnet_v2_152/classification/4', (224, 224, 3)),
    'inception_v3': ('google/tf2-preview/inception_v3/classification/4', (299, 299, 3)),
    'resnet50': ('google/imagenet/resnet_v2_50/classification/4', (224, 224, 3))
}


def deteccion(file):
    #dir = pathlib.Path().parent.absolute()
    dir = '/home/julio/umg/inteligencia-artificial/proyecto-final-ai/backend-ai/upload'
    img_path = f'{dir}/{file.filename}'
    print(img_path)

    model_uri, input_shape = MODELS['inception_v3']
    classifier_url = f'https://tfhub.dev/{model_uri}'
    model = Sequential([
        hub.KerasLayer(classifier_url, input_shape=input_shape)
    ])
    
    image = cv2.imread(img_path)
    #cv2.imshow('imagen analizada', image)  
    #cv2.waitKey(0)  
    
    image_copy = image.copy()
    image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
    image_copy = cv2.resize(image_copy,
                            model.input_shape[1:-1],
                            interpolation=cv2.INTER_AREA)
    image_copy = image_copy / 255.0
    image_copy = np.expand_dims(image_copy, axis=0)

    predictions = model.predict(image_copy)
    predicted_index = np.argmax(predictions[0], axis=-1)

    file_name = 'ImageNetLabels.txt'
    file_url = 'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'
    labels_path = get_file(file_name, file_url)

    with open(labels_path) as f:
        imagenet_labels = np.array(f.read().splitlines())

    best_label = imagenet_labels[predicted_index]
    #cv2.imshow(f'{best_label}', image)
    #cv2.waitKey(0)

    return best_label
    
