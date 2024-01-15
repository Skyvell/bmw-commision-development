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
    ],
  })
}

resource "aws_lambda_function" "parser_lambda" {
  function_name = "parser_lambda"
  role          = aws_iam_role.parser_lambda_role.arn
  handler       = "handler.lambda_handler"
  runtime       = "python3.11"
  filename      = "../dist/parser_lambda.zip"
  source_code_hash = filebase64sha256("../dist/parser_lambda.zip")

  layers = [aws_lambda_layer_version.pandas_layer.arn]
}