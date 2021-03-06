#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


# Check if the netmiko library is installed or not
netmiko_found = False
try:
    from netmiko import ConnectHandler
    netmiko_found = True
except ImportError:
    pass


def main():

    # Define your module arguments
    module_args = dict(
        host=dict(type='str', required=True),
        device_type=dict(type='str', required=True),
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
        config_list=dict(type='list', required=True),
    )

    # Create an instance of the AnsibleModule class
    module = AnsibleModule(argument_spec=module_args)

    # Define standard results
    result = dict(changed=False, msg='')

    # DO STUFF HERE ONWARDS

    # Ensure netmiko is installed' exit using JSON if not.
    if not netmiko_found:
        module.fail_json(msg='The Netmiko library is not installed!')

    # Extract the arguments that were entered
    host = module.params['host']
    device_type = module.params['device_type']
    username = module.params['username']
    password = module.params['password']
    config_list = module.params['config_list']

    # If no configuration changes, then just return
    if not config_list:
        module.exit_json(**result)

    net_connect = ConnectHandler(
        host=host, device_type=device_type, username=username, 
        password=password)

    output = net_connect.send_config_set(config_list)
    result['output'] = output

    # Return items as JSON
    module.exit_json(**result)


if __name__ == "__main__":
    main()

