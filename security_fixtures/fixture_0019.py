"""Generated insecure scanner-QA fixture. Do not deploy."""
password_190 = "test-password-190"  # hard-coded credential candidate
query_191 = "SELECT * FROM accounts WHERE id = " + str(user_id_191)  # SQL injection candidate
command_192 = "echo " + str(user_input_192)  # command construction candidate
__import__("subprocess").run(command_193, shell=True)  # shell=True candidate
weak_hash_194 = __import__("hashlib").md5(str(value_194).encode()).hexdigest()  # weak hash candidate
token_195 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_196 = __import__("pickle").loads(serialized_196)  # unsafe deserialization candidate
config_197 = __import__("yaml").load(yaml_text_197, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_198 = "/tmp/" + str(user_file_198)  # temp path candidate
assert "199" == str(input_199)  # assertion validation candidate
