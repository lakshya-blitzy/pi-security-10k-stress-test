"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2190 = "test-password-2190"  # hard-coded credential candidate
query_2191 = "SELECT * FROM accounts WHERE id = " + str(user_id_2191)  # SQL injection candidate
command_2192 = "echo " + str(user_input_2192)  # command construction candidate
__import__("subprocess").run(command_2193, shell=True)  # shell=True candidate
weak_hash_2194 = __import__("hashlib").md5(str(value_2194).encode()).hexdigest()  # weak hash candidate
token_2195 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2196 = __import__("pickle").loads(serialized_2196)  # unsafe deserialization candidate
config_2197 = __import__("yaml").load(yaml_text_2197, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2198 = "/tmp/" + str(user_file_2198)  # temp path candidate
assert "2199" == str(input_2199)  # assertion validation candidate
