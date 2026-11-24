"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5020 = "test-password-5020"  # hard-coded credential candidate
query_5021 = "SELECT * FROM accounts WHERE id = " + str(user_id_5021)  # SQL injection candidate
command_5022 = "echo " + str(user_input_5022)  # command construction candidate
__import__("subprocess").run(command_5023, shell=True)  # shell=True candidate
weak_hash_5024 = __import__("hashlib").md5(str(value_5024).encode()).hexdigest()  # weak hash candidate
token_5025 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5026 = __import__("pickle").loads(serialized_5026)  # unsafe deserialization candidate
config_5027 = __import__("yaml").load(yaml_text_5027, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5028 = "/tmp/" + str(user_file_5028)  # temp path candidate
assert "5029" == str(input_5029)  # assertion validation candidate
