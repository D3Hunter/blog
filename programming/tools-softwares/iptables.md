`iptables/netfilter` is the userspace/kernel module
`lsmod | grep ip_tables`

tables->table->chains->rule->target(action)
`rule`从上到下匹配，第一个匹配后停止，无匹配使用默认

rpm -q iptables

iptables -nL --line-numbers
iptables -D chain rulenum 删除chain中的rule或某个reference
iptables -X chain 仅当无reference
iptables -F [chain] 删除所有rule，不加chain则flush所有chain
iptables -N LOGGING
iptables -A INPUT -j LOGGING
iptables -A OUTPUT -j LOGGING
iptables -A LOGGING -j LOG -m limit --limit 2/min --log-prefix "Dropped: " --log-level 4

允许访问`mysql`，使用`insert`放在`reject`前
iptables -I RH-Firewall-1-INPUT 9 -p tcp -m tcp --dport 3306 -j ACCEPT

配置iptables和selinux：`system-config-securitylevel`
保存iptables：`service iptables save`

/etc/syslog.conf  kern.warning /var/log/custom.log
/etc/sysconfig/iptables
