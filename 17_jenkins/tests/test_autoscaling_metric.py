import unittest2 as unittest
from unittest.mock import Mock
from utils import calc_backlog_per_instance


class TestBacklogPerInstanceMetric(unittest.TestCase):
    def setUp(self):
        self.sqs_queue_client = Mock()
        self.asg_client = Mock()

    def test_no_worker_full_queue(self):
        self.sqs_queue_client.attributes = {
            'ApproximateNumberOfMessages': '100'
        }

        self.asg_client.describe_auto_scaling_groups = Mock(return_value={
            'AutoScalingGroups': [{
                'DesiredCapacity': 0
            }]
        })

        self.assertEqual(calc_backlog_per_instance(self.sqs_queue_client, self.asg_client, None), 99)
