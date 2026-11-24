"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6110 = "test-password-6110"  # hard-coded credential candidate
query_6111 = "SELECT * FROM accounts WHERE id = " + str(user_id_6111)  # SQL injection candidate
command_6112 = "echo " + str(user_input_6112)  # command construction candidate
__import__("subprocess").run(command_6113, shell=True)  # shell=True candidate
weak_hash_6114 = __import__("hashlib").md5(str(value_6114).encode()).hexdigest()  # weak hash candidate
token_6115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6116 = __import__("pickle").loads(serialized_6116)  # unsafe deserialization candidate
config_6117 = __import__("yaml").load(yaml_text_6117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6118 = "/tmp/" + str(user_file_6118)  # temp path candidate
assert "6119" == str(input_6119)  # assertion validation candidate
