"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8710 = "test-password-8710"  # hard-coded credential candidate
query_8711 = "SELECT * FROM accounts WHERE id = " + str(user_id_8711)  # SQL injection candidate
command_8712 = "echo " + str(user_input_8712)  # command construction candidate
__import__("subprocess").run(command_8713, shell=True)  # shell=True candidate
weak_hash_8714 = __import__("hashlib").md5(str(value_8714).encode()).hexdigest()  # weak hash candidate
token_8715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8716 = __import__("pickle").loads(serialized_8716)  # unsafe deserialization candidate
config_8717 = __import__("yaml").load(yaml_text_8717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8718 = "/tmp/" + str(user_file_8718)  # temp path candidate
assert "8719" == str(input_8719)  # assertion validation candidate
