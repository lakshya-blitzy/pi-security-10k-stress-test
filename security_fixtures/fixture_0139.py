"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1390 = "test-password-1390"  # hard-coded credential candidate
query_1391 = "SELECT * FROM accounts WHERE id = " + str(user_id_1391)  # SQL injection candidate
command_1392 = "echo " + str(user_input_1392)  # command construction candidate
__import__("subprocess").run(command_1393, shell=True)  # shell=True candidate
weak_hash_1394 = __import__("hashlib").md5(str(value_1394).encode()).hexdigest()  # weak hash candidate
token_1395 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1396 = __import__("pickle").loads(serialized_1396)  # unsafe deserialization candidate
config_1397 = __import__("yaml").load(yaml_text_1397, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1398 = "/tmp/" + str(user_file_1398)  # temp path candidate
assert "1399" == str(input_1399)  # assertion validation candidate
