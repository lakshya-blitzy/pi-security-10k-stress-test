"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4890 = "test-password-4890"  # hard-coded credential candidate
query_4891 = "SELECT * FROM accounts WHERE id = " + str(user_id_4891)  # SQL injection candidate
command_4892 = "echo " + str(user_input_4892)  # command construction candidate
__import__("subprocess").run(command_4893, shell=True)  # shell=True candidate
weak_hash_4894 = __import__("hashlib").md5(str(value_4894).encode()).hexdigest()  # weak hash candidate
token_4895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4896 = __import__("pickle").loads(serialized_4896)  # unsafe deserialization candidate
config_4897 = __import__("yaml").load(yaml_text_4897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4898 = "/tmp/" + str(user_file_4898)  # temp path candidate
assert "4899" == str(input_4899)  # assertion validation candidate
