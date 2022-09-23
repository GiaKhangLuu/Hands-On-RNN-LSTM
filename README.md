# 🚀 Running

Install all packages

> pip3 install -r requirements.txt

Start activity recognition

> python3 inference_lstm.py

# 🐳 Running from Docker 

In LinuxOS, we can let the docker container accesses webcam by command:

`docker run --device=/dev/video0:/dev/video0 <image-name>`

But MacOS do not have path `/dev/video0`. So the process to let docker access camera in MacOS is quite tricky.

Following the next steps everytime when we want to connect a webcam to a docker container.

Assume that `socat, xquartz, docker-machine, VirtualBox and VirtualBox Extension` have been installed:

1. `open -a XQuartz`
2. From the XQuartz terminal, enter `socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"`

If we have an error, find the PID (process ID): `lsof -i tcp:6000`

Then kill it: `kill -9 <process-id>`

3. `IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')`
4. `xhost + $IP`
5. `DOCKER_MACHINE=<docker-machine-name>`
6. `docker-machine start ${DOCKER_MACHINE}`
7. `eval $(docker-machine env ${DOCKER_MACHINE})`
8. `vboxmanage list webcams`
9. `vboxmanage controlvm "${DOCKER_MACHINE}" webcam attach .1`

If some errors occur during these above steps, the solutions can be found in the `issue` tab 

Before testing with webcam, check the XQuartz is running well likes below:

`docker run --rm -it -e DISPLAY=$IP:0 gns3/xeyes`

When everything works, we can now run this repo:

`docker run --rm -it --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$IP:0 giakhang/my-first-image:myfirstimagepush`

# References
[https://www.youtube.com/watch?v=bxrc1otsKIM](url)

[https://www.youtube.com/watch?v=B5wf8p1oezA](url)

[https://www.youtube.com/watch?v=TOCxu0jh8ic&t=1660s](url)

[https://medium.com/@jijupax/connect-the-webcam-to-docker-on-mac-or-windows-51d894c44468](url)
