# Docker-MPI
Flights data Analysis using MPI.

### Setting up the environment

`docker pull husseinabdallah2/mpi4py-cluster:master`

![Picture1](https://user-images.githubusercontent.com/41756221/211596862-ded8381a-2971-4dbb-a6f2-c1c6fe0ac43d.png)

`docker images`

![Picture2](https://user-images.githubusercontent.com/41756221/211597029-3d0a63f3-27ae-4c09-a3ee-2cfc2b820756.png)

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

![Picture3](https://user-images.githubusercontent.com/41756221/211597166-67af0f7d-c45b-4d57-91b7-4de2a13c3d76.png)

Explanation: command to list the available images in the image repository

`docker start 70b3968e54ee6920f59c34097409581eecd336ae6321a341bcbbb085ff38b5bb 32beb28f308c0e94db4eaf5a655e094d55e337f744149e8f1d79aca28aac 0552972d18ab287e87aced3b4e742dc24c38634d088fee18fc5fb608c99c1f f1b11ac2bcb411a89ed9ee8b5f432682a32d97f0fdbd7ff108df0ab152abcb`

![Picture4](https://user-images.githubusercontent.com/41756221/211597251-3b8cb490-a9ce-46ea-8f96-10fb26cbcbfd.png)

Explanation: Start command is used to activiate the containers which we just created.

`docker exec -it 70b3968e54ee6920f59c34097409581eecd336ae6321a341bcbbb085ff38b5bb /bin/bash`

![Picture5](https://user-images.githubusercontent.com/41756221/211597359-e39b998d-ba6a-4e18-89cb-5ccd6ae82b89.jpg)

Explanation: Command to enter inside the docker container. “ls -lrt is used to list the available directories. (MASTER NODE)

`apt-get update`

![Picture6](https://user-images.githubusercontent.com/41756221/211597423-c95310cf-6a0b-4d77-87ef-01b1e0b3e197.png)

Explanation: Explanation: apt-get update retrieves package lists from the repositories and "updates" them with information on the most recent versions of packages and their dependencies.

`apt-get install nano net-tools iputils-ping openssh-client openssh-server`

![Picture7](https://user-images.githubusercontent.com/41756221/211597481-5c6fda52-a5aa-47d0-9137-262a27b36678.png)

Explanation: command to install network tools.

`pip install pandas==1.5.`

![Picture8](https://user-images.githubusercontent.com/41756221/211597789-470b3b2a-b9cd-4c0f-87ce-bd89d4d9e9c6.png)

Explanation : Command to install pandas package in ubuntu

`nano ~/machinefile`

![Picture9](https://user-images.githubusercontent.com/41756221/211597878-53585012-794a-437c-8af2-f7989042e110.png)

Explanation: Command to set the IP addresses(hosts).

`passwd`

![Picture10](https://user-images.githubusercontent.com/41756221/211597956-843b5306-12ba-46b7-95c5-516b56e7499b.png)

Explanation: Command to set the password to the container.

`service ssh start`

![Picture11](https://user-images.githubusercontent.com/41756221/211598128-a1da2d14-5a83-47fb-821b-f8c0f79dd3fc.jpg)

Explanation : command to start and check the ssh service.

`docker exec -it 32beb28f308c0e94db4eaf5a655e094d55e337f744149e8f1d79aca28aac9 /bin/bash`

![Picture12](https://user-images.githubusercontent.com/41756221/211598201-98355a77-3485-409b-abb3-d80c2f0c05ef.jpg)

Explanation: Command to enter inside the container.

`apt-get update`

![Picture13](https://user-images.githubusercontent.com/41756221/211598232-5e1f150e-6788-4319-bf77-165fb3be6d3e.png)

Explanation: apt-get update retrieves package lists from the repositories and "updates" them with information on the most recent versions of packages
and their dependencies.

`apt-get install nano net-tools iputils-ping openssh-client openssh-server`

![Picture14](https://user-images.githubusercontent.com/41756221/211598271-3f355ab6-c637-4e32-b76a-4bb078db387d.png)

Explanation: command to install network tools.

`pip install pandas==1.5.`

![Picture15](https://user-images.githubusercontent.com/41756221/211598303-a0143666-9744-45fe-8353-2069d89b934c.jpg)

Explanation: Command to install the pandas package.

`nano ~/machinefile`

![Picture16](https://user-images.githubusercontent.com/41756221/211598327-e3e6d2d5-2d63-48e4-bcb0-c7b666ac8580.png)

Explanation: Command to set the IP addresses(hosts).

`Passwd`

![Picture17](https://user-images.githubusercontent.com/41756221/211598355-b5919523-855a-47df-bd88-08e1c5d0ef24.png)

Explanation: Command to set the password to the container.

`service ssh start`

![Picture18](https://user-images.githubusercontent.com/41756221/211598387-d82395fd-91b8-48a0-b311-eaa280c66648.jpg)

Explanation: command to start and check the ssh service.
Till now we have configured the containers master and worker1.
Repeat the above steps for the other 2 containers as well. (worker2 and worker3)

`nano /etc/ssh/sshd_config`

![Picture20](https://user-images.githubusercontent.com/41756221/211598665-dd9ed0c4-d353-4203-9e91-3301355ded87.jpg)

Explanation: command to exit the ssh config file.

Check for “PermitRootLogin yes“

`ssh root@172.17.0.7`

![Picture21](https://user-images.githubusercontent.com/41756221/211598855-556372d6-d26c-48ca-b898-5a44fb19197e.png)

Explanation: command to check the connectivity between the master

container and worker1 container

`ssh root@172.17.0.8`

![Picture22](https://user-images.githubusercontent.com/41756221/211598917-164c3306-d6a6-42da-b063-4e2ab7a96830.png)

Explanation: command to check the connectivity between the master container and worker2 container

`ssh root@172.17.0.9`

![Picture23](https://user-images.githubusercontent.com/41756221/211599006-d8c4e17e-099c-4fa3-bcb5-2831b57f6dcc.png)

Explanation: command to check the connectivity between the master

container and worker3 container

`ssh-keygen -t rsa`

![Picture24](https://user-images.githubusercontent.com/41756221/211599038-d79af957-de92-4c2f-9c6d-512a8b975b1d.png)

Explanation: command to create a ssh key in the master node.

`ls -lrt`

![Picture25](https://user-images.githubusercontent.com/41756221/211599065-36587ee5-58c4-48f7-80ab-3be18516b8b9.png)

Explanation: command to list the files and directories in the master container
and check if the ssh key is generated.

`ssh-copy-id -i sshkeyfile.pub root@172.17.0.7`

![Picture26](https://user-images.githubusercontent.com/41756221/211599187-9d01d068-aaaa-474c-84b8-447b4b8606d4.png)

Explanation: command to copy the generated ssh key to worker1.

`ssh-copy-id -i sshkeyfile.pub root@172.17.0.8`

![Picture27](https://user-images.githubusercontent.com/41756221/211599218-6c0828d6-5bdd-4e5b-b6c1-229a47f47ac3.jpg)

Explanation: command to copy the generated ssh key to worker2.

`ssh-copy-id -i sshkeyfile.pub root@172.17.0.9`

![Picture28](https://user-images.githubusercontent.com/41756221/211599248-58f0b89e-ab28-4823-9385-9525ca68ed81.jpg)

Explanation: command to copy the generated ssh key to worker3.

`ssh-copy-id -i root@172.17.0.7`

![Picture29](https://user-images.githubusercontent.com/41756221/211599319-110059b3-5fbe-4f61-94b8-a26a4faa7c47.jpg)

Explanation: command to copy the ssh key and enable the passwordless ssh from master to worker1.

`ssh-copy-id -i root@172.17.0.8`

![Picture30](https://user-images.githubusercontent.com/41756221/211599344-9928e17f-2aaf-4dfe-87c6-ccebf2847357.jpg)

Explanation: command to copy the ssh key and enable the passwordless ssh from master to worker2.

`ssh-copy-id -i root@172.17.0.9`

![Picture31](https://user-images.githubusercontent.com/41756221/211599393-e5aa652b-ec87-4b8b-8f33-745357a24030.jpg)

Explanation: command to copy the ssh key and enable the passwordless ssh from master to worker3.

`docker network inspect bridge`

![Picture32](https://user-images.githubusercontent.com/41756221/211599434-6843ea37-d565-43ca-a958-3ea9fa4fc559.png)

Explanation: Command to display the network configurations and ip addresses.

Below are the scripts to demonstrate the working of MPI using docker containers.

`mpiexec -n 4 -machinefile ~/machinefile python -m mpi4py usecase1_mostcancelledflights.py`

`mpiexec -n 4 -machinefile ~/machinefile python -m mpi4py usecase2_mostdivertedflights.py`

`mpiexec -n 4 -machinefile ~/machinefile python -m mpi4py usecase3_avgtimebetweenNA&CHG.py`

`mpiexec -n 4 -machinefile ~/machinefile python -m mpi4py usecase4_datesmising.py`

![Picture33](https://user-images.githubusercontent.com/41756221/211599583-f47de0b6-153b-48aa-a9d6-0aeee655879d.png)
