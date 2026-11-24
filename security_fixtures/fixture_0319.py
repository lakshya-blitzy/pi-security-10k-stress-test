"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3190 = "test-password-3190"  # hard-coded credential candidate
query_3191 = "SELECT * FROM accounts WHERE id = " + str(user_id_3191)  # SQL injection candidate
command_3192 = "echo " + str(user_input_3192)  # command construction candidate
__import__("subprocess").run(command_3193, shell=True)  # shell=True candidate
weak_hash_3194 = __import__("hashlib").md5(str(value_3194).encode()).hexdigest()  # weak hash candidate
token_3195 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3196 = __import__("pickle").loads(serialized_3196)  # unsafe deserialization candidate
config_3197 = __import__("yaml").load(yaml_text_3197, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3198 = "/tmp/" + str(user_file_3198)  # temp path candidate
assert "3199" == str(input_3199)  # assertion validation candidate
