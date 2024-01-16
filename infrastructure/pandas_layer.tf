resource "aws_lambda_layer_version" "pandas_layer" {
  filename   = "../builds/layers/pandas_layer.zip"
  layer_name = "pandas_layer"

  compatible_runtimes = ["python3.11"]
  description = "Pandas layer for Lambda."

  source_code_hash = filebase64sha256("../builds/layers/pandas_layer.zip")
}
