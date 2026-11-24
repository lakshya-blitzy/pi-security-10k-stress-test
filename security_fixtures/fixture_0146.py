"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1460 = "test-password-1460"  # hard-coded credential candidate
query_1461 = "SELECT * FROM accounts WHERE id = " + str(user_id_1461)  # SQL injection candidate
command_1462 = "echo " + str(user_input_1462)  # command construction candidate
__import__("subprocess").run(command_1463, shell=True)  # shell=True candidate
weak_hash_1464 = __import__("hashlib").md5(str(value_1464).encode()).hexdigest()  # weak hash candidate
token_1465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1466 = __import__("pickle").loads(serialized_1466)  # unsafe deserialization candidate
config_1467 = __import__("yaml").load(yaml_text_1467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1468 = "/tmp/" + str(user_file_1468)  # temp path candidate
assert "1469" == str(input_1469)  # assertion validation candidate
