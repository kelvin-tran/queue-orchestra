from os import environ
from typing import List

from google.cloud import pubsub_v1


class GooglePublisher(object):

    def __init__(self, topic_id: str):
        self.topic_id = topic_id
        self.publisher = pubsub_v1.PublisherClient()
        self.project_id = environ['GOOGLE_PROJECT_ID']

    def send_messages(
            self, topic_path: str, messages: List[str],
            origin: str = None, author: str = None
    ) -> List[str]:
        """
        Publishes multiple messages to a Pub/Sub topic.
        :param topic_path: path of the topic to publish message
        :param messages: list of str messages to post to the topic
        :param origin: origin string to identify origin of sender
        :param author: author name to identify author
        """
        message_ids = []
        for message in messages:
            data = message.encode('utf-8')
            future = self.publisher.publish(
                topic_path, data=data, origin=origin, username=author
            )
            message_ids.append(future.result())
        return message_ids
