# Homework 5_Curtis Lin

## Questions

### What is TensorFlow? Which company is the leading contributor to TensorFlow?

- TensorFlow is a free and open-source software library for deep learning applications such as neural networks.

- Google is the leading contributor.

### What is TensorRT? How is it different from TensorFlow?

- NVIDIA TensorRT™ is an SDK for high-performance deep learning inference. It includes a deep learning inference optimizer and runtime that delivers low latency and high-throughput for deep learning inference applications (from Nvidia).

What is ImageNet? How many images does it contain? How many classes?

- ImageNet is an image database organized according to the WordNet hierarchy (from ImageNet)

- ImageNet contains 14 million images (from wiki)

- ImageNet contains more than 20,000 categories (from wiki)

### Please research and explain the differences between MobileNet and GoogleNet (Inception) architectures.

- GoogLeNet is a deep convolutional neural network architecture codenamed Inception that achieve classification and detection. Their architecture consisted of a 22 layer deep CNN which contains 4 million parameters.

- MobileNets, a family of mobile-first computer vision models for TensorFlow, designed to effectively maximize accuracy while being mindful of the restricted resources for an on-device or embedded application (from Google) 

- GoogLeNet requires large computational resources. On the other hand, MobileNets is to maximize accuracy with limited computational resources. 

### In your own words, what is a bottleneck?

- Computational resouces for training large dataset with neural network

### How is a bottleneck different from the concept of layer freezing?

- Layer freezing means layer weights of a trained model are not changed when they are reused in a subsequent downstream task (from Quora). With layer freezing, the trained model can be reused for making prediction of other dataset. Therefore, layer freezing can reduce the usage of computational resources.  

### In part one this lab, you trained the last layer (all the previous layers retain their already-trained state). Explain how the lab used the previous layers (where did they come from? how were they used in the process?)

- The lab uses the previous layers from TensorFlow Hub with tf.keras

- We use `hub.module` to load a mobilenet, and `tf.keras.layers.Lambda` to wrap it up as a keras layer

### Why is the batch size important? What happens if you try running with a batch size of 32? What about a batch size of 4?

- Batch size indicates how many data you would like to train at one time. The large batch results in better  accurate of the estimatation of the gradient. However, large batch size requires more memory. Therefore, running batch size of 4 may show less accuracy.

### -----------------------------------------------
### Not completed yet

### Find another image classification feature vector from tfhub.dev and rerun the notebook. Which one did you pick and what changes, if any did you need to make?

### How long did the training take in part 2?

### In part 2, you can also specifiy the learning rate using the flag --learning_rate. How does a low --learning_rate (part 2, step 4) value (like 0.001) affect the precision? How much longer does training take?

### How about a --learning_rate (part 2, step 4) of 1.0? Is the precision still good enough?

### For part 2, step 5, How accurate was your model? Were you able to train it using a few images, or did you need a lot?
