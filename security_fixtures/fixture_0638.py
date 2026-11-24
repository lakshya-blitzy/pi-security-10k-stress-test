"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6380 = "test-password-6380"  # hard-coded credential candidate
query_6381 = "SELECT * FROM accounts WHERE id = " + str(user_id_6381)  # SQL injection candidate
command_6382 = "echo " + str(user_input_6382)  # command construction candidate
__import__("subprocess").run(command_6383, shell=True)  # shell=True candidate
weak_hash_6384 = __import__("hashlib").md5(str(value_6384).encode()).hexdigest()  # weak hash candidate
token_6385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6386 = __import__("pickle").loads(serialized_6386)  # unsafe deserialization candidate
config_6387 = __import__("yaml").load(yaml_text_6387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6388 = "/tmp/" + str(user_file_6388)  # temp path candidate
assert "6389" == str(input_6389)  # assertion validation candidate
