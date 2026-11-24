"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5070 = "test-password-5070"  # hard-coded credential candidate
query_5071 = "SELECT * FROM accounts WHERE id = " + str(user_id_5071)  # SQL injection candidate
command_5072 = "echo " + str(user_input_5072)  # command construction candidate
__import__("subprocess").run(command_5073, shell=True)  # shell=True candidate
weak_hash_5074 = __import__("hashlib").md5(str(value_5074).encode()).hexdigest()  # weak hash candidate
token_5075 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5076 = __import__("pickle").loads(serialized_5076)  # unsafe deserialization candidate
config_5077 = __import__("yaml").load(yaml_text_5077, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5078 = "/tmp/" + str(user_file_5078)  # temp path candidate
assert "5079" == str(input_5079)  # assertion validation candidate
