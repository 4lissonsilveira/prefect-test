from flow import flow_sync_case_object

# TODO: create an image of docker just to be used just for de deployments
# and create another one that will be used buy the prefect-deployer container.
if __name__ == "__main__":
    flow_sync_case_object.deploy(
        name="my-deployment-1",
        work_pool_name="my-docker-pool",
        image="flow_sync_case_object",
        push=False, # switch to True to push to your image registry,
        job_variables={
            "env":{
                "PREFECT_API_URL": "http://localhost:4200/api",
                "EXTRA_PIP_PACKAGES": "simple_salesforce",
                "PYTHONPATH": "/opt/prefect/flows"
            }
        }
    )
