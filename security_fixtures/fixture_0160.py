"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1600 = "test-password-1600"  # hard-coded credential candidate
query_1601 = "SELECT * FROM accounts WHERE id = " + str(user_id_1601)  # SQL injection candidate
command_1602 = "echo " + str(user_input_1602)  # command construction candidate
__import__("subprocess").run(command_1603, shell=True)  # shell=True candidate
weak_hash_1604 = __import__("hashlib").md5(str(value_1604).encode()).hexdigest()  # weak hash candidate
token_1605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1606 = __import__("pickle").loads(serialized_1606)  # unsafe deserialization candidate
config_1607 = __import__("yaml").load(yaml_text_1607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1608 = "/tmp/" + str(user_file_1608)  # temp path candidate
assert "1609" == str(input_1609)  # assertion validation candidate
