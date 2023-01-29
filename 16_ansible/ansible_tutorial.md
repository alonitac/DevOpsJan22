# Ansible

# Build simple inventory and use ad-hoc commands

Ansible works against multiple managed nodes or “hosts” in your infrastructure at the same time, using a list or group of lists known as **inventory**.
The default location for inventory is a file called `/etc/ansible/hosts` (use `-i` to specify another location).

1. For this demo, create **two** Amazon Linux EC2 instances in our shared AWS account. Make sure you have access to the `.pem` private key.
2. Build a simple `hosts` inventory file as follows:
```ini
<host-ip1>
<host-ip2>
```

An Ansible ad hoc command uses the `ansible` command-line tool to automate a single task, in not-reusable manner. We will use the `ping` module to ping our hosts.

3. Run the following command, investigate the returned error and use the `--user` option to fix it.
```shell
ansible -i /path/to/inventory-file --private-key /path/to/private-key-pem-file all -m ping
```

4. Let's say the hosts run webserver, we can arrange hosts under groups, and automate tasks for specific group:
```ini
[webserver]
web1 ansible_host=<host-ip-1> ansible_user=<host-ssh-user>
web2 ansible_host=<host-ip-2> ansible_user=<host-ssh-user>
```

There are two more default groups: `all` and `ungrouped`. The all group contains every host. The ungrouped group contains all hosts that don’t have another group aside from `all`.

5. Let's check the uptime of all server in `webserver` group:
```shell
ansible -i /path/to/inventory-file --private-key /path/to/private-key-pem-file webserver -m command -a "uptime"
```

## Working with Playbooks

If you need to execute a task with Ansible more than once, write a **playbook** and put it under source control.
Ansible Playbooks offer a repeatable, re-usable and simple configuration management.
Playbooks are expressed in YAML format, composed of one or more ‘plays’ in an **ordered** list. 
A playbook 'play' runs one or more tasks. Each task calls an Ansible module from top to bottom.

In this demo, we will be practicing some security hardening for the webserver hosts.

To demonstrate the power of Ansible, we first want to create a task that verify the installation of `httpd` (and install it if needed)

