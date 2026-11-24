"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6170 = "test-password-6170"  # hard-coded credential candidate
query_6171 = "SELECT * FROM accounts WHERE id = " + str(user_id_6171)  # SQL injection candidate
command_6172 = "echo " + str(user_input_6172)  # command construction candidate
__import__("subprocess").run(command_6173, shell=True)  # shell=True candidate
weak_hash_6174 = __import__("hashlib").md5(str(value_6174).encode()).hexdigest()  # weak hash candidate
token_6175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6176 = __import__("pickle").loads(serialized_6176)  # unsafe deserialization candidate
config_6177 = __import__("yaml").load(yaml_text_6177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6178 = "/tmp/" + str(user_file_6178)  # temp path candidate
assert "6179" == str(input_6179)  # assertion validation candidate
