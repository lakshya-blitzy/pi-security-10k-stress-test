"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4190 = "test-password-4190"  # hard-coded credential candidate
query_4191 = "SELECT * FROM accounts WHERE id = " + str(user_id_4191)  # SQL injection candidate
command_4192 = "echo " + str(user_input_4192)  # command construction candidate
__import__("subprocess").run(command_4193, shell=True)  # shell=True candidate
weak_hash_4194 = __import__("hashlib").md5(str(value_4194).encode()).hexdigest()  # weak hash candidate
token_4195 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4196 = __import__("pickle").loads(serialized_4196)  # unsafe deserialization candidate
config_4197 = __import__("yaml").load(yaml_text_4197, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4198 = "/tmp/" + str(user_file_4198)  # temp path candidate
assert "4199" == str(input_4199)  # assertion validation candidate
