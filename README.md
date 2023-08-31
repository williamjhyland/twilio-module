# twilio-module
This example shows you you can configure a generic component as a module in Viam.

This is a limited document for more details reach out to the Viam team or reference the documentation.

# Project Structure
The definition of the new resources are in the main file of the src directory.

The exec.sh script is the entrypoint for a module and calls the main.py file. The main.py file contains the definition of a new sensor model and code to register it.

# Configuring and using the module
Twilio module for alerting based on a do_command(). Intended to be implemented as a Viam module. Requires the following in the config:
    ['auth_token']
    ['account_sid']
    ['recipient_phone']
    ['deliverer_phone']
