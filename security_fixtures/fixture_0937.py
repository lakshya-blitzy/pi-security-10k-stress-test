"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9370 = "test-password-9370"  # hard-coded credential candidate
query_9371 = "SELECT * FROM accounts WHERE id = " + str(user_id_9371)  # SQL injection candidate
command_9372 = "echo " + str(user_input_9372)  # command construction candidate
__import__("subprocess").run(command_9373, shell=True)  # shell=True candidate
weak_hash_9374 = __import__("hashlib").md5(str(value_9374).encode()).hexdigest()  # weak hash candidate
token_9375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9376 = __import__("pickle").loads(serialized_9376)  # unsafe deserialization candidate
config_9377 = __import__("yaml").load(yaml_text_9377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9378 = "/tmp/" + str(user_file_9378)  # temp path candidate
assert "9379" == str(input_9379)  # assertion validation candidate
