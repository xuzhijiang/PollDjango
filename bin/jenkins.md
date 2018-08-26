## Installation

install jdk1.8 or jdk1.7,because jenkins does not work with jdk1.9.

从Jenkins官方网站`https://jenkins.io/`下载最新的`war`包:

`java -jar jenkins.war` and copy the password output by the console.

open `http://localhost:8080/` and enter the password you copied.

perform a default installation, jenkins will install plugins like Maven, git automatically, Finally, create an admin user and complete the installation.

![refer to](https://jenkins.io/doc/tutorials/build-a-python-app-with-pyinstaller/#fork-sample-repository)