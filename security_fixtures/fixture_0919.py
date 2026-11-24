"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9190 = "test-password-9190"  # hard-coded credential candidate
query_9191 = "SELECT * FROM accounts WHERE id = " + str(user_id_9191)  # SQL injection candidate
command_9192 = "echo " + str(user_input_9192)  # command construction candidate
__import__("subprocess").run(command_9193, shell=True)  # shell=True candidate
weak_hash_9194 = __import__("hashlib").md5(str(value_9194).encode()).hexdigest()  # weak hash candidate
token_9195 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9196 = __import__("pickle").loads(serialized_9196)  # unsafe deserialization candidate
config_9197 = __import__("yaml").load(yaml_text_9197, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9198 = "/tmp/" + str(user_file_9198)  # temp path candidate
assert "9199" == str(input_9199)  # assertion validation candidate
