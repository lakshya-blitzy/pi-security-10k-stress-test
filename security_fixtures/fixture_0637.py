"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6370 = "test-password-6370"  # hard-coded credential candidate
query_6371 = "SELECT * FROM accounts WHERE id = " + str(user_id_6371)  # SQL injection candidate
command_6372 = "echo " + str(user_input_6372)  # command construction candidate
__import__("subprocess").run(command_6373, shell=True)  # shell=True candidate
weak_hash_6374 = __import__("hashlib").md5(str(value_6374).encode()).hexdigest()  # weak hash candidate
token_6375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6376 = __import__("pickle").loads(serialized_6376)  # unsafe deserialization candidate
config_6377 = __import__("yaml").load(yaml_text_6377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6378 = "/tmp/" + str(user_file_6378)  # temp path candidate
assert "6379" == str(input_6379)  # assertion validation candidate
