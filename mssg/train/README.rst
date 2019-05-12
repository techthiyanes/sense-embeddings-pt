***************************************Java

sudo mkdir -p /usr/local/java

sudo cp -r jdk-7u80-linux-x64.tar.gz /usr/local/java/

cd /usr/local/java

sudo tar xvzf jdk-7u80-linux-x64.tar.gz

sudo nano /etc/profile

JAVA_HOME=/usr/local/java/jdk1.7.0_80
JRE_HOME=/usr/local/java/jdk1.7.0_80
PATH=$PATH:$JRE_HOME/bin:$JAVA_HOME/bin
export JAVA_HOME
export JRE_HOME
export PATH

sudo update-alternatives --install "/usr/bin/java" "java" "/usr/local/java/jdk1.7.0_80/bin/java" 1

sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/local/java/jdk1.7.0_80/bin/javac" 1

sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/local/java/jdk1.7.0_80/bin/javaws" 1

sudo update-alternatives --set java /usr/local/java/jdk1.7.0_80/bin/java

sudo update-alternatives --set javac /usr/local/java/jdk1.7.0_80/bin/javac

sudo update-alternatives --set javaws /usr/local/java/jdk1.7.0_80/bin/javaws

source /etc/profile

java -version

**************************Apache Maven

wget https://www-us.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz -P /tmp

sudo tar xf /tmp/apache-maven-*.tar.gz -C /opt

sudo ln -s /opt/apache-maven-3.3.9 /opt/maven

sudo nano /etc/profile.d/maven.sh

Paste:

export JAVA_HOME=/usr/local/java/jdk1.7.0_80
export M2_HOME=/opt/maven
export MAVEN_HOME=/opt/maven
export PATH=${M2_HOME}/bin:${PATH}

sudo chmod +x /etc/profile.d/maven.sh

source /etc/profile.d/maven.sh

mvn -version

mvn -X clean install

*******************************Scala

sudo wget http://scala-lang.org/files/archive/scala-2.11.6.deb
sudo dpkg -i scala-2.11.6.deb
sudo apt-get update
sudo apt-get install scala
scala -version

