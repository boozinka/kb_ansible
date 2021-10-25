Following Kirk Byers Python Ansible Course

This course dives into Ansible as applied to Network Engineering.

### Topics covered include:

- [ ] Class 1 - Ansible Fundamentals
- [ ] Class 2 - Variables, Modules, Network Fact Gathering
- [ ] Class 3 - Conditionals, Loops, and Configuration Templating
- [ ] Class 4 - Making Network Configuration Changes (Basics)
- [ ] Class 5 - Making Network Configuration Changes (Part2)
- [ ] Class 6 - Imports, Includes, and Roles
- [ ] Class 7 - Parsers and Dynamic Inventory
- [ ] Class 8 - Additional Ansible Techniques and Debugging

- [ ] Bonus Class 1 - NAPALM-Ansible
- [ ] Bonus Class 2 - OS Upgrade IOS/IOS-XE, Creating your own Filter/Module


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



Class 2. Modules & Network Fact Gathering

- [ ] I.    Class 2 Introduction
- [ ] II.   Varibles (Part1)
- [ ] III.  Varibles (Part2)
- [ ] IV.   Variables: set_fact and vars_prompt
- [ ] V.    host_vars and group_vars
- [ ] VI.   Ansible Modules
- [ ] VII.  Network Modules
- [ ] VIII. ios_command (Part1)
- [ ] IX.   ios_command (Part2)
- [ ] X.    ios_command Multiline Prompting
- [ ] XI.   eos_command
- [ ] XII.  cli_command
- [ ] XIII. Privilege Escalation (become/enable)


Exercises:
-----------

1a. Create a Playbook containing a Play that executes on the "arista5" host. Ensure that "gather_facts" is set to True. Create a task that uses the "debug" module to print the "ansible_facts" to stdout. Create a subsequent task that prints just "ansible_facts.net_all_ipv4_addresses" to stdout.

1b. Add tasks to your Playbook to print out inventory information about arista5. This should include both the "ansible_network_os" and the "ansible_host" variables.

1c. Create a directory called "group_vars" in the same directory as your Playbook. Within this directory, create a file named "all.yml". In this file, define a variable named "desired_eos_version" and set it to a value of "4.18.3". Add another task to your Playbook to print out the value of this "desired_eos_version" variable.

1d. In the same directory as your Playbook, create a YAML file called "my_vars.yml". Within this file, create the same variable named "desired_eos_version" as in the previous exercise, but with a different value. Load this variable from my_vars.yml by adding "vars_files: my_vars.yml" into your Playbook. Re-run the Playbook to see what happens. Which "desired_eos_version" wins? Why?

1e. Add a task to your playbook to create a new variable using "set_fact". Name this variable "device_hostname" and set the value of it equal to the "inventory_hostname" combined with the suffix ".lab.io". In a final task, print the value of this variable.


2a. Create a new directory that includes a Playbook and a "group_vars" directory. The group_vars directory should contain a "cisco" subdirectory. Inside this "group_vars/cisco" subdirectory, create a file named "bgp.yml". Inside this "bgp.yml" file create a variable for "bgp_asn" and assign it a value between 65000 and 65535. Use the "debug" module to print a message to stdout. The message should look similar to the following: 

TASK [Print BGP ASN for cisco hosts] **************************************************************************************************
ok: [cisco1] => {
    "msg": "The ASN for host cisco1 is 65001"
}
ok: [cisco5] => {
    "msg": "The ASN for host cisco5 is 65001"
}
ok: [cisco2] => {
    "msg": "The ASN for host cisco2 is 65001"
}
ok: [cisco6] => {
    "msg": "The ASN for host cisco6 is 65001"
}

2b. Create a "host_vars" directory, and a subdirectory named "cisco5" within it. Inside this, "host_vars/cisco5", create a file named "bgp.yml". Inside this file, create a variable named "bgp_asn" using a different ASN value. Re-run the Playbook. You should observe that the host_vars "bgp_asn" has higher priority than the group_vars "bgp_asn" variable.

2c. Create the following subdirectories: cisco1, cisco2, cisco6 (inside the host_vars directory). The "host_vars/cisco5" subdirectory should already exist. Note, the directory names must exactly match the Ansible "inventory_hostname". In each of these ciscoX directories create a file named "ip_addresses.yml". Inside this file create a "loopback0" variable and assign this variable a unique IPv4 address (for example, 1.1.1.1 for cisco1).

Inside the same ciscoX directory, create a second file named "bgp.yml". In this file create a variable "bgp_router_id" and assign it a value of the "loopback0" variable you just created (remember your  "{{ loopback0 }}" notation). The "cisco5" bgp.yml file should contain both the "bgp_asn" and the "bgp_router_id".

Finally, modify your Playbook such that your output looks similar to the following. 

TASK [Print BGP ASN for cisco hosts] **************************************************************************************************
ok: [cisco2] => {
    "msg": "The ASN for host cisco2 is 65001, the router-id is 2.2.2.2"
}
ok: [cisco1] => {
    "msg": "The ASN for host cisco1 is 65001, the router-id is 1.1.1.1"
}
ok: [cisco6] => {
    "msg": "The ASN for host cisco6 is 65001, the router-id is 6.6.6.6"
}
ok: [cisco5] => {
    "msg": "The ASN for host cisco5 is 65535, the router-id is 5.5.5.5"
}

The above exercise demonstrates that you can store additional inventory variables in host_vars, and group_vars. These subdirectories also allow you to divide your YAML into multiple files which can simplify inventory management.


3a. Create a Playbook that operates against the "nxos" group. This Playbook should contain a Play that uses the "nxos_command" module to gather the output from "show version". Register the result of this command to a variable and print the variable out in a second task.

3b. Modify the Playbook to run both "show version" and "show lldp neighbors". Once again, "register" the result and print the output.

3c. Modify the debug task to print only the output of "show lldp neighbors" to stdout. You should be accessing my_variable["stdout_lines"][1] (where "my_variable" is the name of the variable that you "registered"). Alternatively, you could access my_variable["stdout"][1].

3d. Copy the "ansible-hosts.ini" file from your home directory; modify this file to no longer contain the "ansible_ssh_pass" variable. Re-execute your Playbook, pointing to use this modified inventory file (you can accomplish this by using "-i ./ansible-hosts.ini"). Use Ansible command-line arguments to pass the ansible_ssh_pass value. Your Playbook output should be the same as the previous task.


