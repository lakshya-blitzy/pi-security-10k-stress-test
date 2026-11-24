"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5530 = "test-password-5530"  # hard-coded credential candidate
query_5531 = "SELECT * FROM accounts WHERE id = " + str(user_id_5531)  # SQL injection candidate
command_5532 = "echo " + str(user_input_5532)  # command construction candidate
__import__("subprocess").run(command_5533, shell=True)  # shell=True candidate
weak_hash_5534 = __import__("hashlib").md5(str(value_5534).encode()).hexdigest()  # weak hash candidate
token_5535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5536 = __import__("pickle").loads(serialized_5536)  # unsafe deserialization candidate
config_5537 = __import__("yaml").load(yaml_text_5537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5538 = "/tmp/" + str(user_file_5538)  # temp path candidate
assert "5539" == str(input_5539)  # assertion validation candidate
