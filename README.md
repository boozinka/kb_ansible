Following Kirk Byers Python Ansible Course

This course dives into Ansible as applied to Network Engineering.

### Topics covered include:

Class 1 - Ansible Fundamentals
Class 2 - Variables, Modules, Network Fact Gathering
Class 3 - Conditionals, Loops, and Configuration Templating
Class 4 - Making Network Configuration Changes (Basics)
Class 5 - Making Network Configuration Changes (Part2)
Class 6 - Imports, Includes, and Roles
Class 7 - Parsers and Dynamic Inventory
Class 8 - Additional Ansible Techniques and Debugging

Bonus Class 1 - NAPALM-Ansible
Bonus Class 2 - OS Upgrade IOS/IOS-XE, Creating your own Filter/Module


Class 1. Ansible Fundamentals

- [ ] I.    Ansible Course Introduction
- [ ] II.   Course Format
- [ ] III.  Lab Environment
- [ ] IV.   New Packaging
- [ ] V.    Collections*
- [ ] VI.   YAML (Part1)
- [ ] VII.  YAML (Part2)
- [ ] VIII. What Problems are We Trying to Solve?​
- [ ] IX.   Ansible System Components​
- [ ] X.    Connection Local​
- [ ] XI.   Inventory (Part1)
- [ ] XII.  Inventory (Part2)
- [ ] XIII. Playbook Structure


Exercises:
-----------

Note: YAML files allow you to use whatever amount of spacing you wish for indentation (as long as you are consistent). A general recommendation is to use two spaces for indentation for YAML files.

Note: YAML linters are available and can be useful in helping to make sure you are writing valid YAML. yamllint is a Python utility for checking YAML files for a few common "issues" such as duplicate dictionary keys, line length, and most importantly indentation issues. You can use this or websites such as yamllint.com to check your YAML files.


1a. Create a YAML file that is a five element list (in expanded YAML format).

In order to verify the contents of this YAML file (i.e. to print the data structure to stdout), use the Python script stored here. To run this python script you can 'git clone' this repository, or just copy/paste the contents of the script into a ".py" file on your system. Use the following command to run the script:

python print_yaml.py MYFILE.yml


1b. Create a YAML file that is a five element list, but in a compressed YAML format. Once again, use the "print_yaml.py" python script to print the contents of the YAML file to stdout.

1c. Create a YAML file that contains a dictionary representing a networking device (in an expanded YAML format). The highest level key should be the device name (for example, "rtr1"). The value corresponding to that key should be another dictionary. This inner dictionary should have the following key-value pairs (host, username, password, device_type, use_session_log). use_session_log should be a YAML-boolean, the rest of the values should be strings. Use the "print_yaml.py" python script to print the contents of the YAmL file to stdout.

1d. Duplicate the dictionary created in the previous task except this time use the compressed YAML format. Once again, print the contents of the file using print_yaml.py. The result should match the result of exercise 1c.

1e. Create a YAML file that is a nested data structure. The highest level data structure should be a dictionary with a key-name of "network_devices". The value corresponding to this key should be a two-element list. Each element of this list should contain a dictionary with six key-value pairs (host, username, password, device_type, use_session_log, ip_addresses). The ip_addresses key should point to a list of IP addresses that each network device contains (just make up three IP addresses for each device).
Once again, use the python "print_yaml.py" script to print the contents of the YAML file to stdout.


2a. Create an "INI" style inventory file. This file should have an "all:vars" section containing variables for the following:

    ansible_connection type should be set to "network_cli"
    ansible_python_interpreter should be set to "~/VENV/py3_venv/bin/python"
    ansible_user and ansible_ssh_pass should be set to the course's standard values

Additionally, add the following three groups to the inventory file:

    local
    cisco
    arista

Use the ansible-inventory --list -i ./inventory.ini to validate and inspect your inventory file, your output should look similar to the following:

{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "arista",
            "cisco",
            "local",
            "ungrouped"
        ]
    }
}


2b. Add two hosts to the arista and cisco groups and re-inspect the inventory using ansible-inventory --list -i ./inventory.ini. Additionally, use the --graph option. This option provides a more compressed view of your inventory. Your --graph output should look similar to the following:

@all:
  |--@arista:
  |  |--arista5
  |  |--arista6
  |--@cisco:
  |  |--cisco1
  |  |--cisco2
  |--@local:
  |--@ungrouped:



2c. Modify your inventory file to set the "ansible_network_os" for the cisco and arista groups to "ios" and "eos" respectively. Additionally, set the "ansible_host" for each of these hosts to the fqdn of the device (i.e. cisco1.lasthop.io, arista1.lasthop.io, etc.). Use the ansible-inventory --list -i ./inventory.ini command to inspect the inventory and validate that the network_os has been set appropriately. Additionally, add "localhost" to be a member of the "local" group (you will need to set ansible_connection=local for the localhost entry).


3a. Create a Playbook that contains a single Ansible Play. Provide a "name" for this Play. Additionally, set the "hosts" for this Play to "localhost". Finally, create a task using the "debug" module. This task should print the "ansible_host" variable to stdout. Run this Playbook, your output should look similar to the following (use the inventory you created in exercise2c):

$ ansible-playbook exercise3a.yaml -i inventory.ini

PLAY [Exercise 3a] *******************************************

TASK [Gathering Facts] ***************************************
ok: [localhost]

TASK [debug] *************************************************
ok: [localhost] => {
    "ansible_host": "127.0.0.1"
}

PLAY RECAP  **************************************************
localhost: ok=2 changed=0 failed=0 skipped=0 rescued=0 ignored=0


3b. Modify the previously created Play such that the "Gathering Facts" task is no longer enabled. The "PLAY RECAP" should now indicate that only a single task was executed.


3c. Add a second Play to the Playbook. This Play should operate against the "cisco" group, and should not gather facts. Within this Play create two tasks, the first task should use the debug module to print the "ansible_connection" variable. The second task should use the debug module to print the "ansible_host" variable. Your final output should be similar to the following:

$ ansible-playbook exercise3c.yaml -i inventory.ini

PLAY [Exercise 3a] ********************************************

TASK [Gathering Facts] ****************************************
ok: [localhost]

TASK [debug] **************************************************
ok: [localhost] => {
    "ansible_host": "127.0.0.1"
}

PLAY [Another Play] *******************************************

TASK [debug] **************************************************
ok: [cisco1] => {
    "ansible_connection": "network_cli"
}
ok: [cisco2] => {
    "ansible_connection": "network_cli"
}

TASK [debug] **************************************************
ok: [cisco1] => {
    "ansible_host": "cisco1.lasthop.io"
}
ok: [cisco2] => {
    "ansible_host": "cisco2.lasthop.io"
}

PLAY RECAP ****************************************************
cisco1: ok=2 changed=0 failed=0 skipped=0 rescued=0 ignored=0
cisco2: ok=2 changed=0 failed=0 skipped=0 rescued=0 ignored=0
localhost: ok=2 changed=0 failed=0 skipped=0 rescued=0 ignored=0


