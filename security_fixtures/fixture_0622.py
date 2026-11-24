"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6220 = "test-password-6220"  # hard-coded credential candidate
query_6221 = "SELECT * FROM accounts WHERE id = " + str(user_id_6221)  # SQL injection candidate
command_6222 = "echo " + str(user_input_6222)  # command construction candidate
__import__("subprocess").run(command_6223, shell=True)  # shell=True candidate
weak_hash_6224 = __import__("hashlib").md5(str(value_6224).encode()).hexdigest()  # weak hash candidate
token_6225 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6226 = __import__("pickle").loads(serialized_6226)  # unsafe deserialization candidate
config_6227 = __import__("yaml").load(yaml_text_6227, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6228 = "/tmp/" + str(user_file_6228)  # temp path candidate
assert "6229" == str(input_6229)  # assertion validation candidate
