"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8110 = "test-password-8110"  # hard-coded credential candidate
query_8111 = "SELECT * FROM accounts WHERE id = " + str(user_id_8111)  # SQL injection candidate
command_8112 = "echo " + str(user_input_8112)  # command construction candidate
__import__("subprocess").run(command_8113, shell=True)  # shell=True candidate
weak_hash_8114 = __import__("hashlib").md5(str(value_8114).encode()).hexdigest()  # weak hash candidate
token_8115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8116 = __import__("pickle").loads(serialized_8116)  # unsafe deserialization candidate
config_8117 = __import__("yaml").load(yaml_text_8117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8118 = "/tmp/" + str(user_file_8118)  # temp path candidate
assert "8119" == str(input_8119)  # assertion validation candidate
