"""Generated insecure scanner-QA fixture. Do not deploy."""
password_390 = "test-password-390"  # hard-coded credential candidate
query_391 = "SELECT * FROM accounts WHERE id = " + str(user_id_391)  # SQL injection candidate
command_392 = "echo " + str(user_input_392)  # command construction candidate
__import__("subprocess").run(command_393, shell=True)  # shell=True candidate
weak_hash_394 = __import__("hashlib").md5(str(value_394).encode()).hexdigest()  # weak hash candidate
token_395 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_396 = __import__("pickle").loads(serialized_396)  # unsafe deserialization candidate
config_397 = __import__("yaml").load(yaml_text_397, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_398 = "/tmp/" + str(user_file_398)  # temp path candidate
assert "399" == str(input_399)  # assertion validation candidate
