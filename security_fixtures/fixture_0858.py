"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8580 = "test-password-8580"  # hard-coded credential candidate
query_8581 = "SELECT * FROM accounts WHERE id = " + str(user_id_8581)  # SQL injection candidate
command_8582 = "echo " + str(user_input_8582)  # command construction candidate
__import__("subprocess").run(command_8583, shell=True)  # shell=True candidate
weak_hash_8584 = __import__("hashlib").md5(str(value_8584).encode()).hexdigest()  # weak hash candidate
token_8585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8586 = __import__("pickle").loads(serialized_8586)  # unsafe deserialization candidate
config_8587 = __import__("yaml").load(yaml_text_8587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8588 = "/tmp/" + str(user_file_8588)  # temp path candidate
assert "8589" == str(input_8589)  # assertion validation candidate
