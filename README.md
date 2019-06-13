# Car Identifier

## Objective
Automate the process of recognizing the details of the cars from images, including make and model. 
<br>*Build and Deploy a Deep Learning model as a publicaly API endpoint on a clould provider.*

## Tasks Completed
- Trained a deep learning model to identify car details
- Wrap above model in a python flask app
- Created a vanilla UI to upload a picture from browser and perform predictions
- Dockerised the flask web app
- Docker container deployed on a Google Cloud VM instance
- Created Open API specification for the same using Swagger 

## Dataset
Training and testing has been done using [Stanford Cars 196 dataset]()

Note : The `dataset` folder is is expected to have train and test images in `cars_train` and 'cars_test' folder respectively. These folders are not committed to git to to large sizes.

## URLs

* [Prediction Link](http://tensortaal.com/cars/v1/get_car_details)
```
(http://tensortaal.com/cars/v1/get_car_details)
```

* [Open API Documentation Link] (http://tensortaal.com/swagger/)
```
(http://tensortaal.com/swagger/)
```

* [Git Repository] (https://github.com/jnvipul/cars_identifier/tree/master)
```
(https://github.com/jnvipul/cars_identifier/tree/master)
```

## Training thought process

Training code can be found in the notebook `trainer.ipynb`

### Transfer Learning
I have used Transfer Learning with Resnet152 to train the model; training frozen layers as well.

####  Model Architechture - Resnet152
This is a very complicated problem, and thus we need a big and complex network for the same. Thats the reason Resnet152 is used for transfer learning. Resnet50 and Resnet34 have also been tried, Resnet152 has better performance among all.

### Learning Rate selection
For learning rate selection, **Cycling learning rates** has been used as per the [paper by Leslie Smith](https://arxiv.org/abs/1506.01186).
Idea is to cycle the learning rate between lower bound and upper bound in order to escape local minima and saddle points. 
<br>
Quick explanation of Cyclic learning rates can be found on the article I recently published on [Towards Data Science](https://towardsdatascience.com/cyclical-learning-rates-the-ultimate-guide-for-setting-learning-rates-for-neural-networks-3104e906f0ae)

### Feature Engineering - Data Augmentation
Data Augmentation techniques have been used and experimented for the kind of data we have. For instance; for car pictures - **warp(perspective), rotation, flips, zoom, lightning** are good augmentation technique; and improved the results.
<br>
Tried more augmentaion techniques like **Jitter, Crop-Pad etc** but the didn't seem to improve the model as of now. <br>
(More experimentation and study could be done here)

### Epoch Counts
Number of epochs have been heavily experimented and then chosen wisely to find a good trade-off between underfitting and overfitting.

## Code
All python code is [PEP8 complaint](https://www.python.org/dev/peps/pep-0008/).

### Packaging
Inference code is packaged in a python module using [python flask](http://flask.pocoo.org/) app which serves the prediction as an api endpoint. 
<br> Flask app has been dockerised using [docker.io]
(docker.io)
<br>
API specification has been created using [Open API 3.0](https://swagger.io/blog/news/announcing-openapi-3-0/)

### Deployment
Docker container has been deployed on a GCP VM instance.


## Running the code
**Step 1.** Navigate to <b>*cars/identifier/flask*</b> <br>
**Step 2.** Build docker image with the command below -:
```
docker build -t vj_cars .
```

**Step 3.** Run docker container with the command below
```
docker run -d -p 80:4000 vj_cars
```
**Step 4.** Confirm if container is running with the command below -: 
```
docker ps
```

## Results
Final model has an accuracy of `~85%` on test set.

## Verdict
Upon analyzing the top losses, the model predicts wrong class in the cases when muliple cars looks very similar from that angle or mostly in the cases when we have a back picture of the car, where it is very difficult to identify the car. 
<br>
More images and high quality data can be used to improve the model.

## Things I would do further
- Dataset is a bit skewed towards a few car models, work on class imbalance issue 
- Explore and experiment more with Data Augmentation techniques
- Try a different policy of cyclic learning rate
- Add a monitoring service like datadog/newrelic
- Exhaustive error handling and test cases