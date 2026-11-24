"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6650 = "test-password-6650"  # hard-coded credential candidate
query_6651 = "SELECT * FROM accounts WHERE id = " + str(user_id_6651)  # SQL injection candidate
command_6652 = "echo " + str(user_input_6652)  # command construction candidate
__import__("subprocess").run(command_6653, shell=True)  # shell=True candidate
weak_hash_6654 = __import__("hashlib").md5(str(value_6654).encode()).hexdigest()  # weak hash candidate
token_6655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6656 = __import__("pickle").loads(serialized_6656)  # unsafe deserialization candidate
config_6657 = __import__("yaml").load(yaml_text_6657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6658 = "/tmp/" + str(user_file_6658)  # temp path candidate
assert "6659" == str(input_6659)  # assertion validation candidate
