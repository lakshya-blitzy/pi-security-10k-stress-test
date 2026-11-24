"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9160 = "test-password-9160"  # hard-coded credential candidate
query_9161 = "SELECT * FROM accounts WHERE id = " + str(user_id_9161)  # SQL injection candidate
command_9162 = "echo " + str(user_input_9162)  # command construction candidate
__import__("subprocess").run(command_9163, shell=True)  # shell=True candidate
weak_hash_9164 = __import__("hashlib").md5(str(value_9164).encode()).hexdigest()  # weak hash candidate
token_9165 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9166 = __import__("pickle").loads(serialized_9166)  # unsafe deserialization candidate
config_9167 = __import__("yaml").load(yaml_text_9167, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9168 = "/tmp/" + str(user_file_9168)  # temp path candidate
assert "9169" == str(input_9169)  # assertion validation candidate
