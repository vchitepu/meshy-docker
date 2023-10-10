# Meshy
Forked from https://github.com/thygate/stable-diffusion-webui-depthmap-script

A standalone docker implementation of stable diffusions depth extension.

#### Requirements
1. Docker running and installed
2. Nvidia GPU

#### Installation
1. Clone this repository
2. Enter directory and run with docker compose
```
$ cd meshy-docker

# For initial installation or for testing updates to code
$ docker compose --profile meshy up --build

# To stop/start
$ docker compose --profile meshy [up|stop]

# To run in detatched mode
# docker compose --profile up -d
```
NOTE: Currently uses a FastAPI to make calls easier but this is still in development
