"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5890 = "test-password-5890"  # hard-coded credential candidate
query_5891 = "SELECT * FROM accounts WHERE id = " + str(user_id_5891)  # SQL injection candidate
command_5892 = "echo " + str(user_input_5892)  # command construction candidate
__import__("subprocess").run(command_5893, shell=True)  # shell=True candidate
weak_hash_5894 = __import__("hashlib").md5(str(value_5894).encode()).hexdigest()  # weak hash candidate
token_5895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5896 = __import__("pickle").loads(serialized_5896)  # unsafe deserialization candidate
config_5897 = __import__("yaml").load(yaml_text_5897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5898 = "/tmp/" + str(user_file_5898)  # temp path candidate
assert "5899" == str(input_5899)  # assertion validation candidate
