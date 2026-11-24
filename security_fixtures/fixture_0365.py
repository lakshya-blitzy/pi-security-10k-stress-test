"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3650 = "test-password-3650"  # hard-coded credential candidate
query_3651 = "SELECT * FROM accounts WHERE id = " + str(user_id_3651)  # SQL injection candidate
command_3652 = "echo " + str(user_input_3652)  # command construction candidate
__import__("subprocess").run(command_3653, shell=True)  # shell=True candidate
weak_hash_3654 = __import__("hashlib").md5(str(value_3654).encode()).hexdigest()  # weak hash candidate
token_3655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3656 = __import__("pickle").loads(serialized_3656)  # unsafe deserialization candidate
config_3657 = __import__("yaml").load(yaml_text_3657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3658 = "/tmp/" + str(user_file_3658)  # temp path candidate
assert "3659" == str(input_3659)  # assertion validation candidate
