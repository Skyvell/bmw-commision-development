resource "aws_dynamodb_table" "commission-matrices" {
  name         = "comission-matrices"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "Market"
  range_key    = "Year"

  attribute {
    name = "Year"
    type = "N"
  }

  attribute {
    name = "Market"
    type = "S"
  }

  tags = {
    Environment = "dev"
  }
}

resource "aws_dynamodb_table" "volume-targets" {
  name         = "volume-targets"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "Agent"
  range_key    = "MonthYear"

  attribute {
    name = "Agent"
    type = "S"
  }

  attribute {
    name = "MonthYear"
    type = "S"
  }

  tags = {
    Environment = "dev"
  }
}