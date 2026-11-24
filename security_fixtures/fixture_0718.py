"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7180 = "test-password-7180"  # hard-coded credential candidate
query_7181 = "SELECT * FROM accounts WHERE id = " + str(user_id_7181)  # SQL injection candidate
command_7182 = "echo " + str(user_input_7182)  # command construction candidate
__import__("subprocess").run(command_7183, shell=True)  # shell=True candidate
weak_hash_7184 = __import__("hashlib").md5(str(value_7184).encode()).hexdigest()  # weak hash candidate
token_7185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7186 = __import__("pickle").loads(serialized_7186)  # unsafe deserialization candidate
config_7187 = __import__("yaml").load(yaml_text_7187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7188 = "/tmp/" + str(user_file_7188)  # temp path candidate
assert "7189" == str(input_7189)  # assertion validation candidate
