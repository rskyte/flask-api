import os
import sys
import pytest
import unittest
sys.path.append("./")
sys.path.append(os.getcwd() + "/src")

from unittest.mock import Mock
from unittest.mock import MagicMock
from types import SimpleNamespace
from s3_logic import S3Logic

class S3LogicTest(unittest.TestCase):
    def setUp(self):
        self.client = Mock()
        self.client.put_object = MagicMock(return_value={'ResponseMetadata': {'HTTPStatusCode': 200}})
        
        mock_dictionary = {'key': 'test'}
        mock_namespace = SimpleNamespace(**mock_dictionary)
        self.bucket = Mock()
        self.bucket.key = MagicMock(return_value=mock_namespace)
        self.bucket.objects.all = MagicMock(return_value=mock_dictionary)
        self.s3_logic = S3Logic(self.client, self.bucket)
    
    def test_successful_data_input_returns_200_status_code(self):
        value = self.s3_logic.put({'userId': 'jsmith', 'name': 'John Smith'})
        self.assertEqual(value, 200, 'incorrect status code returned')

    #def test_unsuccessful_data_input_returns_400_status_code(self):

    def test_can_read_list_of_all_user_ids_from_bucket(self):
        value = self.s3_logic.get_all_user_ids()
        self.assertEqual(value[0], 'test', 'incorrect user id list')

    def test_empty_list_returned_when_no_users_in_bucket(self):
        self.bucket.objects.all = MagicMock(return_value=[])
        value = self.s3_logic.get_all_user_ids()
        self.assertEqual(value, [], 'incorrect user id list')