## [Git & GitHub](https://www.youtube.com/watch?v=SWYqp7iY_Tc&t=1s)

### What is Git?

- A Version Control System (VCS) for tracking changes in computer files.
- A distributed/decentralized version control system.
    - Many developers can work on the same project without being in the same network.
- It coordinates wor between developers.
- It has info about who made what changes and when.
- We can revert back a specific version of any file at any time.
- We can work on Git repository _locally_ without internet.
- We can also upload this repo _remotely_ to internet using tools like _GitHub_.

### Concepts of Git

- Keeps track of code history.
- Takes _snapshots_ of our files.
- We decide when to take a snapshot by making a **commit**.
- We can visit any snapshot at any time.
- We can stage files before committing using **add** command.

### Basic Commands

- `git init`: initialize local git repo.
- `git add <file>`: add file(s) to index/the staging area.
- `git rm --cached <file>`: unstage file(s).
- `git status`: check status of working tree.
- `git commit`: commit changes in index.
    - `-m "message"`
- `git push`: push to remote repo.
- `git pull`: pull lates from remote repo.
- `git clone <repo>`: clone repo into a new directory.
- `git branch <name>`
- `git checkout <branch_name>`: move to another branch.
- `git merge <branch_name>`
- `git remote add origin <repo>`
- `git remote`
- `git push -u origin main`

## [GitHub](https://github.com/skills/introduction-to-github)
