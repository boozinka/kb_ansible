---
- name: Exercise 8.2 - Use "lookup" to set the "ansible_ssh_pass" from the environment varible
  hosts: arista 
  gather_facts: False
  vars:
    ansible_ssh_pass: "{{ lookup('env', 'ANSIBLE_PASSWORD') }}"
    command: show vlan 
  tasks:
    - name: Retrieve results from 'show vlan' command
      arista.eos.eos_command:
        commands: "{{ command }}"
      register: output

    - name: Print output of the "show vlan" command
      ansible.builtin.debug:
        var: output.stdout_lines[0]

