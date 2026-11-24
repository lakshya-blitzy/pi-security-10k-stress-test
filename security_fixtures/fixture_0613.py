"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6130 = "test-password-6130"  # hard-coded credential candidate
query_6131 = "SELECT * FROM accounts WHERE id = " + str(user_id_6131)  # SQL injection candidate
command_6132 = "echo " + str(user_input_6132)  # command construction candidate
__import__("subprocess").run(command_6133, shell=True)  # shell=True candidate
weak_hash_6134 = __import__("hashlib").md5(str(value_6134).encode()).hexdigest()  # weak hash candidate
token_6135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6136 = __import__("pickle").loads(serialized_6136)  # unsafe deserialization candidate
config_6137 = __import__("yaml").load(yaml_text_6137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6138 = "/tmp/" + str(user_file_6138)  # temp path candidate
assert "6139" == str(input_6139)  # assertion validation candidate
