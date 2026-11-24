"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4110 = "test-password-4110"  # hard-coded credential candidate
query_4111 = "SELECT * FROM accounts WHERE id = " + str(user_id_4111)  # SQL injection candidate
command_4112 = "echo " + str(user_input_4112)  # command construction candidate
__import__("subprocess").run(command_4113, shell=True)  # shell=True candidate
weak_hash_4114 = __import__("hashlib").md5(str(value_4114).encode()).hexdigest()  # weak hash candidate
token_4115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4116 = __import__("pickle").loads(serialized_4116)  # unsafe deserialization candidate
config_4117 = __import__("yaml").load(yaml_text_4117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4118 = "/tmp/" + str(user_file_4118)  # temp path candidate
assert "4119" == str(input_4119)  # assertion validation candidate
