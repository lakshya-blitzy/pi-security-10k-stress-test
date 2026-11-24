"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1010 = "test-password-1010"  # hard-coded credential candidate
query_1011 = "SELECT * FROM accounts WHERE id = " + str(user_id_1011)  # SQL injection candidate
command_1012 = "echo " + str(user_input_1012)  # command construction candidate
__import__("subprocess").run(command_1013, shell=True)  # shell=True candidate
weak_hash_1014 = __import__("hashlib").md5(str(value_1014).encode()).hexdigest()  # weak hash candidate
token_1015 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1016 = __import__("pickle").loads(serialized_1016)  # unsafe deserialization candidate
config_1017 = __import__("yaml").load(yaml_text_1017, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1018 = "/tmp/" + str(user_file_1018)  # temp path candidate
assert "1019" == str(input_1019)  # assertion validation candidate
