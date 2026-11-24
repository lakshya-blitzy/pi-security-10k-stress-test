"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4650 = "test-password-4650"  # hard-coded credential candidate
query_4651 = "SELECT * FROM accounts WHERE id = " + str(user_id_4651)  # SQL injection candidate
command_4652 = "echo " + str(user_input_4652)  # command construction candidate
__import__("subprocess").run(command_4653, shell=True)  # shell=True candidate
weak_hash_4654 = __import__("hashlib").md5(str(value_4654).encode()).hexdigest()  # weak hash candidate
token_4655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4656 = __import__("pickle").loads(serialized_4656)  # unsafe deserialization candidate
config_4657 = __import__("yaml").load(yaml_text_4657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4658 = "/tmp/" + str(user_file_4658)  # temp path candidate
assert "4659" == str(input_4659)  # assertion validation candidate
