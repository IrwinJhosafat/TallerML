import sys
from tensorflow import keras

MODEL_PATH= 'pulsar_model.h5'

#Load TensorFlow Model
model = keras.models.load_model(MODEL_PATH)
print(model.summary())

if len(sys.argv) > 0:
    arguments = sys.argv[1:]

    #Process the arguments
    print(arguments)
    params = [arguments]
    print(model.predict(arguments))
else:
    print("No hay parametros")
    
    