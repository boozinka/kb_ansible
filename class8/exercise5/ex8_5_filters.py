---
- name: Exercise 8.5 - Use Ansible Filters
  hosts: nxos 
  gather_facts: False
  vars:
    command: show vlan
  tasks:

    - name: Configure VLANs on 'nxos1'
      cisco.nxos.nxos_vlans: 
        config: 
          - vlan_id: 100
            name: blue100
          - vlan_id: 101
            name: blue101
        state: merged
      when: inventory_hostname == "nxos1"
      tags: config

    - name: Configure VLANs on 'nxos2'
      cisco.nxos.nxos_vlans: 
        config: 
          - vlan_id: 200
            name: blue200
          - vlan_id: 201
            name: blue201
        state: merged
      when: inventory_hostname == "nxos2"
      tags: config

    - name: Gather 'show vlan' information using '| json' from Nexus switches
      cisco.nxos.nxos_command:
        commands: "{{ command }} | json"
      register: json_output
      tags: show

    - name: Create new varible, stripping away unwanted information
      ansible.builtin.set_fact:
        vlan_dict: "{{ json_output.stdout[0].TABLE_vlanbrief.ROW_vlanbrief }}"
      tags: show

    - name: Use 'map' to create list of 'vlan_ids'
      ansible.builtin.set_fact:
        vlan_list: "{{ vlan_dict | map(attribute='vlanshowbr-vlanid') | list }}"
      tags: show

    - name: Print 'vlan_list' to stdout
      ansible.builtin.debug:
        var: vlan_list
      tags: show 

    - name: Print VLANs in common using Intersection filter
      ansible.builtin.debug:
        msg: "{{ vlan_list | intersect(hostvars['nxos2']['vlan_list']) }}"
      when: inventory_hostname == "nxos1"
      tags: show

    - name: Print VLANs in unique to 'nxos1' using Difference filter
      ansible.builtin.debug:
        msg: "{{ vlan_list | difference(hostvars['nxos2']['vlan_list']) }}"
      when: inventory_hostname == "nxos1"
      tags: show

    - name: Print VLANs in unique to 'nxos2' using Difference filter
      ansible.builtin.debug:
        msg: "{{ vlan_list | difference(hostvars['nxos1']['vlan_list']) }}"
      when: inventory_hostname == "nxos2"
      tags: show


