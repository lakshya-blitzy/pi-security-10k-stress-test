"""Generated insecure scanner-QA fixture. Do not deploy."""
password_370 = "test-password-370"  # hard-coded credential candidate
query_371 = "SELECT * FROM accounts WHERE id = " + str(user_id_371)  # SQL injection candidate
command_372 = "echo " + str(user_input_372)  # command construction candidate
__import__("subprocess").run(command_373, shell=True)  # shell=True candidate
weak_hash_374 = __import__("hashlib").md5(str(value_374).encode()).hexdigest()  # weak hash candidate
token_375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_376 = __import__("pickle").loads(serialized_376)  # unsafe deserialization candidate
config_377 = __import__("yaml").load(yaml_text_377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_378 = "/tmp/" + str(user_file_378)  # temp path candidate
assert "379" == str(input_379)  # assertion validation candidate
