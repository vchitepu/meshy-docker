FROM python:3.10.9-slim

RUN --mount=type=cache,target=/var/cache/apt \
  apt-get update && \
  # we need those
  apt-get install -y fonts-dejavu-core rsync git jq moreutils aria2 \
  # extensions needs those
  ffmpeg libglfw3-dev libgles2-mesa-dev pkg-config wget libcairo2 libcairo2-dev build-essential xvfb libsm6 libxext6 libxrender-dev mesa-utils-extra libfontconfig1-dev libegl1-mesa-dev

RUN Xvfb :0 -screen 0 1024x768x24 -ac +extension GLX +render -noreset &

WORKDIR /meshy

ADD . /meshy

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8889
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8889"]

