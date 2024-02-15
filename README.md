## What is it?
A simple example of how to create a slack bot using [slack_bolt](https://slack.dev/bolt-python/tutorial/getting-started)

## How to run
### Install python
Make sure you have [python 3.10](https://www.python.org/downloads/) or later installed.

### Ways of running the app

#### The easy way
Run the following command in the terminal to automatically set up a [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/), 
install the dependencies and run the program.
```bash 
./run --app-token [SLACK_APP_TOKEN] --bot-token [SLACK_BOT_TOKEN]
```
The first run will take slightly longer as it will install the dependencies.

#### The slightly less easy way
1. Create a [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
```bash
python3 -m venv .pyenv
```

2. Activate the venv 
```bash
source .pyenv/bin/activate
```

3. Install the dependencies
```bash
pip install -e ./src
```

4. Run the program
```bash
runbot --app-token [SLACK_APP_TOKEN] --bot-token [SLACK_BOT_TOKEN]
```