4a. Create a Playbook that clears the logging buffer on the cisco6 device. The command to clear the logging buffer is: "clear logging". This command will prompt for confirmation ("Clear logging buffer [confirm]"). Ensure that your task handles the confirmation appropriately. Register and print the results of the task to stdout. Remember that "prompt" takes a regular expression so you either need to simplify it or backslash escape special regex characters (I strongly recommend you simplify your pattern to avoid regular expression characters, if possible).


5a. Create another Playbook that operates against the juniper group. Using the "junos_command" module, run the "show interfaces terse" command and store the output of this in a variable named "interfaces". Use the debug module to print this variable to stdout (to inspect it).

5b. By using "stdout_lines", access and print out the "fxp0.0" interface information. You can potentially accomplish this by using the below pattern: 

"{{ interfaces['stdout_lines'][0][21] }}"
Note, it is possible that the index-number "21" might change.

Note2, there are better patterns that can be used (instead of hard-coding a specific index). We will learn these patterns later in the course including using a loop and a conditional (or potentially using a string/regex pattern search).

Your output should look similar to the following (i.e. it should contain the devices IP address on the 172.30.0.0/24 network). 

TASK [debug] **********************************************
ok: [vmx1] => {
    "msg": "fxp0.0                  up    up   inet     172.30.0.221/24 "
}
ok: [vmx2] => {
    "msg": "fxp0.0                  up    up   inet     172.30.0.156/24 "
}

5c. Now how would you extract only the "172.30.0.X/24" from that line? In other words, how would you print out only the following: 

TASK [debug] *****************************************************
ok: [vmx1] => {
    "msg": "Primary IP: 172.30.0.221/24"
}
ok: [vmx2] => {
    "msg": "Primary IP: 172.30.0.156/24"
}

Reminder, you can execute certain string methods inside Ansible (in a Jinja2 context). For example, you can do: "{{ my_var.split() }}"  to split the string on consecutive white space. This will return a list of words; you can then access the last element of this list by using [-1].


6a. Create a Playbook that executes a task against the arista group. Using the "eos_command" module, execute "show ip arp" and register the output. Print this registered output to stdout.

6b. Add an additional set of tasks to use eos_command to execute "show ip arp | json". Once again register this output and print it to standard output. For the "show ip arp | json" output is a string returned or is structured data returned?



Class 3. Conditionals, Loops and Configuration Templating

- [ ] I.    Class 3 Introduction 
- [ ] II.   Idempotency 
- [ ] III.  Tags, Limit, Check 
- [ ] IV.   Conditionals 
- [ ] V.    Loops
- [ ] VI.   Loops and Dictionaries
- [ ] VII.  Loops and Conditionals
- [ ] VIII. Jinja2 Introduction
- [ ] IX.   Jinja2 Variables
- [ ] X.    Jinja2 Conditionals
- [ ] XI.   Jinja2 For-Loops 
- [ ] XII.  Jinja2 Looping over Dictionaries
- [ ] XIII. Jinja2 Includes
- [ ] XIV.  Jinja2 Modular Includes


Exercises:
-----------

1a. Construct an Ansible playbook that contains a single play. The play should execute the following:

* If the ansible_network_os is "eos" then "eos_command" should be used to retrieve "show ip arp"
* If the ansible_network_os is "ios" then "ios_command" should be used to retrieve "show ip arp"
* If the ansible_network_os is "junos" then "junos_command" should be used to retrieve "show arp" (notice slight command differences).
* For each of the above, register the output into a unique variable for example, show_ip_arp_eos.
* Print out the registered output only for the EOS devices.

Note, you will be required to disable fact gathering for the Juniper device. There is an issue with the Juniper lab device and Ansible where fact gathering will fail.

1b. Expand on your playbook that you created in exercise1a. Add tags into your playbook such that you can execute only the "eos", "ios", or "junos" section of your playbook depending on which tag you provide. For example, if I provide the "eos" tag, then only the "eos" tasks should be run.

1c. Use the "--limit" argument and your playbook from exercise1a to execute the playbook only for "arista5".


2. Create a Playbook that executes against the nxos1 switch. This playbook should use a "loop" and the "nxos_command" module to execute "show vlan id" for each of the following four VLANs: 1, 2, 3, 4. Register the output of this task to a variable named "vlans".

Retrieve the output of "show vlan id 4" from your registered "vlans" variable and use the debug module to print this output to stdout. You will probably have to inspect this "vlans" variable to see how the multiple iterations of the loop affect the returned data structure.


3. Create a Playbook that executes against the cisco1 and cisco2 routers. This playbook should execute "show lldp neighbors" using the ios_command module. Register the output and extract "stdout_lines[0]" from this output. This will be a list of the output lines.

Loop over these lines and find the LLDP entry that contains "twb-sf-hpsw1". This line should be present on both cisco1 and cisco2. Save this line containing "twb-sf-hpsw1" as a new variable named lldp_entry.

Using this new lldp_entry variable and the split() method use set_fact to extract the following three items from the line: remote_device, local_intf, remote_intf. Remember that split() will break the line up in consecutive white space and will return a list. So with the following line: 

twb-sf-hpsw1        Fa4            120        B      15

lldp_entry.split() would return the following list: 

['twb-sf-hpsw1', 'Fa4', '120', 'B', '15']

In this above output, remote_device is "twb-sf-hpsw1", local_intf is "Fa4" and remote_intf is "15".

Print the following three variables to stdout: remote_device, local_intf, remote_intf. Your output should look similar to the following: 

ok: [cisco1] => {
    "msg": [
        "Remote device: twb-sf-hpsw1",
        "Local intf: Fa4",
        "Remote intf: 15"
    ]
}
ok: [cisco2] => {
    "msg": [
        "Remote device: twb-sf-hpsw1",
        "Local intf: Fa4",
        "Remote intf: 13"
    ]
}

Note, there are other, better ways to solve problems similar to this. In particular, you can use parsers such as TextFSM and Cisco-Genie to accomplish the parsing for you. We will talk about these more later in the course.


4. Using a single Jina2 template and an Ansible Playbook generate a configuration matching the following for each of the four Arista switches:

