"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8650 = "test-password-8650"  # hard-coded credential candidate
query_8651 = "SELECT * FROM accounts WHERE id = " + str(user_id_8651)  # SQL injection candidate
command_8652 = "echo " + str(user_input_8652)  # command construction candidate
__import__("subprocess").run(command_8653, shell=True)  # shell=True candidate
weak_hash_8654 = __import__("hashlib").md5(str(value_8654).encode()).hexdigest()  # weak hash candidate
token_8655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8656 = __import__("pickle").loads(serialized_8656)  # unsafe deserialization candidate
config_8657 = __import__("yaml").load(yaml_text_8657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8658 = "/tmp/" + str(user_file_8658)  # temp path candidate
assert "8659" == str(input_8659)  # assertion validation candidate
