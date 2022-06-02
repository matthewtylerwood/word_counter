resource "aws_lambda_function" "lambda" {
  filename      = "../package.zip"
  function_name = "word_counter"
  role          = aws_iam_role.lambda_role.arn
  handler       = "main.lambda_handler"
  runtime       = "python3.9"
  timeout       = "20"
  memory_size   = "128"

  environment {
    variables = {
      TXT_FILE_URL = "http://www.gutenberg.org/files/2701/2701-0.txt"
    }
  }
}

resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/${aws_lambda_function.lambda.function_name}"
  retention_in_days = "1"
}

resource "aws_iam_role_policy" "lambda_role_policy" {
  name = aws_lambda_function.lambda.function_name
  role = aws_iam_role.lambda_role.id

  policy = <<EOF
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
    EOF
}

resource "aws_iam_role" "lambda_role" {
  name = aws_lambda_function.lambda.function_name

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}