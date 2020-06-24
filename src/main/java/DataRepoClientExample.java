import bio.terra.datarepo.api.ResourcesApi;
import bio.terra.datarepo.client.ApiClient;
import bio.terra.datarepo.client.ApiException;
import bio.terra.datarepo.client.Configuration;
import bio.terra.datarepo.model.EnumerateBillingProfileModel;

public class DataRepoClientExample {

    public static void main(String[] args) throws ApiException {
        ApiClient apiClient = Configuration.getDefaultApiClient();
        apiClient.setBasePath("https://jade.datarepo-dev.broadinstitute.org");

        // TODO: replace with a token generated from service account JSON
        apiClient.setAccessToken("ya29.fakeTOKEN");

        ResourcesApi api = new ResourcesApi(apiClient);

        try {
            EnumerateBillingProfileModel enumeratedProfiles = api.enumerateProfiles(0, 10);

            System.out.println("How many profiles total? " + enumeratedProfiles.getTotal());

            enumeratedProfiles.getItems().forEach(profile -> {
                System.out.println(profile.toString());
            });
        } catch (ApiException ex) {
            System.out.println("oh no! hope this wasn't a demo... profile enumeration failed: " + ex.getMessage());
            throw ex;
        }
    }
}
