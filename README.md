# genai-webapp-python

This template is designed to be a starting point for a Generative AI Python web development environment that includes both a Python FastAPI backend with LangServe/LangChain set up, and a Python Streamlit frontend.

The reasoning for separating the frontend and the backend is to make things modular. For example, let's say you wanted to make a production version of a prototype and wanted to keep your LangServe backend, but want to make a more powerful React frontend. You can simply replace the frontend container with a React environment, but keep the same REST FastAPI on the backend.

Poetry is used as the python build framework. The frontend and backend code will each run in their own Docker Container. 

> ⚠️ **WARNING**: This framework is designed with rapid prototyping as the main goal. While Streamlit and LangChain are great for this purpose, they are not necessarily designed for production applications, even though they can be deployed in production and work fine. Keep maintainability and scale in mind as your project moves forward, and make sure you understand the limitations of each technology and how they work!

# Local Development

This application's deployment and development environment is designed for local development with Visual Studio Code. While other IDEs that support DevContainer functionality may work, they are not tested.

## Getting Started

`docker-compose.yml` defines the local containers. You can update any aspect of the local containers here, for example, changing the ports that the frontend and backend run on locally, changing the command to start the services or adding environment variables.

### Credentials

In order for the two example chatbots in this template application to work, you must set up the proper AWS and Azure credentials, as outlined below. You don't have to set up both, but there will be errors in the application if you try to visit their respective pages without configuring them.

### AWS

By default, docker-compose passes your `$HOME/.aws` directory into each container's user home, so it will have access to your local AWS configured profiles. It expects you to have an AWS CLI profile named `genai` configured with access to an AWS account with permission to run the Bedrock Invoke APIs.

The default application uses the `anthropic.claude-v2` and `meta.llama2-70b-chat-v1` Bedrock models. It expects that the EULAs for these models have been accepted in the Bedrock console in order to use them.

## Azure OpenAI

By default, docker-compose passes the Environment Variables `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT` from your local environment into the backend container's user environment. It expects you to have these configured in your local shell running in VS Code. To set up an Azure OpenAI Endpoint to populate these variables, refer to the Azure documentation. 

The default application expects your Azure OpenAI Endpoint to have two deployments, one with the name `gpt-4` and another named `gpt-35-turbo`. 

## Containers

There are three containers that will run for local development. Each are configured with a `Dockerfile` and `pyproject.toml` in their respective directories, described below.

### .devcontainer

This directory defines the container that VS Code / DevContainer will install extensions to and execute within your workspace. You can add dependencies here that are for your local development convenience such as linters, debuggers or any other tools you want available for development. You can update `.devcontainer/devcontainer.json` to add additional VS Code extensions.

The entire repository will be mounted at `/workspace` in the running container.

### backend

This directory defines the container that LangServe / LangChain will run in. Its default configuration is to run on port `8100`. Add dependencies here that you want the frontend to have. The `Dockerfile` defines both a `development` and `production` target, and docker-compose is set to run the `development` target locally. This means you can define development-only dependencies in `pyproject.toml`, if desired.

The `backend` directory will be mounted into its respective container at `/code` in the running container. By default, the command supplied will direct the uvicorn server that runs the FastAPI application to monitor for and automatically reload any code changes in real time.

### frontend

This directory defines the container that Streamlit will run in. Its default configuration is to run on port `8101`. Add dependencies here that you want the frontend to have. The `Dockerfile` defines both a `development` and `production` target, and docker-compose is set to run the `development` target locally. This means you can define development-only dependencies in `pyproject.toml`, if desired.

The `frontend` directory will be mounted into its respective container at `/code` in the running container. By default, the command supplied will direct the streamlit server to monitor for and automatically reload any code changes in real time.

## VS Code Setup

1. **Prerequisites**: Ensure Docker Desktop is installed and Docker Engine is running on your machine. Ensure DevContainer extension is installed in VS Code.
2. **Setup**: Clone this repository and open it in a new Visual Studio Code workspace
3. **DevContainer**: Upon opening the workspace, you should be prompted to reopen it in a container. If not, you can manually initiate the DevContainer build process.

## Usage

After the DevContainer build process is complete, you will have a fully configured development environment with both the frontend and backend containers running on their respective ports at `http://localhost`.

You could also choose to add more container services to `docker-compose.yaml`. For example, to run MySQL or AWS DynamoDB locally as well, as your application requires.
