"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1430 = "test-password-1430"  # hard-coded credential candidate
query_1431 = "SELECT * FROM accounts WHERE id = " + str(user_id_1431)  # SQL injection candidate
command_1432 = "echo " + str(user_input_1432)  # command construction candidate
__import__("subprocess").run(command_1433, shell=True)  # shell=True candidate
weak_hash_1434 = __import__("hashlib").md5(str(value_1434).encode()).hexdigest()  # weak hash candidate
token_1435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1436 = __import__("pickle").loads(serialized_1436)  # unsafe deserialization candidate
config_1437 = __import__("yaml").load(yaml_text_1437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1438 = "/tmp/" + str(user_file_1438)  # temp path candidate
assert "1439" == str(input_1439)  # assertion validation candidate
