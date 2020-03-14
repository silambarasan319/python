#!/bin/bash
yum install java-1.8.0-openjdk-devel -y

#alternatives --config java

touch /etc/profile.d/java.sh
#!/bin/bash
export JAVA_HOME=$(dirname $(dirname $(readlink $(readlink $(which javac)))))
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar

source /etc/profile.d/java.sh
