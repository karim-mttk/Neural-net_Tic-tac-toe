from keras.models import Sequential
from keras.layers import Flatten, Dense
import tensorflow as tf

def neural_network(board_state):
    # Define the neural network architecture
    model = Sequential()
    model.add(Flatten(input_shape=(3, 3)))
    model.add(Dense(9, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    # Load the trained weights (assuming they are saved as a file)
    model.load_weights('model_weights.h5')

    # Predict the computer's move using the neural network
    predicted_move = model.predict(board_state.reshape(1, 3, 3)).squeeze()

    # Convert the predicted move to a tuple of row and column numbers
    row, col = divmod(predicted_move.argmax(), 3)

    return row, col
