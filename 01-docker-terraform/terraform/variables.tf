variable "credentials" {
  description = "My Credentials"
  default     = "PATH_TO_CREDENTIALS_FILE"
}

variable "project" {
  description = "Project"
  default     = "PROJECT_ID"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "BQ_DATASET_NAME"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "BUCKET_NAME"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}