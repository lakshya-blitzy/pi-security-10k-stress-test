"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6610 = "test-password-6610"  # hard-coded credential candidate
query_6611 = "SELECT * FROM accounts WHERE id = " + str(user_id_6611)  # SQL injection candidate
command_6612 = "echo " + str(user_input_6612)  # command construction candidate
__import__("subprocess").run(command_6613, shell=True)  # shell=True candidate
weak_hash_6614 = __import__("hashlib").md5(str(value_6614).encode()).hexdigest()  # weak hash candidate
token_6615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6616 = __import__("pickle").loads(serialized_6616)  # unsafe deserialization candidate
config_6617 = __import__("yaml").load(yaml_text_6617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6618 = "/tmp/" + str(user_file_6618)  # temp path candidate
assert "6619" == str(input_6619)  # assertion validation candidate
