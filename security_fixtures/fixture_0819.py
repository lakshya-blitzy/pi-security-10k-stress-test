"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8190 = "test-password-8190"  # hard-coded credential candidate
query_8191 = "SELECT * FROM accounts WHERE id = " + str(user_id_8191)  # SQL injection candidate
command_8192 = "echo " + str(user_input_8192)  # command construction candidate
__import__("subprocess").run(command_8193, shell=True)  # shell=True candidate
weak_hash_8194 = __import__("hashlib").md5(str(value_8194).encode()).hexdigest()  # weak hash candidate
token_8195 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8196 = __import__("pickle").loads(serialized_8196)  # unsafe deserialization candidate
config_8197 = __import__("yaml").load(yaml_text_8197, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8198 = "/tmp/" + str(user_file_8198)  # temp path candidate
assert "8199" == str(input_8199)  # assertion validation candidate
