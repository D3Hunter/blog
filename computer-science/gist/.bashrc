export JAVA_HOME=/usr/lib/jvm/default-java
export JRE_HOME=${JAVA_HOME}/jre
export CATALINA_HOME=/usr/share/tomcat7
export CATALINA_BASE=/var/lib/tomcat7
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib:${CATALINA_HOME}/lib/servlet-api.jar
export PATH=${JAVA_HOME}/bin:/usr/local/nginx/sbin:$PATH

alias ll='ls -lrt'
alias l='ls -l'
alias emacs='emacs -nw'
alias grep='grep --exclude-dir=\.?* --exclude=\.?*'
alias docker-killall='docker ps -a | tail -n +2 | cut -f1 -d' ' | xargs docker rm'
TERM=xterm-256color
#force_color_prompt=yes
