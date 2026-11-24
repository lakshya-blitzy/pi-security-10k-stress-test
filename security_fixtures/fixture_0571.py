"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5710 = "test-password-5710"  # hard-coded credential candidate
query_5711 = "SELECT * FROM accounts WHERE id = " + str(user_id_5711)  # SQL injection candidate
command_5712 = "echo " + str(user_input_5712)  # command construction candidate
__import__("subprocess").run(command_5713, shell=True)  # shell=True candidate
weak_hash_5714 = __import__("hashlib").md5(str(value_5714).encode()).hexdigest()  # weak hash candidate
token_5715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5716 = __import__("pickle").loads(serialized_5716)  # unsafe deserialization candidate
config_5717 = __import__("yaml").load(yaml_text_5717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5718 = "/tmp/" + str(user_file_5718)  # temp path candidate
assert "5719" == str(input_5719)  # assertion validation candidate