https://github.com/twin-bridges/ansible_course/blob/master/class3/exercises/exercise4/CFGS/arista5.txt

The four Arista switch configurations should be identical to each other except the hostname and the VLAN1 IP address will change. Your output filenames should be stored in a separate directory and should be named "{{ inventory_hostname }}.txt" (for example, ./CFGS/arista5.txt).

The Jinja2 template should have variables for the following: 

hostname          # pull from inventory_hostname
ntp_server1       # set in group_vars/all.yml
timezone          # set in group_vars/all.yml
vlan1_ip_address  # set in host_vars/aristaX.yml (see table)
vlan1_netmask     # set in host_vars/aristaX.yml (always "24")
def_gateway       # group_vars/arista.yml (always 10.220.88.1)

For the "Ethernet" interfaces section, you should use a Jinja2 for-loop in your template.

Additionally, each of the interfaces should be configured with the proper VLAN (see reference configuration here). This VLAN information should be stored in group_vars/arista.yml in some way (your data structure will need to create a binding in some way between the interface name and the VLAN assignment). 

Table of IP addresses:
-----------------------
arista5       10.220.88.32/24
arista6       10.220.88.33/24
arista7       10.220.88.34/24
arista8       10.220.88.35/24

These generated configurations when complete will be identical to what is configured on the Arista devices (except I have dropped the "username/password" section as I didn't want that checked into GitHub).


5. Use Jinja2 templating and an Ansible playbook to generate the following interface and BGP configurations for nxos1 and nxos2 respectively.
  

##### nxos1 #####
interface Ethernet1/4
  ip address 172.31.254.1/30
!
interface loopback101
  ip address 172.31.101.101/32
!
interface loopback102
  ip address 172.31.102.101/32
!
!
feature bgp
router bgp 22
  router-id 172.31.101.101
  address-family ipv4 unicast
    network 172.31.101.101/32
    network 172.31.102.101/32
  neighbor 172.31.254.2
    remote-as 22
    description configured by ansible
    address-family ipv4 unicast
!


##### nxos2 #####
interface Ethernet1/4
  ip address 172.31.254.2/30
!
interface loopback101
  ip address 172.31.101.102/32
!
interface loopback102
  ip address 172.31.102.102/32
!
!
feature bgp
router bgp 22
  router-id 172.31.101.102
  address-family ipv4 unicast
    network 172.31.101.102/32
    network 172.31.102.102/32
  neighbor 172.31.254.1
    remote-as 22
    description configured by ansible
    address-family ipv4 unicast
!

For this process, you should have two separate Jinja2 templates: one for the interfaces section and one for the BGP configuration.

The following items should be variables in your Jinja2 templates: 

interfaces
{{ eth1_4_ip_address }}
{{ eth1_4_netmask }}
{{ loopback101_ip_address }}
{{ loopback101_netmask }}
{{ loopback102_ip_address }}
{{ loopback102_netmask }}

bgp
{{ bgp_asn }}
{{ bgp_peer_ip }}

The BGP networks that are announced should also be made into variables in some way (these values would ultimately be the loopback101 and loopback102 IP addresses and netmasks).
I recommend that you define all of these variables in host_vars and group_vars. In my reference solution, I only defined the {{ bgp_asn }} in group_vars; everything else was defined in host_vars.

I also defined the networks to advertise as follows (for example, in host_vars/nxos1/bgp.yml): 

bgp_peer_ip: 172.31.254.2
bgp_advertise: 
  - "{{ loopback101_ip_address }}/{{ loopback101_netmask }}"
  - "{{ loopback102_ip_address }}/{{ loopback102_netmask }}"

In other words, I defined the variables for {{ loopback101_ip_address }} and {{ loopback101_netmask }} in host_vars/nxos1/interfaces.yml and then used these variables in my bgp.yml file.


One other note, you can use the Ansible assemble module to assemble multiple files into one file. In other words, if you check my reference solution, you will see I used Jinja2 templating to generate one configuration file for the interfaces and one configuration file for the BGP configuration. I then used the assemble module to take these two separate files and create one unified configuration file from them.

In a future lesson, we will take these generated configurations and deploy them to nxos1 and nxos2.


Class 4. Making Network Configuration Changes (Basics)

- [ ] I.    Ansible Configuration Overview
- [ ] II.   Resource Modules
- [ ] III.  Resource Modules interfaces
- [ ] IV.   Resource Modules l2_interfaces
- [ ] V.    Resource Modules l3_interfaces and VLANs
- [ ] VI.   Feature Modules IOS
- [ ] VII.  Feature Modules EOS and NX-OS
- [ ] VIII. net_* Modules
- [ ] IX.   Handlers
- [ ] X.    Assert


Exercises:
-----------


1. Configure a custom login banner on the four Cisco IOS/IOS-XE devices using the ios_banner module. Use a "write mem" handler to automatically save the configuration. This "write mem" handler should only execute if configuration changes were made.


2. Use the ios_system module to configure the domain-name, hostname, and two name-servers on cisco1. The new hostname should be "cisco1-tmp" and should be stored in host_vars. The domain-name should be "bogus.com" and the name-servers should be "8.8.8.8" and "8.8.4.4". Both the domain-name and the name-servers should be stored in group_vars/all.yml. This playbook should be idempotent.


3. Use the nxos_l3_interfaces resource module to configure an IP address on Ethernet1/4 on both NX-OS switches. The interface name (Ethernet1/4), the IP address, and the netmask should be stored in host_vars. You should be using the "merged" state for this operation. If "Ethernet1/4" is being used by another student, then you can use either "Ethernet1/3" or "Ethernet1/2". For IP network, choose a random /24 network from the 10.227.X.X range. Use 10.227.X.1 for nxos1 and 10.227.X.2 for nxos2.

After configuring the interfaces, use the net_ping module to verify IP connectivity between the two NX-OS switches. Using an assert statement(s) in your playbook, verify the ping worked correctly (>=80% of the ping responses should be returned).


4. Use the eos_vlans resource module to create a VLAN and to assign the VLAN a name on all four of the Arista switches. The VLAN ID should be in the VLAN range from VLAN 200 to 299.

After this VLAN is created, then use the eos_l2_interfaces resource module to assign that VLAN to one of the interfaces on all four of the Arista switches. You should either Ethernet5, Ethernet6, or Ethernet7 (do NOT use Ethernet1). Your VLAN ID, VLAN name, and interface name should be stored in either host_vars or group_vars.

Using eos_command and a show command(s), verify that your VLAN exists and that the Ethernet interface you chose was assigned to that interface (I used "show vlan | json"). This verification will probably require that you use an assert statements.


5. Use the nxos_interfaces resource module to configure "Ethernet1/3" on both nxos1 and nxos2 as a layer2 port (i.e. configure "switchport" on that interface). If "Ethernet1/3" is being used by another student then use either "Ethernet1/1" or "Ethernet1/2" instead.

Use the l2_interface module to configure the port for trunking ("switchport mode trunk). Note, this is the Ansible issue that requires us to use the deprecated feature module instead of using the newer resources module.

Using the l2_interfaces resource module configure the trunk native VLAN to VLAN4. Yes, it is ugly to use both "l2_interface" and "l2_interfaces", but I wanted you to get more experience with the resource modules.

Using the nxos_command module execute a show command on the switches and capture that output. Use this output and the Ansible assert module to verify that the interface is trunking and that the native VLAN is correct. I used 'show interface {{ intf_name }} trunk | json' for my show command.

The intf_name, intf_mode (layer2), switchport_mode (trunk), and the native_vlan should all be stored in host_vars/group_vars and should NOT be hard-coded into your Ansible playbook.


Class 5. Making Network Configuration Changes (Part2)

- [ ] I.    Introduction to platform_config Modules
- [ ] II.   ios_config
- [ ] III.  ios_config diff
- [ ] IV.   nxos_config and junos_config
- [ ] V.    Using cli_config
- [ ] VI.   Config Hierarchy and platform_config
- [ ] VII.  Deploying Jinja2 Generated Configurations
- [ ] VIII. SSH Key Authentication
- [ ] IX.   Module Path
- [ ] X.    Collections*


Exercises:
-----------

1. Configure the following items on all of the lab network devices (4 x Cisco IOS/IOS-XE devices, 4 x Arista devices, 2 x NX-OS devices, and 2 x Juniper vMX devices): 

---
ntp_server1: 130.126.24.24
ntp_server2: 152.2.21.1
domain_name: bogus.com
dns_server1: 8.8.8.8
dns_server2: 8.8.4.4

The above variables should all be stored in group_vars or host_vars. You can use the following templates as a reference for the particular CLI syntax for each platform.

Configuration templates

Your playbook should be idempotent for all the devices. Additionally, you should use the ios_config, eos_config, nxos_config, and junos_config modules to accomplish this task.


2. Repeat exercise1 except now use the "cli_config" module for all of the devices (instead of ios_config, eos_config, nxos_config, and junos_config). Once again your final playbook should be idempotent.

Note, I had to specify "ansible_connection: network_cli" for the Juniper vMXs as the cli_config module requires network_cli.


3a. Using the ios_config module and the configuration hierarchy arguments (for exampe: parents, before, match, replace) configure a ten-line access-list on the cisco5 and cisco6 devices. Here is an example ACL you could use: 

ip access-list extended TEST-ANSIBLE1
 permit ip host 10.1.1.1 any
 permit ip host 10.1.1.2 any
 permit ip host 10.1.1.3 any
 permit ip host 10.1.1.4 any
 permit ip host 10.1.1.5 any
 permit ip host 10.1.1.6 any
 permit ip host 10.1.1.7 any
 permit ip host 10.1.1.8 any
 permit ip host 10.1.1.9 any
 permit ip host 10.1.1.10 any

Use the ios_command module to verify that the ACL is configured (basically execute: "show access-list <ACL-NAME>" and then use the debug module to print out the ACL).

Your playbook should be idempotent.


3b. Re-order your access-list such that one of the last three access-list lines is now at the beginning. Additionally convert this moved ACL entry from being a "permit" statement to being a "deny" statement. Ensure that executing your new playbook results in the correct final access-list being configured. For example, my new access-list would look as follows: 

ip access-list extended TEST-ANSIBLE1
 deny   ip host 10.1.1.9 any
 permit ip host 10.1.1.1 any
 permit ip host 10.1.1.2 any
 permit ip host 10.1.1.3 any
 permit ip host 10.1.1.4 any
 permit ip host 10.1.1.5 any
 permit ip host 10.1.1.6 any
 permit ip host 10.1.1.7 any
 permit ip host 10.1.1.8 any
 permit ip host 10.1.1.10 any

Once again use the "ios_command" module and the "debug" module to verify that your updated ACL is properly configured.

Your playbook should be idempotent.


4. Using the configurations generated from class3-exercise5 configure both BGP and the relevant interface on both nxos1 and nxos2.

In other words, class3-exercise5 was an exercise where we used Jinja2 to generate both BGP and interface configurations for nxos1 and nxos2, BUT we did not deploy those configurations. Now you should use nxos_config module to deploy those configurations.

Verify the BGP session reached the established using the nxos_command module. For this verification task, you can simply execute "show ip bgp summary" using nxos_command and visually verify its output using the "debug" module.


5. Using an SSH key for authentication, execute the "show users" command on both cisco1 and cisco2. You should use the ios_command module to accomplish this. Remember for this exercise that you will need to use the SSH key located here:

ansible_ssh_private_key_file="~/.ssh/student_key"

Additionally, you will need to switch the "ansible_user" to "student1".


Using the "assert" module, verify that "student1" is present in the output of "show users". This will help verify that you are properly using the SSH key and not accidentally connecting using the "pyclass" username/password.



Class 6. Imports, Includes, and Roles


 - [ ] I.    Dynamic (include) vs Static (import)
 - [ ] II.   Import-Include and Tags
 - [ ] III.  Import-Include and Conditionals
 - [ ] IV.   Dynamic or Static - Which should you use?
 - [ ] V.    include_tasks and import_tasks
 - [ ] VI.   include_vars
 - [ ] VII.  Roles
 - [ ] VIII. Roles (Part2)
 - [ ] IX.   Playbook Composition


Errata / Clarification:
------------------------

Expanding on the Ansible tag behavior when using import_tasks or include_tasks

In the videos, I talked a lot about having tags directly associated with the import_tasks or include_tasks statements in the main playbook. But I didn't sufficiently discuss the behavior of import_tasks and include_tags when there are no tags in the main playbook and all of the tags are in the subtask file (or potentially embedded in a role).

For example, consider these two sub-tasks: 

	# file named subtask1.yml
	- debug:
	    msg: "Hello1"
	  tags: test1
	
	- debug:
	    msg: "Hello2"
	  tags: test2

If I execute these sub-tasks using the following playbook and without using any tags... 

	---
	- name: Testing
	  hosts: local
	  tasks:
	    - name: Test tags
	      import_tasks: subtask1.yml
	      
then you get the output you would expect (i.e. all of the sub-tasks properly execute).


But what happens when you do: 

	$ ansible-playbook test1.yml --tags test1

In this case, the import_tasks statement is completely transparently to the tag being applied on playbook execution. Or worded differently, it is like the "import_tasks" statement doesn't exist and we just "statically" have the sub-tasks in our main playbook. Consequently, the sub-tasks will execute or not execute based on the tags that these sub-tasks themselves possess. 

Thus we see the output as follows: 

	$ ansible-playbook test1.yml --tags test1
	
	PLAY [Testing] ******************************
	
	TASK [Gathering Facts] **********************
	ok: [localhost]
	
	TASK [debug] ********************************
	ok: [localhost] => {
	    "msg": "Hello1"
	}
	
	PLAY RECAP **********************************
	localhost : ok=2 changed=0 ...   

The subtask with the "test1" tag was executed and its message displayed to the screen (i.e. "Hello1")


Now what happens when we convert this over to "include_tasks"? 

	---
	- name: Testing
	  hosts: local
	  tasks:
	    - name: Test tags
	      include_tasks: subtask1.yml

In this case the "include_tasks" statement is dynamic and the entire "Test tags" task is included or excluded based on whether we possess the tag or not. Consequently, if we execute our playbook as below, then the "include_tasks" statement in the main playbook will not execute (as it does NOT have the "test1" tag). In other words, the entire include_tasks operation will be skipped including all of the sub-tasks. 


	$ ansible-playbook test1.yml --tags test1
	
	PLAY [Testing] *****************************************
	
	TASK [Gathering Facts] *********************************
	ok: [localhost]
	
	PLAY RECAP *********************************************
	localhost                  : ok=1    changed=0  ...

Here "Gathering Facts" is executed, but nothing else.

How do we fix this? In other words, we have tags embedded in our playbook structure, how do we convince Ansible to drill down deeper and to not skip them (when using "include_tasks")? The easy answer is to add the "always" tag to your "include_tasks" statement. For example: 

	---
	- name: Testing
	  hosts: local
	  tasks:
	    - name: Test tags
	      include_tasks: subtask1.yml
	      tags: always

This "always" tag will tell ansible to always execute this task regardless of the tags you pass in at playbook execution (unless you intentionally skip it using "--skip-tags always").

Re-executing our playbook with the "always" tag applied to the "include_tasks" operation thus yields: 

	$ ansible-playbook test1.yml --tags test1
	
	PLAY [Testing] ******************************************
	
	TASK [Gathering Facts] **********************************
	ok: [localhost]
	
	TASK [Test tags] ****************************************
	included: /home/student5/EP/test1/subtask1.yml for localhost
	
	TASK [debug] ********************************************
	ok: [localhost] => {
	    "msg": "Hello1"
	}
	
	PLAY RECAP **********************************************
	localhost                  : ok=3    changed=0 ...

You can see in the output that the debug task with the "test1" tag did in fact execute.


Exercises:
-----------

1a. Create a playbook that runs against localhost. In this playbook, create a task that uses "include_tasks" and loads in an external sub-tasks file named "subtask1.yml". The task in the main playbook should have a loop that loops over four IP addresses. The sub-tasks file should have a "debug" task that prints out the IP address.

1b. Add the name of your sub-tasks file into "host_vars/localhost.yml". Convert your "include_tasks" statement in your main playbook to use the variable defined in host_vars. The rest of the task and sub-task should remain the same (i.e. looping over four IP addresses and printing them out).

1c. Create a file named "subtask2.yml" that has three "debug" tasks. These debug tasks should each print out slightly different messages. Additionally, these three sub-tasks should each have their own "tag" associated with them. Create a new main playbook that uses "include_tasks" to execute the tasks in "subtask2.yml". No loop is necessary in this exercise. What happens if you execute your playbook and pass in one of the "tags" defined in "subtask2.yml". Does the sub-task actually execute? Why not? At this point, it is assumed that the main playbook has no tags defined in it.

While still using "include_tasks", how could you correct the main playbook such that the proper sub-task would execute if you use the sub-tasks corresponding "tag"? For reference, see the "Expanding on the Ansible tag behavior when using import_tasks or include_tasks" section in this email.


2a. Convert exercise1a over to use "import_tasks" instead of "include_tasks". Where do you need to relocate the loop for proper execution?

2b. Try to convert exercise1b over to "import_tasks" instead of "include_tasks" while using a variable from inventory. Will you be able to do this? Why not? How could you use a variable for the file name while still using "import_tasks"? Hint, what are some other variable locations besides inventory where you could define the sub-tasks file name?

2c. Convert exercise1c over to use "import_tasks" instead of "include_tasks". If no tags are defined in the main playbook (i.e. on the "import_tasks" task), then what happens upon ansible-playbook execution (in other words, you pass in a "tag" via ansible-playbook and that tag only exists in the sub-task file)? Does the sub-task execute or not? Why does the sub-task execute (note, see the "Errata/Clarification section earlier in this email").


3. Use import_tasks and an Ansible conditional to load an external task file that configures the Cisco IOS devices for DNS, NTP, and for a domain-name. Use a second import_tasks statement and a conditional to configure the same thing for the Cisco IOS-XE devices. Both configurations should use the "ios_config" module and should be idempotent.


4. Construct a playbook that executes against the Arista, Cisco IOS/IOS-XE, and Cisco NX-OS lab devices. The playbook should consist of a single Ansible play. The tasks for each platform should configure the global parameters (DNS servers, NTP servers, and domain-name). The actual configuration tasks for each platform should be imported/included from an external task file per platform.

You should make a distinction between Cisco IOS and IOS-XE since there are slight syntactical differences for their DNS configurations. Your top level playbook should also have tags corresponding to "ios", "ios-xe", "eos", and "nxos" such that you could execute your playbook with that tag and only configure that platform (yes there are other ways you could do this using --limit given our current inventory structure, but with a different inventory structures you might be forced into tags).

Make sure your playbook works properly with no tags (i.e. all of the platforms are configured).

Make sure your playbook works properly using tags (i.e. only that platform is configured).


5. Create an Ansible role that configures NTP on the IOS, IOS-XE, Arista, and NX-OS devices. The Ansible role should use "ios_config", "eos_config", and "nxos_config" to accomplish this. In each case, an external Jinja2 template should be used (in other words, the "src" argument to ios_config/eos_config/nxos_config should be used). All of the configuration tasks for this role should be located in "tasks/main.yml". All of the variables and Jinja2 templates should be included in the role.


6. Create an Ansible role that configures VRF-lite on the cisco5 and cisco6 devices (see the reference configuration below). This same configuration should be deployed to both routers. You should make variables out of the VRF names, route distinguishers, and VRF-interfaces (i.e. the interface a given VRF is assigned to). All the elements used to accomplish this configuration should be included in the role (tasks, variables, templates). 

--------
ip vrf blue
 rd 65000:1
!
ip vrf red
 rd 65000:2
!
interface Loopback98
 ip vrf forwarding blue
!
interface Loopback99
 ip vrf forwarding red
--------


Class 7. Parsers and Dynamic Inventory


 - [ ] I.    hostvars
 - [ ] II.   block-rescue-always
 - [ ] III.  The Parsing Problem
 - [ ] IV.   pipe JSON
 - [ ] V.    TextFSM + Ansible
 - [ ] VI.   Genie  
 - [ ] VII.  Ansible + regex_replace
 - [ ] VIII. Ansible + regex_findall
 - [ ] IX.   Ansible + regex_search (Part1)
 - [ ] X.    Ansible + regex_search (Part2)
 - [ ] XI.   Dynamic Inventory
 - [ ] XII.  Dynamic Inventory Example
 - [ ] XIII. An Inventory Directory


Exercises:
-----------

1. Using class5, exercise4 as a base solution, change this earlier exercise such that you do NOT hard-code the "bgp_peer_ip" in inventory. In other words, in our earlier solution, we had something similar to the following embedded in our inventory: 

$ cat host_vars/nxos1/bgp.yml 
bgp_peer_ip: 172.31.254.2
Consequently, we hard-coded the "nxos2" BGP peer IP address in our inventory for nxos1 (and vice versa).

In this new solution, convert over and use "hostvars" instead. In other words, nxos1 should access the hostvars for "nxos2" and look up this BGP peer IP address which is defined in the nxos2 inventory (using hostvars).

If necessary, just use my earlier class5, exercise4 solution as the starting point for solving this problem.


2. See below:

****
Note, this block/rescue behavior and recovering the password is broken in the current version of Ansible. Consequently, you will need to skip this exercise or alternatively downgrade to ansible 3.3.0 and ansible-base 2.10.8

See https://github.com/ansible-collections/ansible.netcommon/issues/133
****


Using a "block" and a "rescue" statement execute "eos_config" and configure two DNS servers. For the block section, you should intentionally set an invalid password in the "eos_config" task such that your authentication will fail. You might need to use a section similar to the following to accomplish this: 

- name: Attempt configuration using an invalid password
  vars:
    ansible_ssh_pass: "invalid"
  eos_config:
    # remaining lines for task

Then in the rescue section, you would need to set the password back to the correct value. For this task, you should use an environment variable so you don't hard-code the lab password in the playbook. 

  vars:
    # Use environment variable to avoid hard-coded passwd
    ansible_ssh_pass: "{{lookup('env','ANSIBLE_PASSWORD')}}"

The rescue section of the playbooks should properly configure the two DNS servers using "eos_config". Consequently, the general pattern for this playbook will be--the block section will fail authentication and then the rescue section will retry this operation and should succeed.


3a. Exercise1 of this lesson should create a valid BGP session between nxos1 and nxos2. Additionally, each router should be exchanging announcing two BGP prefixes. Use the "show ip bgp summary" command, the nxos_command module, a TextFSM template (the ntc-template, "cisco_nxos_show_ip_bgp_summary.template"), and Ansible's parse_cli_textfsm filter to extract structured BGP information.

From this structured data, add an ansible "assert" statement that checks for the following: 
•	The "STATE_PFXRCD" field should not contain "Shut" (short for Shutdown).
•	The "STATE_PFXRCD" field should not contain "Idle" (BGP has been configured, but not transitioned to the established state).
•	The "STATE_PFXRCD" field should have at least two BGP prefixes.
This process will return an empty list if BGP has not been configured.

3b. Using the ntc-templates index file, and ntc_parse, retrieve the output of "show vlan" (as structured data) from the four Arista devices. You will likely need to define the following three variables to accomplish this: 

  vars:
    platform: "arista_eos"
    command: "show vlan"
    # where {{ username }} is the name of your lab user
    textfsm_index: "/home/{{ username }}/ntc-templates/ntc_templates/templates/"
Display your returned data structure to standard output.


4a. Using genie and the "clay584.genie" collection execute "show interface" on the two NX-OS switches. Use the "parse_genie" filter to convert this output to structured data.

Print the returned data structure to standard out using "debug" and verify that this data structure is in fact structured data (instead of a string).

4b. Repeat the same pattern as exercise4a except this time execute "show version". From this output extract the software version and print it to the screen.


5a. Execute "show lldp neighbors" on both of the NX-OS devices. Use regular expressions and the regex_findall() filter to extract the following: remote_name, local_interface, remote_interface.

Print these three fields out the the screen using a data structure (a list or a dictionary for the outermost data structure).

5b. Use regex_search and "show version" to extract the software version from each of the Arista devices. Display this software version to standard output. Note, you could also solve this problem on the Arista's using pipe JSON, but here the explicit purpose is to use regular expressions.


6. [Optional - requires Python] - Expand the dynamic inventory script located here such that all the devices located in Ansible inventory (~/ansible-hosts.ini) are included in the dynamic inventory script. You should just hard code the device definitions inside the script such that they get outputted properly as JSON (i.e. hard-code them in the script using Python data structures).

Ensure your script works properly when executed as follows: 

$ ./your_inv_script.py --list
# Where "nxos1" is some host in inventory
$ ./your_inv_script.py --host nxos1
In a real dynamic  inventory scenario, you would be pulling the device and group information from external systems via APIs; converting to the proper data structure(s), and then outputting these data structures in JSON. Consequently, in this exercise, we are only really doing the last part of this (the proper output in JSON format so Ansible can ingest the inventory information).

When your script is done, the output of "ansible-inventory --graph -i ./your_inv_script.py" should look as follows: 

$ ansible-inventory --graph -i ./dyn_inv.py 
@all:
  |--@arista:
  |  |--arista5
  |  |--arista6
  |  |--arista7
  |  |--arista8
  |--@cisco:
  |  |--cisco1
  |  |--cisco2
  |  |--cisco5
  |  |--cisco6
  |--@juniper:
  |  |--vmx1
  |  |--vmx2
  |--@local:
  |  |--localhost
  |--@nxos:
  |  |--nxos1

  |  |--nxos2
  |--@ungrouped:



Class 8. Additional Ansible Techniques and Debugging


- [ ] I.    Lookups
- [ ] II.   Filters (Part1)
- [ ] III.  Filters (Part2)
- [ ] IV.   Plugins 
- [ ] V.    Data Structures and Zip (Part1)
- [ ] VI.   Data Structures and Zip (Part2)
- [ ] VII.  Zip and Combine
- [ ] VIII. List Concatenation
- [ ] IX.   Ansible Debugging
- [ ] X.    Ansible Debug Examples (Part1)
- [ ] XI.   Ansible Debug Examples (Part2)
- [ ] XII.  Vault


Exercises:
-----------

1. Use TextFSM and the below ntc-template to retrieve "show lldp neighbors" from the two NX-OS switches:

cisco_nxos_show_lldp_neighbors.template

Convert the data structure returned via TextFSM from a list of lists to a dictionary.

The new dictionary format should be: the keys are the local interface name and the corresponding value is the remote device name.

Inside Ansible, you should use a loop and the "combine" filter to accomplish this task. You should print your final data structure to the screen as part of your playbook. Your final data structure should look similar to the following (this is only showing nxos1): 

    "lldp_map": {
        "Eth1/1": "nxos2.lasthop.io",
        "Eth1/2": "nxos2.lasthop.io",
        "Eth1/3": "nxos2.lasthop.io",
        "Eth1/4": "nxos2.lasthop.io"
    }

2. Create a custom Ansible inventory for the Arista devices that does NOT contain either the ansible_user or the ansible_ssh_pass.

Create an Ansible playbook. In this playbook, create variables for both 'ansible_ssh_pass' and for 'ansible_user'. The 'ansible_ssh_pass' variable should be set using a "lookup" and the ANSIBLE_PASSWORD environment variable (this environment variable should already be set in the lab environment). In other words, you should not hard-code the password in the playbook; instead you should be reading it from the referenced environment variable.

Your playbook should successfully execute the "show vlan" command on all of the remote Arista devices using the eos_command module (use the "-i new_inventory_file.ini" to use the new inventory file you created). Print the returned output from "show vlan" to the screen to verify the playbook executed correctly.


3. On the four Arista switches create a playbook that retrieves the switching table using 'pipe json' (i.e. 'show mac address-table | json'). From this output, convert the returned data structure to a dictionary. This new dictionary should use the mac-addresses as the keys and the source interfaces as the values (i.e. for a given mac-address the corresponding value should be the interface that this mac-address originated on).

You should accomplish this data structure conversion using 'map-attribute', 'zip', and then casting as a 'dict'. For each Arista switch, print the resulting dictionary to standard output.


4. Using the four Arista switches and the same 'show mac address-table | json' command, create a playbook that creates a list of all of the mac-addresses in the switching table (for each switch). In order to do this, you should use list concatenation and a loop.


5. Configure the following VLANs on nxos1 and nxos2 (use the nxos_vlans module to accomplish this): 

nxos1
- vlan_id: 100
  name: blue100
- vlan_id: 101
  name: blue101

nxos2
- vlan_id: 200
  name: blue200
- vlan_id: 201
  name: blue201
In the same playbook, after the VLANs have been configured, create a new play (or new tasks) that does the following:

a. Uses the nxos_command module to execute "show vlan | json" and records this output.
b. Uses Ansible set filters to determine the common VLANs that are configured on both nxos1 and nxos2. Print these common VLANs to standard output.
c. Uses Ansible set filters to determine the unique VLANs that are only configured on nxos1. Print these to standard output.
d. Uses Ansible set filters to determine the unique VLANS that are only configured on nxos2. Print these to standard output.

Note, you will probably need to use "hostvars" to accomplish this exercise. In other words, when executing on nxos1, you will need to reference the VLANs configured on nxos2 using hostvars['nxos2']...

6. Exercise6 contains a set of playbooks (exercise6a.yml through exercise6g.yml). For reference, see the exercise directory here.

Each of these playbooks will fail (i.e. not execute properly). You should "git clone" this repository to your lab environment (or otherwise copy the six playbooks; you will also need to copy any of the TextFSM templates located in that exercise6 directory).

Your job for each of these playbooks is to find and correct the error in each playbook. 

In general, the playbook should only contain one error. Note, the error may or may not result in an actual Ansible execution failure (i.e. ansible-playbook detecting the task as failed and stopping execution). Or worded differently, a couple of the playbooks execute successfully from an Ansible perspective, but do not do what they are supposed to do.

You should try to fix each one of these playbooks on your own.

For reference, there is also a solutions directory where I have created a "fixed" version of each playbook. You can do a diff between the failing and fixed playbook to see the exact issue (but once again try to solve them yourself).

# How to diff exercise6a
$ diff exercise6a.yml solutions/exercise6a_fixed.yml 

7. Create a new directory for exercise7 and in this directory create the following sub-directories and files:

$ cat ./group_vars/arista/dns.yml
---
domain_name: bogus.com
dns_server1: 8.8.8.8
dns_server2: 8.8.4.4

$ cat ./group_vars/arista/ntp.yml
---
ntp_server1: 130.126.24.24
ntp_server2: 152.2.21.1

Also create the following playbook:

---
- name: Exercise7
  hosts: arista
  gather_facts: False
  tasks:
    - debug:
        var: ntp_server1

    - debug:
        var: domain_name

Verify your playbook executes properly and the two specified variables from group_vars are printed out to standard output.
 
a. Using 'ansible-vault encrypt', encrypt the two YAML files in group_vars. Verify the two files are in fact encrypted by looking at the files. Verify your playbook still executes properly when using the '--ask-vault-pass' command-line argument.
b. Create a file named ".my_vault" in the same directory as your playbook. Store your vault password in this file. Using this file and the "--vault-password-file .my_vault" command-line argument, verify your playbook still executes properly.
c. Use 'ansible-vault view' to view the dns.yml file. You should be able to see the clear-text contents of this file.
d. Configure the following in your ~/.ansible.cfg file:

vault_password_file = /path/to/.my_vault
After making this change, verify your playbook still executes properly, but without you needing to specify any additional command-line arguments.
e. Execute 'ansible-vault decrypt' to decrypt both the dns.yml and the ntp.yml files. Verify these files are now both clear-text YAML files.


Bonus Lesson 1. - NAPALM-Ansible

 - [ ] I.    NAPALM-Ansible Overview
 - [ ] II.   Installing NAPALM-Ansible
 - [ ] III.  napalm_get_facts (Part1)
 - [ ] IV.   napalm_get_facts (Part2)
 - [ ] V.    NAPALM getters on Multiple Platforms
 - [ ] VI.   napalm_ping
 - [ ] VII.  NAPALM Configuration Operations
 - [ ] VIII. NAPALM Merge
 - [ ] X.    NAPALM Replace (Part2)
 - [ ] XI.   NAPALM and Jinja2 (Part1)
 - [ ] XII.  NAPALM and Jinja2 (Part2)


Exercises:
----------

1. Use "napalm_get_facts" and the get_config() method (filter: config) to retrieve the running configuration from all of the devices in the lab environment. Save the running configurations using the following directory structure: 

./BUP/
|-- eos
|  |-- arista5.txt
|  |-- arista6.txt
|  |-- arista7.txt
|  |-- arista8.txt
|-- ios
|  |-- cisco1.txt
|  |-- cisco2.txt
|  |-- cisco5.txt
|  |-- cisco6.txt
|-- junos
|  |-- vmx1.txt
|  |-- vmx2.txt
|-- nxos
    |-- nxos1.txt
    |-- nxos2.txt

Your playbook should automatically create the "BUP" sub-directory and the "BUP/{{ ansible_network_os }}" sub-directory (if they do not exist). Use the Ansible "file" module to accomplish this.


2. Use napalm_get_facts and the "get_lldp_neighbors()" method (filter: lldp_neighbors) to retrieve the LLDP neighbors from all of the Arista and Cisco IOS/IOS-XE devices.

Reformat the retrieved data to print out the following table to standard output (in a somewhat readable way). Note, you might need to use the "stdout_callback = debug" to accomplish this (i.e. to make the output somewhat readable): 

********* LLDP table for (cisco6) ********
GigabitEthernet2: cisco5
GigabitEthernet3: cisco5
GigabitEthernet4: cisco5
GigabitEthernet5: cisco5
GigabitEthernet6: cisco5
GigabitEthernet7: cisco5

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The first entry should be the local interface and the second entry should be the remote peer that is visible via that interface. You should clearly indicate which device the LLDP data was retrieved from.

This exercise will likely require that you loop through the data and use string concatenation to generate one large string (per device). You will subsequently output this string to the screen.


3. Use Jinja2 templating to generate the following VLAN and interface configurations:

VLAN Config 

vlan 202
   name blue202
!
vlan 203
   name blue203
!
vlan 204
   name blue204
!
vlan 205
   name blue205
!
vlan 206
   name blue206
!
vlan 207
   name blue207

interface configuration 

interface Ethernet2
   switchport access vlan 202
!
interface Ethernet3
   switchport access vlan 203
!
interface Ethernet4
   switchport access vlan 204
!
interface Ethernet5
   switchport access vlan 205
!
interface Ethernet6
   switchport access vlan 206
!
interface Ethernet7
   switchport access vlan 207

All of the relevant VLAN IDs and VLAN names should be stored in group_vars. All of the interface to VLAN assignment should also be stored in group_vars (i.e. which interface is assigned to which VLAN).

Use napalm-ansible and the "napalm_install_config" module (merge-operation) to deploy this configuration to the "arista5" switch. Validate your configuration changes before committing them by generating and reviewing a "diff" file of the pending changes.

Do NOT change the Ethernet1 interface as this interface is needed for management access to the device.


4. Repeat the BGP configuration exercise from class7, exercise1 using napalm-ansible.

Your updated solution should use "napalm_install_config" to install the configuration changes (merge operation).

Additionally, use "napalm_get_facts" and the "get_bgp_neighbors()" method (filter: bgp_neighbors) to verify that the BGP peers reach an established state ("is_up" key in the NAPALM returned data). Additionally, verify each peer is receiving two prefixes.

You should use Ansible tags in your playbook to create three separate phases: build, deploy, and verify. The build phase should handle all of the configuration generation. The deploy phase should push the configuration to the devices. The verify phase should ensure the BGP relationship reaches the correct state.

Use the NAPALM "nxos_ssh" driver to accomplish this exercise (add the argument "dev_os: nxos_ssh" to the NAPALM tasks).


5. Repeat the VLAN and interface configuration specified in exercise3 except using full configuration replace.

In order to accomplish this, you should use Ansible to retrieve the running configuration from Arista5. You should use this running-configuration as the basis for your Jinja2 template. Your Jinja2 template should use "include" statements to bring in both the interface configuration and the VLAN configuration (from external templates).

Once again all of your new VLAN IDs and VLAN names should be stored in group_vars. Similarly, the interfaces to VLAN ID mappings should also be stored in group_vars.

Note, do NOT change the Ethernet1 interface as this interface is needed for management access to the device.

At the end of the templating process, you should be generating an entire configuration that you can deploy to Arista5.

Next, use "napalm_install_config (replace) to deploy this configuration to the device. Once again, verify your changes will work before you deploying them by generating a "diff" and reviewing it.

Your configuration changes should only modify the arista5 switch.

