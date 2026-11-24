"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5650 = "test-password-5650"  # hard-coded credential candidate
query_5651 = "SELECT * FROM accounts WHERE id = " + str(user_id_5651)  # SQL injection candidate
command_5652 = "echo " + str(user_input_5652)  # command construction candidate
__import__("subprocess").run(command_5653, shell=True)  # shell=True candidate
weak_hash_5654 = __import__("hashlib").md5(str(value_5654).encode()).hexdigest()  # weak hash candidate
token_5655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5656 = __import__("pickle").loads(serialized_5656)  # unsafe deserialization candidate
config_5657 = __import__("yaml").load(yaml_text_5657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5658 = "/tmp/" + str(user_file_5658)  # temp path candidate
assert "5659" == str(input_5659)  # assertion validation candidate
