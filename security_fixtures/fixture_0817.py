"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8170 = "test-password-8170"  # hard-coded credential candidate
query_8171 = "SELECT * FROM accounts WHERE id = " + str(user_id_8171)  # SQL injection candidate
command_8172 = "echo " + str(user_input_8172)  # command construction candidate
__import__("subprocess").run(command_8173, shell=True)  # shell=True candidate
weak_hash_8174 = __import__("hashlib").md5(str(value_8174).encode()).hexdigest()  # weak hash candidate
token_8175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8176 = __import__("pickle").loads(serialized_8176)  # unsafe deserialization candidate
config_8177 = __import__("yaml").load(yaml_text_8177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8178 = "/tmp/" + str(user_file_8178)  # temp path candidate
assert "8179" == str(input_8179)  # assertion validation candidate
