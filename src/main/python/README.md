# Using the Data Repo client locally in Jupyter

These instructions are designed to work with Docker and Visual Studio Code
(VSCode). When using VSCode, ensure you have the official Jupyter and Python
extensions installed from Microsoft.

## Instructions

1. Download and run the Jupyter minimal notebook Docker image

```
docker pull jupyter/minimal-notebook
docker run --rm -p 8888:8888 --name jupyter jupyter/minimal-notebook
```

2. In the logs, you will see a section similar to the one below, copy the URL
starting with `http://127.0.0.1:8888` to the clipboard

```
[C 20:53:41.359 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-8-open.html
    Or copy and paste one of these URLs:
        http://2512f4e1ef18:8888/?token=c9ced3dc0e04a74bca8c9802cbfec510777b68e7c52cafb0
     or http://127.0.0.1:8888/?token=c9ced3dc0e04a74bca8c9802cbfec510777b68e7c52cafb0
```

3. Install the latest `data-repo-client` inside the Jupyter image as follows:

```
docker exec -it jupyter /bin/sh 
pip install data-repo-client
```

4. Start up VSCode, then select `View -> Command Palette -> Jupyter: Create New Blank Jupyter Notebook`
(or open an already existing notebook)

5. In the Jupyter menubar, select `Jupyter Server -> Existing`, paste the URL
from step 2 in the input box, and press `Enter` to confirm your input. You
should see a green lock icon next to the URL if this process is successful.

6. You should be able to `import data_repo_client` in the notebook to start
interacting with the client! This notebook can then be used on Terra.
