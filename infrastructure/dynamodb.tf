resource "aws_dynamodb_table" "commission-matrices" {
  name         = "comission-matrices"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "market"
  range_key    = "year"

  attribute {
    name = "year"
    type = "S"
  }

  attribute {
    name = "market"
    type = "S"
  }

  tags = {
    Environment = "dev"
  }
}

resource "aws_dynamodb_table" "volume-targets" {
  name         = "volume-targets"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "agent"
  range_key    = "year_month"

  attribute {
    name = "agent"
    type = "S"
  }

  attribute {
    name = "year_month"
    type = "S"
  }

  tags = {
    Environment = "dev"
  }
}