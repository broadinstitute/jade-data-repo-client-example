import json, uuid, time
from IPython.core.display import display, clear_output, HTML
from data_repo_client import ApiException, JobsApi

# Helper class with methods to make the Terra Data Repository easier to use via Python
class TdrUtils:

    def __init__(self, jobs_api):
        self.jobs_api = jobs_api

    # Format and print TDR objects
    def tdr_object_to_json(self, obj):
        if (hasattr(obj, "to_dict")):
            return json.dumps(obj.to_dict(), indent=4)
        else:
            return json.dumps(obj, indent=4)


    # Format TDR objects
    def pretty_print_tdr_object(self, obj):
        print(self.tdr_object_to_json(obj))

    # Wait for an monitoy the status of a job
    def wait_for_job(self, job_model):
        counter = 0
        max_dots = 8
        result = job_model
        job_str = '"%s" (%s)' % (job_model.description, job_model.id)
        while True:
            counter += 1
            clear_output(wait=True)
            if (result == None or result.job_status == "running"):
                num_dots = counter % max_dots
                dots = '.' * (num_dots)
                display(HTML('<b>Running job %s %s</b>' %(job_str, dots)))
                time.sleep(3)
                result = self.jobs_api.retrieve_job(job_model.id)
            elif (result.job_status == 'failed'):
                display(HTML('<b>Running job %s: <span style="color:rgb(219, 50, 20);">failed</span></b>' % job_str))
                try:
                    result = self.jobs_api.retrieve_job_result(job_model.id)
                except ApiException as e:
                    result = display(HTML('<p>Job result is:</p><pre>%s</pre>' % self.tdr_object_to_json(e)))
                return result
            elif (result.job_status == "succeeded"):
                display(HTML('<b>Running job %s: <span style="color:rgb(116, 174, 6);">succeeded</span></b>' % job_str))
                result = self.jobs_api.retrieve_job_result(job_model.id)
                display(HTML('<p>Job result is:</p><hr/><pre>%s</pre>' % self.tdr_object_to_json(result)))
                return result
            else:
                raise "Unrecognized job state %s" % result.job_status


    # Convert bytes representation of UUID into string representation
    def UUID(self, bytes):
        return str(uuid.UUID(bytes=bytes))