"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1410 = "test-password-1410"  # hard-coded credential candidate
query_1411 = "SELECT * FROM accounts WHERE id = " + str(user_id_1411)  # SQL injection candidate
command_1412 = "echo " + str(user_input_1412)  # command construction candidate
__import__("subprocess").run(command_1413, shell=True)  # shell=True candidate
weak_hash_1414 = __import__("hashlib").md5(str(value_1414).encode()).hexdigest()  # weak hash candidate
token_1415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1416 = __import__("pickle").loads(serialized_1416)  # unsafe deserialization candidate
config_1417 = __import__("yaml").load(yaml_text_1417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1418 = "/tmp/" + str(user_file_1418)  # temp path candidate
assert "1419" == str(input_1419)  # assertion validation candidate
