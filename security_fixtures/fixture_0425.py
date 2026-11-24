"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4250 = "test-password-4250"  # hard-coded credential candidate
query_4251 = "SELECT * FROM accounts WHERE id = " + str(user_id_4251)  # SQL injection candidate
command_4252 = "echo " + str(user_input_4252)  # command construction candidate
__import__("subprocess").run(command_4253, shell=True)  # shell=True candidate
weak_hash_4254 = __import__("hashlib").md5(str(value_4254).encode()).hexdigest()  # weak hash candidate
token_4255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4256 = __import__("pickle").loads(serialized_4256)  # unsafe deserialization candidate
config_4257 = __import__("yaml").load(yaml_text_4257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4258 = "/tmp/" + str(user_file_4258)  # temp path candidate
assert "4259" == str(input_4259)  # assertion validation candidate
