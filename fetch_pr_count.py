import requests

def get_open_pr_count(owner, repo):
    # GitHub API URL for open pull requests
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open"
    
    # Optional: Add authentication header if needed
    headers = {
        'Authorization': 'token ${{ secrets.YOUR_PERSONAL_ACCESS_TOKEN}}'
    }
    
    # Send the request to GitHub
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # If successful, the API will return a JSON list of open PRs
        open_prs = response.json()
        return len(open_prs)  # Return the number of open PRs
    else:
        print(f"Error fetching data: {response.status_code}")
        return 0  # If error, return 0

# Example usage:
owner = "emmaxyz90"
repo = "aws_static_website_deployment"
open_pr_count = get_open_pr_count(owner, repo)
print(f"Open PRs: {open_pr_count}")
