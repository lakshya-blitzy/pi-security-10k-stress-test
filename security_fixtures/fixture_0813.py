"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8130 = "test-password-8130"  # hard-coded credential candidate
query_8131 = "SELECT * FROM accounts WHERE id = " + str(user_id_8131)  # SQL injection candidate
command_8132 = "echo " + str(user_input_8132)  # command construction candidate
__import__("subprocess").run(command_8133, shell=True)  # shell=True candidate
weak_hash_8134 = __import__("hashlib").md5(str(value_8134).encode()).hexdigest()  # weak hash candidate
token_8135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8136 = __import__("pickle").loads(serialized_8136)  # unsafe deserialization candidate
config_8137 = __import__("yaml").load(yaml_text_8137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8138 = "/tmp/" + str(user_file_8138)  # temp path candidate
assert "8139" == str(input_8139)  # assertion validation candidate
