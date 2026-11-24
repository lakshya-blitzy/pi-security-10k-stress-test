"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1160 = "test-password-1160"  # hard-coded credential candidate
query_1161 = "SELECT * FROM accounts WHERE id = " + str(user_id_1161)  # SQL injection candidate
command_1162 = "echo " + str(user_input_1162)  # command construction candidate
__import__("subprocess").run(command_1163, shell=True)  # shell=True candidate
weak_hash_1164 = __import__("hashlib").md5(str(value_1164).encode()).hexdigest()  # weak hash candidate
token_1165 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1166 = __import__("pickle").loads(serialized_1166)  # unsafe deserialization candidate
config_1167 = __import__("yaml").load(yaml_text_1167, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1168 = "/tmp/" + str(user_file_1168)  # temp path candidate
assert "1169" == str(input_1169)  # assertion validation candidate
