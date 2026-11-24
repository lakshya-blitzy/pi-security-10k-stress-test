"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5190 = "test-password-5190"  # hard-coded credential candidate
query_5191 = "SELECT * FROM accounts WHERE id = " + str(user_id_5191)  # SQL injection candidate
command_5192 = "echo " + str(user_input_5192)  # command construction candidate
__import__("subprocess").run(command_5193, shell=True)  # shell=True candidate
weak_hash_5194 = __import__("hashlib").md5(str(value_5194).encode()).hexdigest()  # weak hash candidate
token_5195 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5196 = __import__("pickle").loads(serialized_5196)  # unsafe deserialization candidate
config_5197 = __import__("yaml").load(yaml_text_5197, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5198 = "/tmp/" + str(user_file_5198)  # temp path candidate
assert "5199" == str(input_5199)  # assertion validation candidate
