"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6060 = "test-password-6060"  # hard-coded credential candidate
query_6061 = "SELECT * FROM accounts WHERE id = " + str(user_id_6061)  # SQL injection candidate
command_6062 = "echo " + str(user_input_6062)  # command construction candidate
__import__("subprocess").run(command_6063, shell=True)  # shell=True candidate
weak_hash_6064 = __import__("hashlib").md5(str(value_6064).encode()).hexdigest()  # weak hash candidate
token_6065 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6066 = __import__("pickle").loads(serialized_6066)  # unsafe deserialization candidate
config_6067 = __import__("yaml").load(yaml_text_6067, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6068 = "/tmp/" + str(user_file_6068)  # temp path candidate
assert "6069" == str(input_6069)  # assertion validation candidate
