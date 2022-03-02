# flask-docker-heroku

This project provides a basic template for creating a flask app that contains an Iris Classifier. 
It further demonstrates how to deploy the app via 1) your local machine (Flask Only), 
2) using docker on your local machine (Flask + Docker), and 3) docker on heroku (Flask + Docker + Heroku). 

###Flask Only
1. On the terminal (inside the project folder), launch the app by running `python app.py`. 
You may be required to install necessary python packages for this.
2. You can open the app locally by going to the url output from the terminal e.g. `http://192.168.1.10:5000/` or 
by going to the hardcoded url in the app.py code i.e. `http://0.0.0.0:5000/`.

###Flask + Docker - if the image does not exists
1. Launch the docker desktop.
2. On the terminal (one branch above the project folder), build the docker image by running `docker build <project_folder> -t '<docker_image_name>:<docker_version_name>'`
3. Launch the app by running `docker run -p 5000:5000 -d <docker_image_name>`
4. You can open the app locally by going to the hardcoded url in the app.py code i.e. `http://0.0.0.0:5000/`.

###Flask + Docker - if the image exists
1. Launch the docker desktop.
2. On the terminal (inside the project folder), load the docker image (tar file) by running `docker load -i <docker_image_file_name>`
3. Launch the app by running `docker run -p 5000:5000 -d <docker_image_name>`
4. You can open the app locally by going to the harcoded url in the app.py code: `http://0.0.0.0:5000/`.

###Flask + Docker + Heroku
1. Once you have created a docker image, login to your heroku account via the terminal by 
running `heroku container:login`.This would open a browser and prompt you to log in with your Heroku credentials.
2. On the terminal(inside the project folder), create an app in heroku that will house your container 
`heroku create <heroku_app_name>`. You will receive a link where your app will be launched e.g. 
`https://<heroku_app_name>.herokuapp.com/`.
3. Push your docker container into heroku by running `heroku container:push web --app <heroku_app_name>`.
4. Deploy your docker container in heroku by running `heroku container:release web --app <heroku_app_name>`.
5. You can open your app anywhere by going to the url `https://<heroku_app_name>.herokuapp.com/`.