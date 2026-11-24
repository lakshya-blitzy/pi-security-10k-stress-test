"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1110 = "test-password-1110"  # hard-coded credential candidate
query_1111 = "SELECT * FROM accounts WHERE id = " + str(user_id_1111)  # SQL injection candidate
command_1112 = "echo " + str(user_input_1112)  # command construction candidate
__import__("subprocess").run(command_1113, shell=True)  # shell=True candidate
weak_hash_1114 = __import__("hashlib").md5(str(value_1114).encode()).hexdigest()  # weak hash candidate
token_1115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1116 = __import__("pickle").loads(serialized_1116)  # unsafe deserialization candidate
config_1117 = __import__("yaml").load(yaml_text_1117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1118 = "/tmp/" + str(user_file_1118)  # temp path candidate
assert "1119" == str(input_1119)  # assertion validation candidate
