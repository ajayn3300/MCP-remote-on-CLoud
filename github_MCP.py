import os
from github import Github, Auth
from dotenv import load_dotenv
load_dotenv()
from fastmcp import FastMCP

#intialize server
mcp = FastMCP('GITHUB')

@mcp.tool()
def get_git_repo(repo_link :str) ->dict:

    '''this function takes github repository link as an argument and return all the python releated content with their file names as a dictionery'''
    link = repo_link.replace("https://github.com/",'')

    # Retrieve the token
    token = os.getenv("GITHUB_API_KEY")

    #gitub
    git = Github(auth = Auth.Token(token))

    #getting repo
    repo = git.get_repo(link)

    # extracting only code content
    contents = [i for i in repo.get_contents('') if i.name.endswith(('py','ipynb'))]

    data = {file.name:file.decoded_content.decode("utf-8") for file in contents}
    return data


@mcp.tool()
def list_user_repositories() -> list[str]:
    '''This function returns a list of all repository paths in the format owner/repo-name for the authenticated GitHub user.'''
    # Retrieve the token
    token = os.getenv("GITHUB_API_KEY")

    # GitHub instance
    git = Github(auth=Auth.Token(token))

    # Get the authenticated user and their repositories
    user = git.get_user()
    
    # repo.full_name automatically returns strings like 'ajayn3300/name-of-gitRepo'
    repo_paths = [repo.full_name for repo in user.get_repos()]
    
    return repo_paths



if __name__ == "__main__":
    # Runs the server using standard input/output (stdio)
    # mcp.run(transport="stdio")  #for local
    mcp.run(transport="streamable-http") # remote


