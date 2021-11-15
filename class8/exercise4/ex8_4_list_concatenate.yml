---
- name: Exercise 8.4 - Create a list of all mac-addresses using list concatenate.
  hosts: arista 
  gather_facts: False
  vars:
    command: show mac address-table
  tasks:
    - name: Retrieve results from 'show mac address-table' command
      arista.eos.eos_command:
        commands: "{{ command }} | json"
      register: output

    - name: Strip off unwanted data and register mac details against varible
      ansible.builtin.set_fact:
        mac_table: "{{ output.stdout[0]['unicastTable']['tableEntries'] }}"

    - name: Use list concatenation and loop to create a list of all mac-addresses
      ansible.builtin.set_fact:
        mac_list: "{{ mac_list | default([]) + [item['macAddress']] }}"
      loop: "{{ mac_table }}"

    - name: Print the new list structure
      ansible.builtin.debug:
        var: mac_list


