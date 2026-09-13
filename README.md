# MCP Remote on Cloud

A lightweight **GitHub MCP (Model Context Protocol) server** built with [FastMCP](https://gofastmcp.com/), exposing GitHub repository data as tools that any MCP-compatible client (like Claude) can call remotely over HTTP.

This server lets an AI assistant:
- List all repositories for an authenticated GitHub user.
- Fetch and read the Python/Jupyter Notebook source code from any public/private repo it has access to.

## ✨ Features

- **`list_user_repositories`** — Returns a list of all repositories (`owner/repo-name`) for the authenticated GitHub account.
- **`get_git_repo`** — Given a GitHub repo URL, fetches the root-level contents and returns all `.py` and `.ipynb` files as a `{filename: source_code}` dictionary.
- Runs as a **remote server** using the `streamable-http` transport, so it can be deployed to the cloud and accessed by MCP clients over a network (rather than only locally via stdio).

## 🛠️ Tech Stack

- [FastMCP](https://gofastmcp.com/) — framework for building MCP servers/clients
- [PyGithub](https://pygithub.readthedocs.io/) — GitHub REST API wrapper
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management

## 📂 Project Structure

```
MCP-remote-on-CLoud/
└── github_MCP.py   # Main MCP server exposing GitHub tools
```

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/ajayn3300/MCP-remote-on-CLoud.git
cd MCP-remote-on-CLoud
```

### 2. Install dependencies
```bash
pip install fastmcp PyGithub python-dotenv
```

### 3. Configure environment variables
Create a `.env` file in the project root and add your GitHub Personal Access Token:
```env
GITHUB_API_KEY=your_github_personal_access_token
```

> Your token needs at least `repo` scope to read private repositories, or no special scope for public-only access.

### 4. Run the server
```bash
python github_MCP.py
```

By default this starts the server using the **streamable-http** transport, making it accessible remotely (e.g. for cloud deployment) rather than only over local stdio.

## 🧰 Available Tools

| Tool | Description | Arguments | Returns |
|---|---|---|---|
| `list_user_repositories` | Lists all repos for the authenticated user | none | `list[str]` of `owner/repo-name` |
| `get_git_repo` | Fetches all `.py`/`.ipynb` files from a repo's root | `repo_link: str` (e.g. `https://github.com/owner/repo`) | `dict` of `{filename: file_content}` |


Once running, point any MCP-compatible client (e.g. Claude, or a custom FastMCP client) to the server's HTTP endpoint to start calling `list_user_repositories` and `get_git_repo` remotely.

## 📄 License

Add a license of your choice (e.g. MIT) here.
