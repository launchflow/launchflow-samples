import launchflow as lf

# Docs: https://docs.launchflow.com/reference/gcp-resources/cloud-sql
postgres = lf.aws.RDSPostgres("example-db")
