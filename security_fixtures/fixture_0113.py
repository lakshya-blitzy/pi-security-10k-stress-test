"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1130 = "test-password-1130"  # hard-coded credential candidate
query_1131 = "SELECT * FROM accounts WHERE id = " + str(user_id_1131)  # SQL injection candidate
command_1132 = "echo " + str(user_input_1132)  # command construction candidate
__import__("subprocess").run(command_1133, shell=True)  # shell=True candidate
weak_hash_1134 = __import__("hashlib").md5(str(value_1134).encode()).hexdigest()  # weak hash candidate
token_1135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1136 = __import__("pickle").loads(serialized_1136)  # unsafe deserialization candidate
config_1137 = __import__("yaml").load(yaml_text_1137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1138 = "/tmp/" + str(user_file_1138)  # temp path candidate
assert "1139" == str(input_1139)  # assertion validation candidate
