"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6590 = "test-password-6590"  # hard-coded credential candidate
query_6591 = "SELECT * FROM accounts WHERE id = " + str(user_id_6591)  # SQL injection candidate
command_6592 = "echo " + str(user_input_6592)  # command construction candidate
__import__("subprocess").run(command_6593, shell=True)  # shell=True candidate
weak_hash_6594 = __import__("hashlib").md5(str(value_6594).encode()).hexdigest()  # weak hash candidate
token_6595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6596 = __import__("pickle").loads(serialized_6596)  # unsafe deserialization candidate
config_6597 = __import__("yaml").load(yaml_text_6597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6598 = "/tmp/" + str(user_file_6598)  # temp path candidate
assert "6599" == str(input_6599)  # assertion validation candidate
