"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3890 = "test-password-3890"  # hard-coded credential candidate
query_3891 = "SELECT * FROM accounts WHERE id = " + str(user_id_3891)  # SQL injection candidate
command_3892 = "echo " + str(user_input_3892)  # command construction candidate
__import__("subprocess").run(command_3893, shell=True)  # shell=True candidate
weak_hash_3894 = __import__("hashlib").md5(str(value_3894).encode()).hexdigest()  # weak hash candidate
token_3895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3896 = __import__("pickle").loads(serialized_3896)  # unsafe deserialization candidate
config_3897 = __import__("yaml").load(yaml_text_3897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3898 = "/tmp/" + str(user_file_3898)  # temp path candidate
assert "3899" == str(input_3899)  # assertion validation candidate
