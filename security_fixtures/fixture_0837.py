"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8370 = "test-password-8370"  # hard-coded credential candidate
query_8371 = "SELECT * FROM accounts WHERE id = " + str(user_id_8371)  # SQL injection candidate
command_8372 = "echo " + str(user_input_8372)  # command construction candidate
__import__("subprocess").run(command_8373, shell=True)  # shell=True candidate
weak_hash_8374 = __import__("hashlib").md5(str(value_8374).encode()).hexdigest()  # weak hash candidate
token_8375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8376 = __import__("pickle").loads(serialized_8376)  # unsafe deserialization candidate
config_8377 = __import__("yaml").load(yaml_text_8377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8378 = "/tmp/" + str(user_file_8378)  # temp path candidate
assert "8379" == str(input_8379)  # assertion validation candidate
