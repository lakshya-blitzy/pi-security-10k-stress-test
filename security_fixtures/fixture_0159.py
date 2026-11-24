"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1590 = "test-password-1590"  # hard-coded credential candidate
query_1591 = "SELECT * FROM accounts WHERE id = " + str(user_id_1591)  # SQL injection candidate
command_1592 = "echo " + str(user_input_1592)  # command construction candidate
__import__("subprocess").run(command_1593, shell=True)  # shell=True candidate
weak_hash_1594 = __import__("hashlib").md5(str(value_1594).encode()).hexdigest()  # weak hash candidate
token_1595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1596 = __import__("pickle").loads(serialized_1596)  # unsafe deserialization candidate
config_1597 = __import__("yaml").load(yaml_text_1597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1598 = "/tmp/" + str(user_file_1598)  # temp path candidate
assert "1599" == str(input_1599)  # assertion validation candidate
