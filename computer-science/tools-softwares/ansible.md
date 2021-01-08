## Ansible
Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy. Avoid writing scripts or custom code to deploy and update your applications — automate in a language that approaches plain English, using SSH, with no agents to install on remote systems.

### Concepts
- `Control Node`: Any machine with Ansible installed.
- `Managed nodes`: The network devices (and/or servers) you manage with Ansible. Managed nodes are also sometimes called “hosts”.
- `inventory`: A list of managed nodes.
- `Modules`: The units of code Ansible executes.
- `Tasks`: The units of action in Ansible.
- `Playbooks`: Ordered lists of tasks, saved so you can run those tasks in that order repeatedly.
- ad-hoc commands: a quick one-liner without writing a playbook.
    - An ad-hoc command looks like this: `ansible [pattern] -m [module] -a "[module options]"`

### Usage
A basic Ansible command or playbook:
1. selects machines to execute against from inventory
2. connects to those machines (or network devices, or other managed nodes), usually over SSH
3. copies one or more modules to the remote machines and starts execution there

### Inventory
The default location for inventory is a file called `/etc/ansible/hosts`. You can specify a different inventory file at the command line using the `-i <path>` option.

The inventory file can be in one of many formats, depending on the `inventory plugins` you have. The most common formats are `INI` and `YAML`.

There are two default groups: `all` and `ungrouped`. The `all` group contains every host. The `ungrouped` group contains all hosts that don’t have another group aside from `all`

### Configuring Ansible
Ansible supports several sources for configuring its behavior, including an ini file named ansible.cfg, environment variables, command-line options, playbook keywords, and variables.

The ansible-config utility allows users to see all the configuration settings available, their defaults, how to set them and where their current value comes from.

create an `ini` file named `ansible.cfg` in `/etc/ansible` to override default settings.

Changes can be made and used in a configuration file which will be searched for in the following order:
- ANSIBLE_CONFIG (environment variable if set)
- ansible.cfg (in the current directory)
    - Ansible will not automatically load a config file from the current working directory if the directory is world-writable.
- ~/.ansible.cfg (in the home directory)
- /etc/ansible/ansible.cfg

## AWX/Tower
`AWX` provides a web-based user interface, REST API, and task engine built on top of `Ansible`. It is the upstream project for `Tower`, a commercial derivative of `AWX`.

- Role-based access control
- push-button deployment
- Centralized logging and auditing
- REST API

