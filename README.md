# Docker-MPI
Flights data Analysis using MPI.

### Setting up the environment

`docker pull husseinabdallah2/mpi4py-cluster:master`

`docker images`

Explanation: The above commands are used to pull the existing image
“husseinabdallah2/mpi4py-cluster:master” from docker hub.

Then we are listing the existing images in the docker library.

`docker run --mount type=bind,source=D:\DOCKERA3T2,target=/A3files --name masternode -it facd914d2eb6 /bin/bash`

`exit`

`docker run --mount type=bind,source=D:\DOCKERA3T2,target=/A3files --name workernode1 -it facd914d2eb6 /bin/bash`

`exit`

`docker run --mount type=bind,source=D:\DOCKERA3T2,target=/A3files --name workernode2 -it facd914d2eb6 /bin/bash`

`exit`

`docker run --mount type=bind,source=D:\DOCKERA3T2,target=/A3files --name workernode3 -it facd914d2eb6 /bin/bash`

`exit`

Explanation: The above commands are used to create containers from the pulled image “facd914d2eb6” and map the location from local with the location in the docker container(ubuntu)

`docker ps -a`

Explanation: command to list the available images in the image repository

`docker start 70b3968e54ee6920f59c34097409581eecd336ae6321a341bcbbb085ff38b5bb 32beb28f308c0e94db4eaf5a655e094d55e337f744149e8f1d79aca28aac 0552972d18ab287e87aced3b4e742dc24c38634d088fee18fc5fb608c99c1f f1b11ac2bcb411a89ed9ee8b5f432682a32d97f0fdbd7ff108df0ab152abcb`

Explanation: Start command is used to activiate the containers which we just created.

`docker exec -it 70b3968e54ee6920f59c34097409581eecd336ae6321a341bcbbb085ff38b5bb /bin/bash`

Explanation: Command to enter inside the docker container. “ls -lrt is used to list the available directories. (MASTER NODE)

`apt-get update`

Explanation: Explanation: apt-get update retrieves package lists from the repositories and "updates" them with information on the most recent versions of packages and their dependencies.

`apt-get install nano net-tools iputils-ping openssh-client openssh-server`

Explanation: command to install network tools.

`pip install pandas==1.5.`

Explanation : Command to install pandas package in ubuntu

nano ~/machinefile

Explanation: Command to set the IP addresses(hosts).

passwd

Explanation: Command to set the password to the container.

service ssh start

Explanation : command to start and check the ssh service.

docker exec -it 32beb28f308c0e94db4eaf5a655e094d55e337f744149e8f1d79aca28aac9 /bin/bash

Explanation: Command to enter inside the container.

apt-get update

Explanation: apt-get update retrieves package lists from the repositories and "updates" them with information on the most recent versions of packages

and their dependencies.

apt-get install nano net-tools iputils-ping openssh-client openssh-server

Explanation: command to install network tools.

pip install pandas==1.5.

Explanation: Command to install the pandas package.

nano ~/machinefile

Explanation: Command to set the IP addresses(hosts).

Passwd

Explanation: Command to set the password to the container.

service ssh start

Explanation: command to start and check the ssh service.

Till now we have configured the containers master and worker1.

Repeat the above steps for the other 2 containers as well. (worker2 and worker3)

nano /etc/ssh/sshd_config

Explanation: command to exit the ssh config file.

Check for “PermitRootLogin yes“

ssh root@172.17.0.

Explanation: command to check the connectivity between the master

container and worker1 container

ssh root@172.17.0.

Explanation: command to check the connectivity between the master container and worker2 container

ssh root@172.17.0.

Explanation: command to check the connectivity between the master

container and worker3 container

ssh-keygen -t rsa

Explanation: command to create a ssh key in the master node.

ls -lrt

Explanation: command to list the files and directories in the master container
and check if the ssh key is generated.

ssh-copy-id -i sshkeyfile.pub root@172.17.0.

Explanation: command to copy the generated ssh key to worker1.

ssh-copy-id -i sshkeyfile.pub root@172.17.0.

Explanation: command to copy the generated ssh key to worker2.

ssh-copy-id -i sshkeyfile.pub root@172.17.0.

Explanation: command to copy the generated ssh key to worker3.

ssh-copy-id -i root@172.17.0.

Explanation: command to copy the ssh key and enable the passwordless ssh from master to worker1.

ssh-copy-id -i root@172.17.0.

Explanation: command to copy the ssh key and enable the passwordless ssh from master to worker2.

ssh-copy-id -i root@172.17.0.

Explanation: command to copy the ssh key and enable the passwordless ssh from master to worker3.

docker network inspect bridge

Explanation: Command to display the network configurations and ip addresses.

Below are the scripts to demonstrate the working of MPI using docker containers.

mpiexec -n 4 -machinefile ~/machinefile python -m
mpi4py usecase1_mostcancelledflights.py

mpiexec -n 4 -machinefile ~/machinefile python -m
mpi4py usecase2_mostdivertedflights.py

mpiexec -n 4 -machinefile ~/machinefile python -m
mpi4py usecase3_avgtimebetweenNA&CHG.py

mpiexec -n 4 -machinefile ~/machinefile python -m
mpi4py usecase4_datesmising.py
