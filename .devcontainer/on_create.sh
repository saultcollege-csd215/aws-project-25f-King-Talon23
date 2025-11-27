# This script gets run as devcontainer post-create command

# Make sure AWS credentials file exists with correct permissions
mkdir -p .aws
touch .aws/credentials
chmod 600 .aws/credentials

# Setup Python virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r app/requirements_flask.txt