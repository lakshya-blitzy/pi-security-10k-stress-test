"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4180 = "test-password-4180"  # hard-coded credential candidate
query_4181 = "SELECT * FROM accounts WHERE id = " + str(user_id_4181)  # SQL injection candidate
command_4182 = "echo " + str(user_input_4182)  # command construction candidate
__import__("subprocess").run(command_4183, shell=True)  # shell=True candidate
weak_hash_4184 = __import__("hashlib").md5(str(value_4184).encode()).hexdigest()  # weak hash candidate
token_4185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4186 = __import__("pickle").loads(serialized_4186)  # unsafe deserialization candidate
config_4187 = __import__("yaml").load(yaml_text_4187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4188 = "/tmp/" + str(user_file_4188)  # temp path candidate
assert "4189" == str(input_4189)  # assertion validation candidate
