# Ollama LLM Agent Test Project

This project uses Ollama to connect to a local Llama3:instruct Large 
Language Model (LLM) instance and perform some work.

**Prerequisites**

* A local Llama3:instruct LLM instance running on your machine
* Docker installed and running on your machine

**Project Structure**

The project consists of the following files:

* `requirements.txt`: a file containing Python dependencies required by the 
project
* `Dockerfile`: a file defining how to build a Docker image for the project
* `docker_manager.sh`: a shell script that provides common Docker run tasks 
(run, build, interact)
* `app.py`: the main Python script that uses Ollama to connect to the LLM 
instance and perform work

**Usage**

To use the project, follow these steps:

1. Run `docker_manager.sh run` to start a new container based on the Docker 
image
2. If the project has never been built before, you will need to run 
`docker_manager.sh build` first
3. Interact with the LLM instance using `docker_manager.sh interact`
4. By default, the container shares the host network; if you want to change 
this behavior, modify the Dockerfile and rebuild

**Notes**

* The project defaults to connecting to the default port (localhost) on 
Ollama
* Changes to `requirements.txt` or `Dockerfile` require rebuilding the 
project with `docker_manager.sh build`
* Run and interact versions of the container will not start if the project 
has never been built before; run `docker_manager.sh build` first

**Troubleshooting**

If you encounter issues running the project, please refer to the following:

* Check that your LLM instance is running on localhost:port
* Verify that the Docker image has been built successfully (run 
`docker_manager.sh build`)
* Check that the container is running with the correct network settings (run
`docker_manager.sh interact` and check the container's network 
configuration)

I hope this helps! Let me know if you have any questions.