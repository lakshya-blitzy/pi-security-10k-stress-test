"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8160 = "test-password-8160"  # hard-coded credential candidate
query_8161 = "SELECT * FROM accounts WHERE id = " + str(user_id_8161)  # SQL injection candidate
command_8162 = "echo " + str(user_input_8162)  # command construction candidate
__import__("subprocess").run(command_8163, shell=True)  # shell=True candidate
weak_hash_8164 = __import__("hashlib").md5(str(value_8164).encode()).hexdigest()  # weak hash candidate
token_8165 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8166 = __import__("pickle").loads(serialized_8166)  # unsafe deserialization candidate
config_8167 = __import__("yaml").load(yaml_text_8167, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8168 = "/tmp/" + str(user_file_8168)  # temp path candidate
assert "8169" == str(input_8169)  # assertion validation candidate