1. Create the following `site.yaml` file, representing an Ansible playbook:
```yaml
---
- name: Harden web servers
  hosts: <hosts-group>
  tasks:
    - name: Ensure httpd is at the latest version
      ansible.builtin.yum:
        name: httpd-2.4*
        state: latest
```
In this playbook we execute one task using the built-in [`yum` module](https://docs.ansible.com/ansible/2.9/modules/yum_module.html#yum-module). Ansible ships with hundreds of [built-in modules](https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html) available for usage.

2. Apply your playbook using the following `ansible-playbook` command.
```shell
ansible-playbook -i /path/to/inventory-file --private-key /path/to/private-key-pem-file site.yaml
```

As the tasks in this playbook require root-privileges, we add the `become: true` to enable execute tasks as a different Linux user:
```yaml
---
- name: Harden web servers
  hosts: webserver
  become: yes
  become_method: sudo
  tasks:
    - name: Ensure httpd is at the latest version
      become_user: root
      ansible.builtin.yum:
        name: httpd-2.4*
        state: latest
```
Run the playbook again and make sure the task has been completed successfully.

We now want to harden the SSH configurations of the hosts. 

3. Add the following task to your notebook
```yaml
    - name: Write the sshd config file
      ansible.builtin.template:
        src: templates/sshd_config.j2
        dest: /etc/ssh/sshd_config
```

As well as the following var file import statement in the top-level area of the playbook:

```yaml
  vars_files:
    - vars/amazon-linux.yaml
```

Ansible uses [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) templating to enable dynamic expressions and access to [variables](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#playbooks-variables).
The `templates/sshd_config.j2` and its corresponding variable file `vars/amazon-linux.yaml` can be found in our shared repo.

5. Run the playbook. Connect to one of the hosts and make sure the `sshd` configuration file has been updated.
6. It's required to restart the `sshd` service after changing the configuration, let's add a `handlers:` entry with a handler that restarts the daemon after a successful configuration change:
```yaml
---
- name: Harden web servers
  hosts: webserver
  become: yes
  become_method: sudo
  vars_files:
    - vars/amazon-linux.yaml

  tasks:
    - name: Ensure httpd is at the latest version
      ansible.builtin.yum:
        name: httpd-2.4*
        state: latest

    - name: Write the sshd config file
      ansible.builtin.template:
        src: templates/sshd_config.j2
        dest: /etc/ssh/sshd_config
      notify: restart sshd

  handlers:
    - name: restart sshd
      become_user: root
      ansible.builtin.service:
        name: sshd
        state: restarted

```
Note the added `notify:` entry in the **Write the sshd config file** task.

7. Run the playbook and check the status of the `sshd` service by running `sudo service sshd status` in one of the hosts machine.
8. Now change the `sshd_port:` in `vars/amazon-linux.yaml` to a number other than `22` and run the playbook.
9. You will need update your `hosts` inventory file to use the new port, as follows:
```ini
web1 ansible_host=... ansible_user=... ansible_port=23
```

Make sure Ansible is able to communicate with your hosts after the change.

10. Let's create another task to make sure the latest version of `auditd` daemon is installed.
```yaml
    - name: Ensure auditd is at the latest version
      become_user: root
      ansible.builtin.yum:
        name: audit
        state: latest
```

11. We now want to add some rules to the `auditd` daemon. For that we will use the `template` built-in module. Add the following task to your playbook:
```yaml
    - name: Write the audits config file
      ansible.builtin.template:
        src: templates/auditd_rules.j2
        dest: /etc/audit/rules.d/audit.rules
```
Again, the `templates/auditd_rules.j2` file can be found in the shared repo. This file contains two rules:

- Audit all activities in `/root` directory
- Audit `sudo` usage

12. Add the following handler under `handlers` entry, as well as `notify: restart auditd` entry in **Write the audits config file** task.
```yaml
    - name: restart auditd
      become_user: root
      ansible.builtin.command: |
        service auditd restart
```
13. Run the playbook and check the status of the auditd service: `sudo service auditd status`.
14. Test that the auditing rule were applied:
    1. Execute some command as root: `sudo su -`
    2. Search for appropriate audit logs: `sudo ausearch -k using_sudo`.

### **Challenge:** add another task to your playbook that removes unused yum repositories and enables GPG key-checking

1. All tasks are configures in `yum_hardening.yaml`
2. Add `vars/main.yaml` with the following variables:
```yaml
# Set to false to disable installing and configuring yum.
os_yum_enabled: true

# List of yum repository files under /etc/yum.repos.d/ which should not be altered.
os_yum_repo_file_whitelist: []
```
Include this var file in `site.yaml`
3. Include the yum tasks YAML file in `site.yaml` by adding the following entry under `tasks:`:
```yaml
    - include_tasks: yum_hardening.yaml
```
4. Run the playbook. 

### Validating playbook tasks: `check` mode and `diff` mode

Ansible provides two modes of execution that validate tasks: check mode and diff mode. 
They are useful when you are creating or editing a playbook or role and you want to know what it will do.

In check mode, Ansible runs without making any changes on remote systems, and report the changes that would have made.
In diff mode, Ansible provides before-and-after comparisons. 

Simply add the `--check` or `--diff` options (both or separated) to the `ansible-playbook` command:

```shell
ansible-playbook -i ./inventory/hosts site.yaml --check --diff 
```

## Ansible Facts

You can retrieve or discover certain variables containing information about your remote systems, which are called **facts**.
For example, with facts variables you can use the IP address of one system as a configuration value on another system. Or you can perform tasks based on the specific host OS.

To see all available facts, add this task to a play:

```yaml
- name: Print all available facts
  ansible.builtin.debug:
    var: ansible_facts
```

Or alternatively, run the `-m setup` ad-hoc command:
```shell
ansible -i ./inventory/hosts webserver -m setup
```

As the `ansible.builtin.yum` module fits only RedHat family systems (e.g. Amazon Linux), we would like to add a condition for the **** and ** ** tasks, using the `ansible_pkg_mgr` facts variable:

```shell
    - name: Ensure httpd is at the latest version
      become_user: root
      ansible.builtin.yum:
        name: httpd-2.4*
        state: latest
      when: ansible_facts['pkg_mgr'] == 'yum'
```


## Organize the playbook using Roles

[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html) let you automatically load related vars, templates, tasks, handlers, and other Ansible artifacts based on a known file structure. 

1. Redesign your YAML files according to the following files structure:
```text
#  in the root directory of your Ansible playbook
roles/
    sshd/
        tasks/
            main.yaml
        handlers/
            main.yaml
        templates/
            sshd_config.j2
        vars/
            main.yaml
     auditd/
        tasks/
            main.yaml
        handlers/
            main.yaml
        templates/
            auditd_rules.j2
        vars/
            main.yaml      
```

By default, Ansible will look in each directory within a role for a `main.yaml` file for relevant content.

2. In `site.yaml` add the following entry in the top-play level (roles can be included in the task level also):
```yaml
roles:
    - sshd
    - auditd
```
Clean `site.yaml` from tasks and handlers according the content you copied to `sshd` and `auditd` roles.

Ansible will execute roles first, then other tasks in the play.

