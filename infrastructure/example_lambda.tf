resource "aws_iam_role" "example_lambda_role" {
  name = "example_lambda_role"

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

resource "aws_iam_role_policy" "lambda_policy" {
  role = aws_iam_role.example_lambda_role.name

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

resource "aws_lambda_function" "example_lambda" {
  function_name = "ExampleLambdaTeddy"
  role          = aws_iam_role.example_lambda_role.arn
  handler       = "handler.lambda_handler"
  runtime       = "python3.11"
  filename      = "../dist/example_lambda/example_lambda.zip"
}