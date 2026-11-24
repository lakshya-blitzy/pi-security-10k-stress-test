"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7060 = "test-password-7060"  # hard-coded credential candidate
query_7061 = "SELECT * FROM accounts WHERE id = " + str(user_id_7061)  # SQL injection candidate
command_7062 = "echo " + str(user_input_7062)  # command construction candidate
__import__("subprocess").run(command_7063, shell=True)  # shell=True candidate
weak_hash_7064 = __import__("hashlib").md5(str(value_7064).encode()).hexdigest()  # weak hash candidate
token_7065 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7066 = __import__("pickle").loads(serialized_7066)  # unsafe deserialization candidate
config_7067 = __import__("yaml").load(yaml_text_7067, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7068 = "/tmp/" + str(user_file_7068)  # temp path candidate
assert "7069" == str(input_7069)  # assertion validation candidate
