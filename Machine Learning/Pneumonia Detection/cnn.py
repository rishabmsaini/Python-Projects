# Convolutional Neural Network
# Part 1 - Building the CNN
# Importing the Keras libraries and packages
from keras.models import Sequential # To initialize our NN
from keras.layers import Conv2D # To add convolutional layers
from keras.layers import MaxPooling2D # To add pooling layers
from keras.layers import Flatten # Convert pool feature map into row feature vector
from keras.layers import Dense # Used to add a fully connected layer into classic ANN
from keras.layers import Dropout # Used to avoid overfitting of dataset

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
# add() method adds a convolution layer
# Conv2D(no_of_filters,(size_of_filter),input_shape=(n,n,3),activation='name_of_activation_layer')
classifier.add(Conv2D(32, (3, 3), input_shape = (128, 128, 3), activation = 'relu'))

# Step 2 - Pooling
# MaxPooling2D( pool_size = (m,m))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a 2 more convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Conv2D(64, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images
# ImageDataGenerator avoids overfitting
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, 
                                   horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set', target_size = (128, 128), 
                                                 batch_size = 16, class_mode = 'binary')
test_set = test_datagen.flow_from_directory('dataset/test_set', target_size = (128, 128), 
                                            batch_size = 16, class_mode = 'binary')

classifier.fit_generator(training_set, steps_per_epoch = 2000, epochs = 5, 
                         validation_data = test_set, validation_steps = 400)

# Save model architecture to a single file
classifier.save("classifier.h5")
print("Saved model to disk.")
