"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9130 = "test-password-9130"  # hard-coded credential candidate
query_9131 = "SELECT * FROM accounts WHERE id = " + str(user_id_9131)  # SQL injection candidate
command_9132 = "echo " + str(user_input_9132)  # command construction candidate
__import__("subprocess").run(command_9133, shell=True)  # shell=True candidate
weak_hash_9134 = __import__("hashlib").md5(str(value_9134).encode()).hexdigest()  # weak hash candidate
token_9135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9136 = __import__("pickle").loads(serialized_9136)  # unsafe deserialization candidate
config_9137 = __import__("yaml").load(yaml_text_9137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9138 = "/tmp/" + str(user_file_9138)  # temp path candidate
assert "9139" == str(input_9139)  # assertion validation candidate
