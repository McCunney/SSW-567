import requests

def get_repo_commit_count(user_id):
    repos_url = f'https://api.github.com/users/{user_id}/repos'
    
    response = requests.get(repos_url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data for user: {user_id}")
        return []
    
    repos = response.json()
    
    result = []
    
    for repo in repos:
        repo_name = repo['name']
        commits_url = f'https://api.github.com/repos/{user_id}/{repo_name}/commits'
        
        commits_response = requests.get(commits_url)
        
        if commits_response.status_code != 200:
            print(f"Failed to retrieve commits for repository: {repo_name}")
            commit_count = 0
        else:
            commits = commits_response.json()
            commit_count = len(commits)
        
        result.append(f"Repo: {repo_name} Number of commits: {commit_count}")
    
    return result

if __name__ == "__main__":
    user_id = "McCunney" 
    result = get_repo_commit_count(user_id)
    
    for item in result:
        print(item)

