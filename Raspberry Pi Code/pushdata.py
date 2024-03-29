

from azure.iot.hub import IoTHubRegistryManager
import light_sensor



MESSAGE_COUNT =10


MSG_TXT = "{\"service client sent a message\": %.2f}"

CONNECTION_STRING = "HostName=test-iot-1.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=O/cOu9sw06JqfaC+Vanmlbd9e1x3/nd8SaltXk470mo="
DEVICE_ID = "pi"

def iothub_messaging_sample_run():
    try:
        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

        for i in range(0, MESSAGE_COUNT):
            input("Press Enter to continue...\n")
            print ( 'Sending message: {0}'.format(i) )
            data =light_sensor.data_collection()
            data = str(data)



            registry_manager.send_c2d_message(DEVICE_ID, data)

            # Use Python 3.xx in the case of exception


    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )

if __name__ == '__main__':
    print ( "Starting the Python IoT Hub C2D Messaging service sample..." )

    iothub_messaging_sample_run()
