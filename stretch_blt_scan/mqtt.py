from paho.mqtt import client as mqtt
import logging
logger = logging.getLogger(__name__)


def on_publish(client, user_data, msg_id):
    """
    on_publish call to track if msg has been published.
    :param client: client instance for callback
    :type client: mqtt_client
    :param user_data: the private user data as set in Client() or userdata_set()
    :type user_data: user_data
    :param msg_id: message id corresponding to publish call
    :type msg_id: int
    :return: None
    :rtype: None
    """
    logger.info("Message with msg id {} successfully published.".format(msg_id))


def connect(mqtt_conf):
    """
    Connects to an mqtt broker.
    :param mqtt_conf - dict configuration containing, username, password,
    host, port
    :type dict
    :return: mqtt client to publish and subscribe to messages
    :rtype: paho.mqtt.client.Client()
    """
    logger.info("Creating MQTT client.")
    client = mqtt.Client()
    client.on_publish = on_publish

    username = mqtt_conf.get('USERNAME', '')
    password = mqtt_conf.get('PASSWORD', '')

    client.username_pw_set(username, password)
    logger.info("Connecting to MQTT server")

    host = mqtt_conf.get('HOST', 'localhost')
    port = mqtt_conf.get('PORT', 1883)
    client.connect(host, port)
    return client
