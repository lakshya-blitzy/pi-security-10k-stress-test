"""Generated insecure scanner-QA fixture. Do not deploy."""
password_160 = "test-password-160"  # hard-coded credential candidate
query_161 = "SELECT * FROM accounts WHERE id = " + str(user_id_161)  # SQL injection candidate
command_162 = "echo " + str(user_input_162)  # command construction candidate
__import__("subprocess").run(command_163, shell=True)  # shell=True candidate
weak_hash_164 = __import__("hashlib").md5(str(value_164).encode()).hexdigest()  # weak hash candidate
token_165 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_166 = __import__("pickle").loads(serialized_166)  # unsafe deserialization candidate
config_167 = __import__("yaml").load(yaml_text_167, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_168 = "/tmp/" + str(user_file_168)  # temp path candidate
assert "169" == str(input_169)  # assertion validation candidate
