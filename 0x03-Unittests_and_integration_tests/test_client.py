#!/usr/bin/env python3
"""Testing client"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient class """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(
        self, org_name: str, mock_get_json: unittest.mock.MagicMock
    ) -> None:
        """ Test that GithubOrgClient.org """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"payload": True})
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
        )

    @patch("client.GithubOrgClient.org",
           new_callable=PropertyMock,
           return_value={"repos_url": "http://google.com"})
    def test_public_repos_url(self, mock_org: unittest.mock.MagicMock) -> None:
        """ Test that GithubOrgClient._public_repos_url """
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url,
                         mock_org.return_value["repos_url"])
