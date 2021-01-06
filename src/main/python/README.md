# Creating Python client and Dockerfile

Instructions for generating the python client and publishing to a docker image.

## Create Python client from OpenAPI specification

1. Pull the latest version from `jade-data-repo` and make note of the version number
2. Install version 4.3.1 of `open-generator-cli` from npm (version 5.0.0 causes issues)

```
npm install
npm install @openapitools/openapi-generator-cli -g
openapi-generator-cli version-manager set 4.3.1
```

3. Generate the Python client

```
cd jade-data-repo
openapi-generator-cli generate -i src/main/resources/api/data-repository-openapi.yaml -g python -o ../data-repo-client --package-name data_repo_client
```

## Create Python distribution archives for package

https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives

4. Navigate to newly created Python client

```
cd ../data-repo-client
```

5. Install packaging prerequisites including setuptools and wheel

```
python3 -m pip install --user --upgrade setuptools wheel
```

6. Update `setup.py` to latest version

7. Generate dist

```
python3 setup.py sdist bdist_wheel
```

8. Check out the `/dist` folder, should be two new files

## Upload package to pipy

https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

9. Get api token and set up your .pypirc file - instructions at link above

10. Install twine

```
python3 -m pip install --user --upgrade twine
```

11. Run twine to upload all archives under twiner

```
python3 -m twine upload --repository data_repo_client dist/*
```

12. Go to https://pypi.org/project/data-repo-client and see if new version has been successfully updates

## Create new docker image w/ latest version

13. Navigate to folder w/ dockerfile

14. Update dockerfile to specfify the latest version of the data_repo_client

15. Build docker image

```
docker build . --tag client-VERSIONNUM
```

## Publish the docker image to container registry

16. Tag the new docker image

```
docker tag client-VERSIONNUM:latest us.gcr.io/broad-jade-dev/jupyter-shelby-test
```

17. Push to container registry

```
docker push us.gcr.io/broad-jade-dev/jupyter-shelby-test
```

18. Go to gcloud console and to check for new image
