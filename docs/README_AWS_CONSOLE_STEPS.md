### Steps: AWS Secrets Manager

1. Login `AWS Console`
2. Go to `AWS Secrets Manager`
3. Navigate to `Secrets` Step 1
4. Secret Type: `Other type of secret`
5. Add key/value pairs:
    * `key`:KAFKA_SASL_USERNAME, `value`: [ConfluentCloudKey]
    * `key`:KAFKA_SASL_PASSWORD, `value`: [ConfluentCloudSecret]
    * `key`:KAFKA_BOOTSTRAP_SERVER, `value`: [ConfluentCloudClusterBootstrapServerEndpoint]
    * `key`:ELASTICSEARCH_URL, `value`: [ElasticSearchCloudURL]
    * `key`:ELASTICSEARCH_API_KEY, `value`: [ElasticSearchCloudAPIKEY]
6. Encryption Key: `aws/secretsmanager`
7. Press `Next`
8. Secret name: `MWAA_Secrets`
9. Description: `This contains keys to Kafka Cluster and ElasticSearch`
10. Add Tags:
    * `Youtube`
    * `Production`
11. Press `Next`
12. Press `Next`
13. Press `Store`
