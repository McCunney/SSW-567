import unittest
from unittest.mock import patch
from HW4a import get_repo_commit_count  

class TestGitHubAPI(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_repo_commit_count(self, mock_get):
        mock_repos_response = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]
        
        mock_commits_response = [
            {"sha": "1"},
            {"sha": "2"}
        ]
        
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: mock_repos_response),
            unittest.mock.Mock(status_code=200, json=lambda: mock_commits_response),
            unittest.mock.Mock(status_code=200, json=lambda: mock_commits_response)
        ]
        
        result = get_repo_commit_count('McCunney')
        
        self.assertEqual(result, [
            "Repo: Repo1 Number of commits: 2",
            "Repo: Repo2 Number of commits: 2"
        ])
        
    @patch('requests.get')
    def test_get_repo_commit_count_error(self, mock_get):
        mock_repos_response = []
        
        mock_commits_response = []
        
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: mock_repos_response),
            unittest.mock.Mock(status_code=404, json=lambda: mock_commits_response),  # Commits for Repo1
            unittest.mock.Mock(status_code=404, json=lambda: mock_commits_response)   # Commits for Repo2
        ]
        
        result = get_repo_commit_count('InvalidUser')
        
        self.assertEqual(result, [])
        

if __name__ == '__main__':
    unittest.main()

