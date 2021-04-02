# jade-data-repo-client-example

An example project to demonstrate the capabilities of the data-repo client.

The newest data-repo client builds can be found on the [Broad Institute datarepo-client page](https://broadinstitute.jfrog.io/ui/packages/gav:%2F%2Fbio.terra:datarepo-client).

## Running

To run this, make sure `GOOGLE_APPLICATION_CREDENTIALS` is set and is pointing at a valid
credential JSON file.

```shell
GOOGLE_APPLICATION_CREDENTIALS=/tmp/jade-dev-account.json ./gradlew run
```