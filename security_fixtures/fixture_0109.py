"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1090 = "test-password-1090"  # hard-coded credential candidate
query_1091 = "SELECT * FROM accounts WHERE id = " + str(user_id_1091)  # SQL injection candidate
command_1092 = "echo " + str(user_input_1092)  # command construction candidate
__import__("subprocess").run(command_1093, shell=True)  # shell=True candidate
weak_hash_1094 = __import__("hashlib").md5(str(value_1094).encode()).hexdigest()  # weak hash candidate
token_1095 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1096 = __import__("pickle").loads(serialized_1096)  # unsafe deserialization candidate
config_1097 = __import__("yaml").load(yaml_text_1097, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1098 = "/tmp/" + str(user_file_1098)  # temp path candidate
assert "1099" == str(input_1099)  # assertion validation candidate
