### Managed Apache Airflow

1. Press `Create environment`
2. Set `Name` : `NWAA-Youtube-production`
3. Press `Browse S3`
    * Search `dml-youtube-prod` and Select it
4. Verify `S3 Bucket` value `s3://dml-youtube-prod`
5. Set `DAGs folder` value `s3://dml-youtube-prod/project1/dags/`
6. Set `Requriements file` value `s3://dml-youtube-prod/project1/requirements.txt`
7. Press `Next`
8. Click `Create new VPC`
    * Set `Stack name` value `MWAA-VPC-production`
    * Parameters -> Set `EnvironmentName` value `MWAA-Youtube-Prod`
    * Select IAM role -> Select your Role (If you have)
    * Press `Create stack`
9. Back to Configure environment Tab and refresh the list of `Choose VPC`
10. Select the new VPC `MWAA-VPC-production`
11. Select the Subnet you want
12. In our case `Web server  access` select `Public network (Internet accessible)`
13. Choose the desired `Security group` or `Create new security group`
14. Select `Environment class`
15. Set `Monitoring`:
    * Enable `Airflow task logs`
    * Enable `Airflow eb server logs`
    * Enable `Airflow scheduler logs`
    * Enable `Airflow worker logs`
    * Enable `Airflow DAG processing logs`
16. Add `Airflow configuration options` you need
17. Add `Tags` values:
    * `Key`: `production` and `Value`: `true`
18. Permissions: `Create a new role` or Existing role.
19. Press `Create`