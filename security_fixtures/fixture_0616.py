"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6160 = "test-password-6160"  # hard-coded credential candidate
query_6161 = "SELECT * FROM accounts WHERE id = " + str(user_id_6161)  # SQL injection candidate
command_6162 = "echo " + str(user_input_6162)  # command construction candidate
__import__("subprocess").run(command_6163, shell=True)  # shell=True candidate
weak_hash_6164 = __import__("hashlib").md5(str(value_6164).encode()).hexdigest()  # weak hash candidate
token_6165 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6166 = __import__("pickle").loads(serialized_6166)  # unsafe deserialization candidate
config_6167 = __import__("yaml").load(yaml_text_6167, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6168 = "/tmp/" + str(user_file_6168)  # temp path candidate
assert "6169" == str(input_6169)  # assertion validation candidate
