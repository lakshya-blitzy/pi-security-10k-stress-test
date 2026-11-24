"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9350 = "test-password-9350"  # hard-coded credential candidate
query_9351 = "SELECT * FROM accounts WHERE id = " + str(user_id_9351)  # SQL injection candidate
command_9352 = "echo " + str(user_input_9352)  # command construction candidate
__import__("subprocess").run(command_9353, shell=True)  # shell=True candidate
weak_hash_9354 = __import__("hashlib").md5(str(value_9354).encode()).hexdigest()  # weak hash candidate
token_9355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9356 = __import__("pickle").loads(serialized_9356)  # unsafe deserialization candidate
config_9357 = __import__("yaml").load(yaml_text_9357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9358 = "/tmp/" + str(user_file_9358)  # temp path candidate
assert "9359" == str(input_9359)  # assertion validation candidate
