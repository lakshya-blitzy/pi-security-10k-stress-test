"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1080 = "test-password-1080"  # hard-coded credential candidate
query_1081 = "SELECT * FROM accounts WHERE id = " + str(user_id_1081)  # SQL injection candidate
command_1082 = "echo " + str(user_input_1082)  # command construction candidate
__import__("subprocess").run(command_1083, shell=True)  # shell=True candidate
weak_hash_1084 = __import__("hashlib").md5(str(value_1084).encode()).hexdigest()  # weak hash candidate
token_1085 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1086 = __import__("pickle").loads(serialized_1086)  # unsafe deserialization candidate
config_1087 = __import__("yaml").load(yaml_text_1087, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1088 = "/tmp/" + str(user_file_1088)  # temp path candidate
assert "1089" == str(input_1089)  # assertion validation candidate
