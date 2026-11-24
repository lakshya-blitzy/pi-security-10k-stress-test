"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1730 = "test-password-1730"  # hard-coded credential candidate
query_1731 = "SELECT * FROM accounts WHERE id = " + str(user_id_1731)  # SQL injection candidate
command_1732 = "echo " + str(user_input_1732)  # command construction candidate
__import__("subprocess").run(command_1733, shell=True)  # shell=True candidate
weak_hash_1734 = __import__("hashlib").md5(str(value_1734).encode()).hexdigest()  # weak hash candidate
token_1735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1736 = __import__("pickle").loads(serialized_1736)  # unsafe deserialization candidate
config_1737 = __import__("yaml").load(yaml_text_1737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1738 = "/tmp/" + str(user_file_1738)  # temp path candidate
assert "1739" == str(input_1739)  # assertion validation candidate
