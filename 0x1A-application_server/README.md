# 0x1A. Application server

# Background Context
A web infrastructure is already serving web pages via `Nginx` or `Apache`. While a web server can also serve dynamic content, this task is usually given to an application server. In this project it will add this piece to the infrastructure, plug it to `Nginx` and make is serve your Airbnb clone project.

## Resources
* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash](https://werkzeug.palletsprojects.com/en/0.14.x/routing/) in route - `strict_slashes`

 ## 0. Set up development with Python
 Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

* Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
* Git clone your AirBnB_clone_v2 on your web-01 server.
* Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
* Your Flask application object must be named app.

Example:

Window 1:

    ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
    * Serving Flask app "0-hello_route" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -

Window 2:
    ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
    Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

## 1. Set up production with Gunicorn
Now that you have your development environment set up, let’s get your production application server set up with `Gunicorn` on `web-01`, port `5000`. You’ll need to install `Gunicorn` and any libraries required by your application. Your `Flask` application object will serve as a `WSGI` entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.

Requirements:

* Install `Gunicorn` and any other libraries required by your application.
* The Flask application object should be called app. (This will allow us to run and check your code)
* You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.
* In order to check your code, the checker will bind a Gunicorn instance to port 6000, so make sure nothing is listening on that port.
Example:

Terminal 1:

    ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
    [2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
    [2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
    [2019-05-03 20:47:20 +0000] [3595] [INFO] Using worker: sync
    [2019-05-03 20:47:20 +0000] [3598] [INFO] Booting worker with pid: 3598

Terminal 2:

    ubuntu@229-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
    Hello HBNB!ubuntu@229-web-01:~$

## 2. Serve a page with Nginx

## 3. Add a route with query parameters 

## 4. Let's do this for your API

## 5. Serve your AirBnB clone