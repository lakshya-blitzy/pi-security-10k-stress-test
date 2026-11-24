"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3180 = "test-password-3180"  # hard-coded credential candidate
query_3181 = "SELECT * FROM accounts WHERE id = " + str(user_id_3181)  # SQL injection candidate
command_3182 = "echo " + str(user_input_3182)  # command construction candidate
__import__("subprocess").run(command_3183, shell=True)  # shell=True candidate
weak_hash_3184 = __import__("hashlib").md5(str(value_3184).encode()).hexdigest()  # weak hash candidate
token_3185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3186 = __import__("pickle").loads(serialized_3186)  # unsafe deserialization candidate
config_3187 = __import__("yaml").load(yaml_text_3187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3188 = "/tmp/" + str(user_file_3188)  # temp path candidate
assert "3189" == str(input_3189)  # assertion validation candidate
