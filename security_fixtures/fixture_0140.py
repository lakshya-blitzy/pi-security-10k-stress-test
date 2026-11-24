"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1400 = "test-password-1400"  # hard-coded credential candidate
query_1401 = "SELECT * FROM accounts WHERE id = " + str(user_id_1401)  # SQL injection candidate
command_1402 = "echo " + str(user_input_1402)  # command construction candidate
__import__("subprocess").run(command_1403, shell=True)  # shell=True candidate
weak_hash_1404 = __import__("hashlib").md5(str(value_1404).encode()).hexdigest()  # weak hash candidate
token_1405 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1406 = __import__("pickle").loads(serialized_1406)  # unsafe deserialization candidate
config_1407 = __import__("yaml").load(yaml_text_1407, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1408 = "/tmp/" + str(user_file_1408)  # temp path candidate
assert "1409" == str(input_1409)  # assertion validation candidate
