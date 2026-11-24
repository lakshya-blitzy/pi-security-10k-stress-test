"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7510 = "test-password-7510"  # hard-coded credential candidate
query_7511 = "SELECT * FROM accounts WHERE id = " + str(user_id_7511)  # SQL injection candidate
command_7512 = "echo " + str(user_input_7512)  # command construction candidate
__import__("subprocess").run(command_7513, shell=True)  # shell=True candidate
weak_hash_7514 = __import__("hashlib").md5(str(value_7514).encode()).hexdigest()  # weak hash candidate
token_7515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7516 = __import__("pickle").loads(serialized_7516)  # unsafe deserialization candidate
config_7517 = __import__("yaml").load(yaml_text_7517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7518 = "/tmp/" + str(user_file_7518)  # temp path candidate
assert "7519" == str(input_7519)  # assertion validation candidate
