#!/usr/bin/env python3
"""Module that performs some Unit Testing"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import (
        patch,
        Mock,
        PropertyMock,
        MagicMock
    )
from typing import Dict
from fixtures import TEST_PAYLOAD


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

    def test_public_repos_url(self) -> None:
        """unit-test GithubOrgClient._public_repos_url from client module"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/amazon/repos",
            }
            self.assertEqual(
                GithubOrgClient("amazon")._public_repos_url,
                "https://api.github.com/users/amazon/repos",
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """tests GithubOrgClient.public_repos"""
        test_payload = {
            'repos_url': "https://api.github.com/orgs/amazon",
            'repos': [
                {'id': 1, 'name': 'alx-python'},
                {'id': 2, 'name': 'interview-prep'}
            ]
        }
        mock_get_json.return_value = test_payload.get('repos')

        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock
                ) as mock_pub_repo:
            mock_pub_repo.return_value = test_payload.get('repos_url')
            client = GithubOrgClient('amazon')
            self.assertEqual(
                client.public_repos(),
                ['alx-python', 'interview-prep']
            )
            mock_pub_repo.assert_called_once()

        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Tests the `has_license` method."""
        client = GithubOrgClient("amazon")
        client_has_licence = client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)

    # @patch('client.get_json')
    # def test_public_repos_with_license(
    #         self,
    #         license: str,
    #         mock_get_json: MagicMock
    #         ) -> None:
    #     """tests GithubOrgClient.public_repos with license arg"""
    #     test_payload = TEST_PAYLOAD
    #     mock_get_json.return_value = test_payload.get('repos')
    
    #     with patch(
    #             'client.GithubOrgClient._public_repos_url',
    #             new_callable=PropertyMock
    #             ) as mock_pub_repo:
    #         mock_pub_repo.return_value = test_payload.get('repos_url')
    #         client = GithubOrgClient('amazon')
    #         self.assertEqual(
    #             client.public_repos(license),
    #             ["dagger", "kratu", "traceur-compiler", "firmata.py"]
    #         )
    #         mock_pub_repo.assert_called_once()
    
    #     mock_get_json.assert_called_once()
    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            ["dagger", "kratu", "traceur-compiler", "firmata.py"]
        )


if __name__ == '__main__':
    unittest.main()
