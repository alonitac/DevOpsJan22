# Nexus Repository Manager

## Install

We will deploy the Nexus server via [pre-built Docker image](https://hub.docker.com/r/sonatype/nexus3/).

> You can deploy the Nexus server on the same VM of Jenkins.

```shell
sudo mkdir /nexus-data && sudo chmod 777 /nexus-data
docker run -d -p 8081:8081 --name nexus -v /nexus-data:/nexus-data -e INSTALL4J_ADD_VM_PARAMS="-Xms400m -Xmx400m -XX:MaxDirectMemorySize=400m" sonatype/nexus3
```

## Repository Management

Nexus ships with a great [Official docs](https://help.sonatype.com/repomanager3/nexus-repository-administration/repository-management) and compatible with [many package managers](https://help.sonatype.com/repomanager3/nexus-repository-administration/formats): Java/Maven, npm, NuGet, PyPI, Docker, Helm, Yum, and APT.

### Repository Types

#### Proxy repo

Proxy repository is a repository that is linked to a remote repository. Any request for a component is verified against the local content of the proxy repository. If no local component is found, the request is forwarded to the remote repository.

#### Hosted repo

Hosted repository is a repository that stores components in the repository manager as the authoritative location for these components.

#### Group repo

Repository group allow you to combine multiple repositories and other repository groups in a single repository.
This in turn means that your users can rely on a single URL for their configuration needs, while the administrators can add more repositories and therefore components to the repository group.


## Create PyPi proxy repo

1. After signing in to your Nexus server as an administrator, click on the **Server configuration** (<i class="fa fa-gear"></i>) icon.
2. Create a [PyPi repo](https://help.sonatype.com/repomanager3/nexus-repository-administration/formats/pypi-repositories).
3. [Configure](https://help.sonatype.com/repomanager3/nexus-repository-administration/formats/pypi-repositories#PyPIRepositories-Download,searchandinstallpackagesusingpip) `pip` to download packages from your private artifact repository. To do so, create a file `pip.conf` with the following content:
```text
[global]
trusted-host = <nexus-host>
index-url = http://<nexus-host>:8081/repository/app-dependencies/simple
index = http://<nexus-host>:8081/repository/app-dependencies
```

While changing `<nexus-host>` to the DNS/IP of your server. 

5. Put the `pip.conf` file either in your virtual env filder (`venv`) or define a custom location by setting the following env var: `PIP_CONFIG_FILE=<path-to-pip-conf>`. There are [other methods](https://pip.pypa.io/en/stable/topics/configuration/#location).

## Repository Health Check

https://help.sonatype.com/repomanager3/nexus-repository-administration/repository-management/repository-health-check

## Define s3 as an artifacts storage

https://help.sonatype.com/repomanager3/nexus-repository-administration/repository-management/configuring-blob-stores#ConfiguringBlobStores-AWSSimpleStorageService(S3)


