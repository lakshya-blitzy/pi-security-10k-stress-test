"""Generated insecure scanner-QA fixture. Do not deploy."""
password_890 = "test-password-890"  # hard-coded credential candidate
query_891 = "SELECT * FROM accounts WHERE id = " + str(user_id_891)  # SQL injection candidate
command_892 = "echo " + str(user_input_892)  # command construction candidate
__import__("subprocess").run(command_893, shell=True)  # shell=True candidate
weak_hash_894 = __import__("hashlib").md5(str(value_894).encode()).hexdigest()  # weak hash candidate
token_895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_896 = __import__("pickle").loads(serialized_896)  # unsafe deserialization candidate
config_897 = __import__("yaml").load(yaml_text_897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_898 = "/tmp/" + str(user_file_898)  # temp path candidate
assert "899" == str(input_899)  # assertion validation candidate
