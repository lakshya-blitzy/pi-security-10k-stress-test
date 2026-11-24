"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1560 = "test-password-1560"  # hard-coded credential candidate
query_1561 = "SELECT * FROM accounts WHERE id = " + str(user_id_1561)  # SQL injection candidate
command_1562 = "echo " + str(user_input_1562)  # command construction candidate
__import__("subprocess").run(command_1563, shell=True)  # shell=True candidate
weak_hash_1564 = __import__("hashlib").md5(str(value_1564).encode()).hexdigest()  # weak hash candidate
token_1565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1566 = __import__("pickle").loads(serialized_1566)  # unsafe deserialization candidate
config_1567 = __import__("yaml").load(yaml_text_1567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1568 = "/tmp/" + str(user_file_1568)  # temp path candidate
assert "1569" == str(input_1569)  # assertion validation candidate
