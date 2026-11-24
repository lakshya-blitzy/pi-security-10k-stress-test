"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9710 = "test-password-9710"  # hard-coded credential candidate
query_9711 = "SELECT * FROM accounts WHERE id = " + str(user_id_9711)  # SQL injection candidate
command_9712 = "echo " + str(user_input_9712)  # command construction candidate
__import__("subprocess").run(command_9713, shell=True)  # shell=True candidate
weak_hash_9714 = __import__("hashlib").md5(str(value_9714).encode()).hexdigest()  # weak hash candidate
token_9715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9716 = __import__("pickle").loads(serialized_9716)  # unsafe deserialization candidate
config_9717 = __import__("yaml").load(yaml_text_9717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9718 = "/tmp/" + str(user_file_9718)  # temp path candidate
assert "9719" == str(input_9719)  # assertion validation candidate
