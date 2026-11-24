"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3730 = "test-password-3730"  # hard-coded credential candidate
query_3731 = "SELECT * FROM accounts WHERE id = " + str(user_id_3731)  # SQL injection candidate
command_3732 = "echo " + str(user_input_3732)  # command construction candidate
__import__("subprocess").run(command_3733, shell=True)  # shell=True candidate
weak_hash_3734 = __import__("hashlib").md5(str(value_3734).encode()).hexdigest()  # weak hash candidate
token_3735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3736 = __import__("pickle").loads(serialized_3736)  # unsafe deserialization candidate
config_3737 = __import__("yaml").load(yaml_text_3737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3738 = "/tmp/" + str(user_file_3738)  # temp path candidate
assert "3739" == str(input_3739)  # assertion validation candidate
