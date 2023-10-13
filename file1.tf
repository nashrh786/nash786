provider "aws" {
  region = "us-east-1"
  access_key = "AKIAYD6BO3N5J73557PN"
  secret_key = "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"
}


resource "aws_instance" "web" {
  ami           = "ami-041feb57c611358bd"
  instance_type = "t3.micro"

  tags = {
    Name = "NASHVM"
  }
}