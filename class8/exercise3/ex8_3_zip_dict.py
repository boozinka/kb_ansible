---
- name: Exercise 8.3 - Use "zip" to cast mac-addr-table output as a dictionary
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

    - name: Use 'map' to create equal length lists of 'mac_addr' and 'intf'
      ansible.builtin.set_fact:
        mac_addr: "{{ mac_table | map(attribute='macAddress') | list }}"
        intf: "{{ mac_table | map(attribute='interface') | list }}"

    - name: Create a list of lists with 'mac_addr' and 'intf'
      ansible.builtin.set_fact:
        mac_list: "{{ mac_addr | zip(intf) | list }}"

    - name: Cast list of lists as dictionary with 'mac_addr' as the key & 'intf' as the value
      ansible.builtin.set_fact:
        mac_dict: "{{ dict(mac_list) }}"

    - name: Print the new dictonary structure
      ansible.builtin.debug:
        var: mac_dict


