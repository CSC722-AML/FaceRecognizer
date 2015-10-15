# FaceRecognizer

###Introduction:
Facial recognition, is the identification of a specific individual in an image or video stream is gaining importance. It is adding to the list of biometrics used to secure and identify individuals, such as fingerprints, palm prints and iris.  
Facial recognition systems were originally conceptualized for security purposes in order to flag individuals at, for example, airports or political gatherings which would involve a massive number of people. However, the use of these systems is not limited to this field any more and they are being used in other applications such as Facebook’s feature of tagging and suggesting friends whenever a user uploads a photo.  
A facial recognition system involves extraction of distinguishing features from an image of the face of the individual. These features could include the endpoints of various parts of the face, for example, the edges of the mouth, or the eyes. Features such as the depth of the eye sockets, distance between the eyebrows and the eyes, the length or width of the nose, the structure of the jaw bones and the shape of the chin can also be considered. Such features are extracted from more than one image of the individual and are stored in a datastore. Using these features, the system learns to distinguish between individuals. When a new image is encountered, the system identifies the individual based on what it has learnt so far and on correct identification, adds the features obtained from this image to the datastore and adapts to improve its knowledge.

###Project Description:
We propose to build a face recognition system which will be capable to learn and recognize multiple faces. We plan to experiment with multiple feature sets (which are popular in the field of face detection) such as HAAR features, Fisherfaces, etc and construct a robust model which would efficiently discriminate between these points for different faces. We will exploit these features with different machine learning algorithms like k-means, SVM, deep nets, etc. to develop a tunable algorithm (through parameters) which will work equally well with different feature sets and learning algorithms. We will incorporate the feature extractors from OpenCV and later work on the multidimensional representation obtained for each face.  
We decided to use features rather than templates, as comparisons using templates underperform for images with different resolutions. Also, use of features helps us to determine key points and speed up calculations to detect faces.

###Approach:
1. For building the model, we will be using the Yale Face Database[1]. This database contains 165 gray-scale images of 15 individuals in different angles. 
2. For 150 images from the dataset, we will extract the haar features for each image using OpenCV[3]. OpenCV is an open source computer vision library which contains multiple feature extractors.  
3. Using the extracted features, we can either reduce the dimensions of the feature space or use the entire feature space to build a supervised learner for each face. The choice of the supervised learner will be part of our experiment.  
4. Using the constructed model, we then try to identify the 15 remaining images which we did not use to construct the model. This can be repeated as a 11 fold leave cross validation experiment to measure the efficiency of the model.  

###References:

1. Yale Face Database ![http://vision.ucsd.edu/content/yale-face-database](http://vision.ucsd.edu/content/yale-face-database)
2. Face Recognition: ![Features Versus Templates, http://www.researchgate.net/profile/Tomaso_Poggio/publication/3192217_Face_recognition_features_versus_templates/links/09e4150e6e9231f489000000.pdf](Features Versus Templates, http://www.researchgate.net/profile/Tomaso_Poggio/publication/3192217_Face_recognition_features_versus_templates/links/09e4150e6e9231f489000000.pdf)
3. OpenCV, Open-source Computer Vision, [http://opencv.org/](http://opencv.org/)