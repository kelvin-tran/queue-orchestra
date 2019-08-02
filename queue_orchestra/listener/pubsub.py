import time
from os import environ
from typing import Callable

from google.cloud import pubsub_v1


class GoogleListener(object):

    def __init__(self, subscription_name: str):
        self.subscriber = pubsub_v1.SubscriberClient()
        self.project_id = environ['GOOGLE_PROJECT_ID']
        self.subscription_name = subscription_name

    def listen_for_messages(
            self, process_callback: Callable,
            n_messages: int = 1,
    ):
        """
        Publishes multiple messages to a Pub/Sub topic.
        :param n_messages: the number of messages to send to callback at a time
        :param process_callback: the function to call with the method to do
         something with the message (eg, process its contents)
        """

        def process(message):
            processed = process_callback(message)
            if processed:
                message.ack()
            else:
                message.nack()

        # The `subscription_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/subscriptions/{subscription_name}`
        subscription_path = self.subscriber.subscription_path(
            self.project_id, self.subscription_name
        )
        flow_control = pubsub_v1.types.FlowControl(max_messages=n_messages)
        self.subscriber.subscribe(
            subscription_path, callback=process, flow_control=flow_control
        )

        # The subscriber is non-blocking. We must keep the main thread from
        # exiting to allow it to process messages asynchronously in the background.
        while True:
            time.sleep(60)
