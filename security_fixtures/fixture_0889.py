"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8890 = "test-password-8890"  # hard-coded credential candidate
query_8891 = "SELECT * FROM accounts WHERE id = " + str(user_id_8891)  # SQL injection candidate
command_8892 = "echo " + str(user_input_8892)  # command construction candidate
__import__("subprocess").run(command_8893, shell=True)  # shell=True candidate
weak_hash_8894 = __import__("hashlib").md5(str(value_8894).encode()).hexdigest()  # weak hash candidate
token_8895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8896 = __import__("pickle").loads(serialized_8896)  # unsafe deserialization candidate
config_8897 = __import__("yaml").load(yaml_text_8897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8898 = "/tmp/" + str(user_file_8898)  # temp path candidate
assert "8899" == str(input_8899)  # assertion validation candidate
