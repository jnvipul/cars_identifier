# Car Identifier

## Objective
Automate the process of recognizing the details of the cars from images, including make and model. 
<br>*Build and Deploy a Deep Learning model as a publicaly API endpoint on a clould provider.*

## Tasks Completed
- Train a deep learning model to identify car details
- Wrap above model in a python flask app
- Dockerised the flask app
- Docker container deployed on a Google Cloud VM instance
- Created Open API specification for the same

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

## Training
- 

## Code
All python code is [PEP8 complaint](https://www.python.org/dev/peps/pep-0008/).

### Packaging
The model is wrapped in a [python flask](http://flask.pocoo.org/) app which serves the prediction as an api endpoint. 
<br> Flask app has been dockerised using [docker.io]
(docker.io)
<br>
API specification has been created using [Open API 3.0](https://swagger.io/blog/news/announcing-openapi-3-0/)

### Deployment
Docker container has been deployed on a GCP VM instance.


## Running the code
**Step 1.** Navigate to <b>*vipul_jain/flask*</b> <br>
**Step 2.** Build docker image with the command below -:
```
docker build -t vj_cars .
```
<br>
**Step 3.** Run docker container with the command below
```
docker run -d -p 80:4000 vj_cars
```
<br>
**Step 4.** Confirm if container is running with the command below -: 
```
docker ps
```