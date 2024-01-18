resource "aws_iam_role" "parser_lambda_role" {
  name = "parser_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
      },
    ],
  })
}

resource "aws_iam_role_policy" "parser_lambda_policy" {
  role = aws_iam_role.parser_lambda_role.name

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
        ],
        Resource = "arn:aws:logs:*:*:*",
        Effect   = "Allow",
      },
      {
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
          "s3:ListBucket",
        ],
        Resource = [
          "${aws_s3_bucket.bmw_data_upload_bucket.arn}/*",
          aws_s3_bucket.bmw_data_upload_bucket.arn
        ],
        Effect = "Allow"
      },
      {
        Action = [
          "dynamodb:PutItem",
          "dynamodb:BatchWriteItem",
        ],
        Effect = "Allow",
        Resource = [
          aws_dynamodb_table.commission-matrices.arn,
          aws_dynamodb_table.volume-targets.arn
        ]
      },
    ],
  })
}

resource "aws_lambda_function" "parser_lambda" {
  function_name    = "parser_lambda"
  role             = aws_iam_role.parser_lambda_role.arn
  handler          = "handler.lambda_handler"
  runtime          = "python3.11"
  filename         = "../builds/lambdas/parser.zip"
  source_code_hash = filebase64sha256("../builds/lambdas/parser.zip")
  layers           = [aws_lambda_layer_version.pandas_layer.arn]
  timeout          = 30

  environment {
    variables = {
      DYNAMODB_TABLE_NAME_COMMISSION_MATRICES = aws_dynamodb_table.commission-matrices.name
      DYNAMODB_TABLE_NAME_VOLUME_TARGETS      = aws_dynamodb_table.volume-targets.name
    }
  }
}