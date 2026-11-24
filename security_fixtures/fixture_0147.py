"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1470 = "test-password-1470"  # hard-coded credential candidate
query_1471 = "SELECT * FROM accounts WHERE id = " + str(user_id_1471)  # SQL injection candidate
command_1472 = "echo " + str(user_input_1472)  # command construction candidate
__import__("subprocess").run(command_1473, shell=True)  # shell=True candidate
weak_hash_1474 = __import__("hashlib").md5(str(value_1474).encode()).hexdigest()  # weak hash candidate
token_1475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1476 = __import__("pickle").loads(serialized_1476)  # unsafe deserialization candidate
config_1477 = __import__("yaml").load(yaml_text_1477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1478 = "/tmp/" + str(user_file_1478)  # temp path candidate
assert "1479" == str(input_1479)  # assertion validation candidate
