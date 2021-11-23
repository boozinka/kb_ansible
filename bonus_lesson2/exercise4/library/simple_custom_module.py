#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():

    # Define your module arguments
    module_args = dict(
        my_str=dict(type='str', required=True),
    )

    # Create an instance of the AnsibleModule class
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # Define standard results
    result = dict(changed=False)

    # Extract the argument that was entered
    my_string = module.params['my_str']

    # Convert string to upper case and assign to the results output
    result['output'] = my_string.upper()

    # Return items as JSON
    module.exit_json(**result)


if __name__ == "__main__":
    main()
 
