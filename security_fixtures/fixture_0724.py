"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7240 = "test-password-7240"  # hard-coded credential candidate
query_7241 = "SELECT * FROM accounts WHERE id = " + str(user_id_7241)  # SQL injection candidate
command_7242 = "echo " + str(user_input_7242)  # command construction candidate
__import__("subprocess").run(command_7243, shell=True)  # shell=True candidate
weak_hash_7244 = __import__("hashlib").md5(str(value_7244).encode()).hexdigest()  # weak hash candidate
token_7245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7246 = __import__("pickle").loads(serialized_7246)  # unsafe deserialization candidate
config_7247 = __import__("yaml").load(yaml_text_7247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7248 = "/tmp/" + str(user_file_7248)  # temp path candidate
assert "7249" == str(input_7249)  # assertion validation candidate
