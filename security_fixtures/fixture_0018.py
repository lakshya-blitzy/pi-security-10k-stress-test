"""Generated insecure scanner-QA fixture. Do not deploy."""
password_180 = "test-password-180"  # hard-coded credential candidate
query_181 = "SELECT * FROM accounts WHERE id = " + str(user_id_181)  # SQL injection candidate
command_182 = "echo " + str(user_input_182)  # command construction candidate
__import__("subprocess").run(command_183, shell=True)  # shell=True candidate
weak_hash_184 = __import__("hashlib").md5(str(value_184).encode()).hexdigest()  # weak hash candidate
token_185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_186 = __import__("pickle").loads(serialized_186)  # unsafe deserialization candidate
config_187 = __import__("yaml").load(yaml_text_187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_188 = "/tmp/" + str(user_file_188)  # temp path candidate
assert "189" == str(input_189)  # assertion validation candidate
