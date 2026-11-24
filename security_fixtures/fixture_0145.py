"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1450 = "test-password-1450"  # hard-coded credential candidate
query_1451 = "SELECT * FROM accounts WHERE id = " + str(user_id_1451)  # SQL injection candidate
command_1452 = "echo " + str(user_input_1452)  # command construction candidate
__import__("subprocess").run(command_1453, shell=True)  # shell=True candidate
weak_hash_1454 = __import__("hashlib").md5(str(value_1454).encode()).hexdigest()  # weak hash candidate
token_1455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1456 = __import__("pickle").loads(serialized_1456)  # unsafe deserialization candidate
config_1457 = __import__("yaml").load(yaml_text_1457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1458 = "/tmp/" + str(user_file_1458)  # temp path candidate
assert "1459" == str(input_1459)  # assertion validation candidate
