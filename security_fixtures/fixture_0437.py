"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4370 = "test-password-4370"  # hard-coded credential candidate
query_4371 = "SELECT * FROM accounts WHERE id = " + str(user_id_4371)  # SQL injection candidate
command_4372 = "echo " + str(user_input_4372)  # command construction candidate
__import__("subprocess").run(command_4373, shell=True)  # shell=True candidate
weak_hash_4374 = __import__("hashlib").md5(str(value_4374).encode()).hexdigest()  # weak hash candidate
token_4375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4376 = __import__("pickle").loads(serialized_4376)  # unsafe deserialization candidate
config_4377 = __import__("yaml").load(yaml_text_4377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4378 = "/tmp/" + str(user_file_4378)  # temp path candidate
assert "4379" == str(input_4379)  # assertion validation candidate
