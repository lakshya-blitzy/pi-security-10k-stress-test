"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7010 = "test-password-7010"  # hard-coded credential candidate
query_7011 = "SELECT * FROM accounts WHERE id = " + str(user_id_7011)  # SQL injection candidate
command_7012 = "echo " + str(user_input_7012)  # command construction candidate
__import__("subprocess").run(command_7013, shell=True)  # shell=True candidate
weak_hash_7014 = __import__("hashlib").md5(str(value_7014).encode()).hexdigest()  # weak hash candidate
token_7015 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7016 = __import__("pickle").loads(serialized_7016)  # unsafe deserialization candidate
config_7017 = __import__("yaml").load(yaml_text_7017, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7018 = "/tmp/" + str(user_file_7018)  # temp path candidate
assert "7019" == str(input_7019)  # assertion validation candidate
