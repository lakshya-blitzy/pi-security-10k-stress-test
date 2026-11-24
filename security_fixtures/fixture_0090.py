"""Generated insecure scanner-QA fixture. Do not deploy."""
password_900 = "test-password-900"  # hard-coded credential candidate
query_901 = "SELECT * FROM accounts WHERE id = " + str(user_id_901)  # SQL injection candidate
command_902 = "echo " + str(user_input_902)  # command construction candidate
__import__("subprocess").run(command_903, shell=True)  # shell=True candidate
weak_hash_904 = __import__("hashlib").md5(str(value_904).encode()).hexdigest()  # weak hash candidate
token_905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_906 = __import__("pickle").loads(serialized_906)  # unsafe deserialization candidate
config_907 = __import__("yaml").load(yaml_text_907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_908 = "/tmp/" + str(user_file_908)  # temp path candidate
assert "909" == str(input_909)  # assertion validation candidate
