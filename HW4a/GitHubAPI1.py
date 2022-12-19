import requests

def get_repos_with_commits(github_id):
    # First, get a list of all the repositories for the given GitHub user
    repositories_url = f'https://api.github.com/users/{github_id}/repos'
    repositories_response = requests.get(repositories_url)
    repositories = repositories_response.json()
    
    # Initialize an empty list to store the repository information
    repos_with_commits = []
    
    # Iterate through each repository and get the commit information
    for repo in repositories:
        repo_name = repo['name']
        commits_url = f'https://api.github.com/repos/{github_id}/{repo_name}/commits'
        commits_response = requests.get(commits_url)
        commits = commits_response.json()
        
        # Add the repository name and commit information to the list
        repos_with_commits.append({'repo_name': repo_name, 'commits': commits})
    
    return repos_with_commits

# Example usage
github_id = 'cconway1-stevens'
repos_with_commits = get_repos_with_commits(github_id)
print(repos_with_commits)
