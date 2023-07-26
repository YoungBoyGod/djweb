```shell
sudo adduser gerrit
sudo su gerrit

sudo -s
vi /etc/sudoers
gerrit   ALL=(ALL) NOPASSWD: ALL


```



```shell
默认gerrit 配置
[gerrit]
        basePath = git
        canonicalWebUrl = http://web:8080/
        serverId = fc73c53e-4089-402e-a648-ef895db281f1
[container]
        javaOptions = "-Dflogger.backend_factory=com.google.common.flogger.backend.log4j.Log4jBackendFactory#getInstance"
        javaOptions = "-Dflogger.logging_context=com.google.gerrit.server.logging.LoggingContext#getInstance"
        user = root
        javaHome = /usr/lib/jvm/java-11-openjdk-amd64
[index]
        type = lucene
[auth]
        type = OPENID
        userNameCaseInsensitive = true
[receive]
        enableSignedPush = false
[sendemail]
        smtpServer = localhost
[sshd]
        listenAddress = *:29418
[httpd]
        listenUrl = http://*:8080/
[cache]
        directory = cache

```
修改后配置文件
```shell
[gerrit]
	basePath = git
	canonicalWebUrl = http://10.2.24.136:8091/
	serverId = fc73c53e-4089-402e-a648-ef895db281f1
[container]
	javaOptions = "-Dflogger.backend_factory=com.google.common.flogger.backend.log4j.Log4jBackendFactory#getInstance"
	javaOptions = "-Dflogger.logging_context=com.google.gerrit.server.logging.LoggingContext#getInstance"
	user = root
	javaHome = /usr/lib/jvm/java-11-openjdk-amd64
[index]
	type = lucene
[auth]
	type = HTTP
[receive]
	enableSignedPush = false
[sendemail]
	smtpServer = localhost
[sshd]
	listenAddress = *:29418
[httpd]
	listenUrl = proxy-http://*:8091/
[cache]
	directory = cache



```

```shell
#apache2 httpd.conf
root@web:/etc/apache2# more httpd.conf
<VirtualHost *:8090>
    ServerName 10.2.24.136:8090
    ProxyRequests Off
    ProxyVia Off
    ProxyPreserveHost On
    <Proxy *>
          Order deny,allow
          Allow from all
    </Proxy>
    <Location /login/>
        AuthType Basic
        AuthName "Gerrit Code Review"
        Require valid-user
        AuthBasicProvider file
        AuthUserFile /home/gerrit/gerrit_dir/etc/passwords
    </Location>
    AllowEncodedSlashes On
    ProxyPass / http://10.2.24.136:8091/
</VirtualHost>



#apache2.conf
#add at the end
Include httpd.conf

```

```shell
#apache2 ports.conf
root@web:/etc/apache2# more ports.conf
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

Listen 80
Listen 8090
<IfModule ssl_module>
	Listen 443
</IfModule>

<IfModule mod_gnutls.c>
	Listen 443
</IfModule>
# vim: syntax=apache ts=4 sw=4 sts=4 sr noet


```
<img src="D:\1.png"/>