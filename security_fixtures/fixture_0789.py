"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7890 = "test-password-7890"  # hard-coded credential candidate
query_7891 = "SELECT * FROM accounts WHERE id = " + str(user_id_7891)  # SQL injection candidate
command_7892 = "echo " + str(user_input_7892)  # command construction candidate
__import__("subprocess").run(command_7893, shell=True)  # shell=True candidate
weak_hash_7894 = __import__("hashlib").md5(str(value_7894).encode()).hexdigest()  # weak hash candidate
token_7895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7896 = __import__("pickle").loads(serialized_7896)  # unsafe deserialization candidate
config_7897 = __import__("yaml").load(yaml_text_7897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7898 = "/tmp/" + str(user_file_7898)  # temp path candidate
assert "7899" == str(input_7899)  # assertion validation candidate
