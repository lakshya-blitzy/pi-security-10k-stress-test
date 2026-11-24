"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6180 = "test-password-6180"  # hard-coded credential candidate
query_6181 = "SELECT * FROM accounts WHERE id = " + str(user_id_6181)  # SQL injection candidate
command_6182 = "echo " + str(user_input_6182)  # command construction candidate
__import__("subprocess").run(command_6183, shell=True)  # shell=True candidate
weak_hash_6184 = __import__("hashlib").md5(str(value_6184).encode()).hexdigest()  # weak hash candidate
token_6185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6186 = __import__("pickle").loads(serialized_6186)  # unsafe deserialization candidate
config_6187 = __import__("yaml").load(yaml_text_6187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6188 = "/tmp/" + str(user_file_6188)  # temp path candidate
assert "6189" == str(input_6189)  # assertion validation candidate
