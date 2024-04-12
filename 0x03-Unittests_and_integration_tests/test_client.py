#!/usr/bin/env python3
"""Module that performs some Unit Testing"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize and patch as decorators"""
    @parameterized.expand([('google'), ('abc')])
    @patch('requests.get')
    def test_org(self, org_name: str, mock_request: Mock) -> None:
        """test GithubOrgClient.org method from client module"""
        client = GithubOrgClient(org_name)
        org_url = client.ORG_URL.format(org=org_name)
        result = client.org()
        mock_request.assert_called_once_with(org_url)


if __name__ == '__main__':
    unittest.main()
