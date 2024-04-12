#!/usr/bin/env python3
"""Module that performs some Unit Testing"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Dict


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

    @parameterized.expand([
            ('google', {"payload": True}),
            ('abc', {"payload": False})
        ])
    def test_public_repos_url(self, name, payload: Dict) -> None:
        """unit-test GithubOrgClient._public_repos_url from client module"""
        with patch.object(
                GithubOrgClient,
                'org',
                return_value=lambda: payload
                         ) as mock_org:
            client = GithubOrgClient(name)
            result = client._public_repos_url
            result.return_value = payload
            self.assertEqual(result(), payload)
            # mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()
