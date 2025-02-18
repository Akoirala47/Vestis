import os

# Create processed directory if it doesn't exist
os.makedirs('processed', exist_ok=True)

# Initialize version control for cluster labels (adjust paths as needed)
import subprocess
git_cmd = ['git', '--create-filter=ini', '-c', 'user.name=< clusternumbers >']
subprocess.run(git_cmd, text=True)