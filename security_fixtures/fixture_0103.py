"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1030 = "test-password-1030"  # hard-coded credential candidate
query_1031 = "SELECT * FROM accounts WHERE id = " + str(user_id_1031)  # SQL injection candidate
command_1032 = "echo " + str(user_input_1032)  # command construction candidate
__import__("subprocess").run(command_1033, shell=True)  # shell=True candidate
weak_hash_1034 = __import__("hashlib").md5(str(value_1034).encode()).hexdigest()  # weak hash candidate
token_1035 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1036 = __import__("pickle").loads(serialized_1036)  # unsafe deserialization candidate
config_1037 = __import__("yaml").load(yaml_text_1037, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1038 = "/tmp/" + str(user_file_1038)  # temp path candidate
assert "1039" == str(input_1039)  # assertion validation candidate
