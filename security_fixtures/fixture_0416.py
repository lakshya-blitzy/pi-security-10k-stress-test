"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4160 = "test-password-4160"  # hard-coded credential candidate
query_4161 = "SELECT * FROM accounts WHERE id = " + str(user_id_4161)  # SQL injection candidate
command_4162 = "echo " + str(user_input_4162)  # command construction candidate
__import__("subprocess").run(command_4163, shell=True)  # shell=True candidate
weak_hash_4164 = __import__("hashlib").md5(str(value_4164).encode()).hexdigest()  # weak hash candidate
token_4165 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4166 = __import__("pickle").loads(serialized_4166)  # unsafe deserialization candidate
config_4167 = __import__("yaml").load(yaml_text_4167, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4168 = "/tmp/" + str(user_file_4168)  # temp path candidate
assert "4169" == str(input_4169)  # assertion validation candidate
