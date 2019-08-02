from os import environ
from typing import Iterable

from google.cloud import pubsub_v1


class PubSubTopic(object):

    def __init__(self, topic_id: str):
        self.topic_id = topic_id
        self.client = pubsub_v1.SubscriberClient()
        self.project_id = environ['GOOGLE_PROJECT_ID']

    def get_topic(self) -> str:
        return self.client.topic_path(self.project_id, self.topic_id)

    def list_topics(self) -> Iterable:
        """
        Lists all Pub/Sub topics in the given project.
        """
        publisher = pubsub_v1.PublisherClient()
        project_path = publisher.project_path(self.project_id)
        return publisher.list_topics(project_path)
