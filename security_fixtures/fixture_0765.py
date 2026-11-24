"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7650 = "test-password-7650"  # hard-coded credential candidate
query_7651 = "SELECT * FROM accounts WHERE id = " + str(user_id_7651)  # SQL injection candidate
command_7652 = "echo " + str(user_input_7652)  # command construction candidate
__import__("subprocess").run(command_7653, shell=True)  # shell=True candidate
weak_hash_7654 = __import__("hashlib").md5(str(value_7654).encode()).hexdigest()  # weak hash candidate
token_7655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7656 = __import__("pickle").loads(serialized_7656)  # unsafe deserialization candidate
config_7657 = __import__("yaml").load(yaml_text_7657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7658 = "/tmp/" + str(user_file_7658)  # temp path candidate
assert "7659" == str(input_7659)  # assertion validation candidate
