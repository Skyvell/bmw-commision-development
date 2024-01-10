provider "aws" {
  region  = "eu-north-1"
  profile = "ductus"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "ductus-test-buckett"
  tags = {
    Name        = "My Terraform Bucket"
    Environment = "Dev"
  }
}




