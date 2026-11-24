"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1070 = "test-password-1070"  # hard-coded credential candidate
query_1071 = "SELECT * FROM accounts WHERE id = " + str(user_id_1071)  # SQL injection candidate
command_1072 = "echo " + str(user_input_1072)  # command construction candidate
__import__("subprocess").run(command_1073, shell=True)  # shell=True candidate
weak_hash_1074 = __import__("hashlib").md5(str(value_1074).encode()).hexdigest()  # weak hash candidate
token_1075 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1076 = __import__("pickle").loads(serialized_1076)  # unsafe deserialization candidate
config_1077 = __import__("yaml").load(yaml_text_1077, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1078 = "/tmp/" + str(user_file_1078)  # temp path candidate
assert "1079" == str(input_1079)  # assertion validation candidate
