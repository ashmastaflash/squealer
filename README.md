# Squealer

# Make noise if critical vulnerabilities are found

Ok, here's the big idea:   You build and run this container, giving it a
CloudPassage Halo API key an agent ID, and an auth token for Github.  It runs
all available scans against your instance and if any critical issues are found,
it files an issue against the project in Github.

Here are the environment variables you need to define:

| What it is                  | What it does                                                                                        |
|-----------------------------|-----------------------------------------------------------------------------------------------------|
| HALO_API_KEY                | This is the API key for your Halo account.                                                          |
| HALO_API_SECRET_KEY         | This is the secret key for the Halo API.                                                            |
| HALO_API_HOSTNAME           | If in doubt, set this to ```api.cloudpassage.com```                                                 |
| HALO_API_PORT               | If in doubt, set this to ```443```                                                                  |
| HALO_AGENT_ID               | This is the agent ID.  This can be found in the running instance at /opt/cloudpassage/data/id       |
| SQUEAL                      | If critical results are found, exit with code 2 after filing an issue. Set to anything to activate. |
| COMMIT_ID                   | ID of commit being tested                                                                           |
| GITHUB_PROJECT              | Github project path.  For instance, ashmastaflash/squealer                                          |
| GITHUB_TOKEN                | Github auth token.  Must at least have repo access.                                                 |


```docker build -t squealer .```

       docker run -d \
       -e HALO_API_KEY=$HALO_API_KEY \
       -e HALO_API_SECRET=$HALO_API_SECRET \
       -e HALO_API_HOSTNAME=$HALO_API_HOSTNAME \
       -e HALO_API_PORT=$HALO_API_PORT \
       -e HALO_AGENT_ID=$HALO_AGENT_ID \
       -e COMMIT_ID=$COMMIT_ID \
       -e GITHUB_PROJECT=$GITHUB_PROJECT \
       -e GITHUB_TOKEN=$GITHUB_TOKEN \
       -e SQUEAL=True \
       squealer
