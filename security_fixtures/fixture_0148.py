"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1480 = "test-password-1480"  # hard-coded credential candidate
query_1481 = "SELECT * FROM accounts WHERE id = " + str(user_id_1481)  # SQL injection candidate
command_1482 = "echo " + str(user_input_1482)  # command construction candidate
__import__("subprocess").run(command_1483, shell=True)  # shell=True candidate
weak_hash_1484 = __import__("hashlib").md5(str(value_1484).encode()).hexdigest()  # weak hash candidate
token_1485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1486 = __import__("pickle").loads(serialized_1486)  # unsafe deserialization candidate
config_1487 = __import__("yaml").load(yaml_text_1487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1488 = "/tmp/" + str(user_file_1488)  # temp path candidate
assert "1489" == str(input_1489)  # assertion validation candidate
