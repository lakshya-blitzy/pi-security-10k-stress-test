"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7110 = "test-password-7110"  # hard-coded credential candidate
query_7111 = "SELECT * FROM accounts WHERE id = " + str(user_id_7111)  # SQL injection candidate
command_7112 = "echo " + str(user_input_7112)  # command construction candidate
__import__("subprocess").run(command_7113, shell=True)  # shell=True candidate
weak_hash_7114 = __import__("hashlib").md5(str(value_7114).encode()).hexdigest()  # weak hash candidate
token_7115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7116 = __import__("pickle").loads(serialized_7116)  # unsafe deserialization candidate
config_7117 = __import__("yaml").load(yaml_text_7117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7118 = "/tmp/" + str(user_file_7118)  # temp path candidate
assert "7119" == str(input_7119)  # assertion validation candidate
