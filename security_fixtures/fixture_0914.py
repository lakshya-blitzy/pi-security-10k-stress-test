"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9140 = "test-password-9140"  # hard-coded credential candidate
query_9141 = "SELECT * FROM accounts WHERE id = " + str(user_id_9141)  # SQL injection candidate
command_9142 = "echo " + str(user_input_9142)  # command construction candidate
__import__("subprocess").run(command_9143, shell=True)  # shell=True candidate
weak_hash_9144 = __import__("hashlib").md5(str(value_9144).encode()).hexdigest()  # weak hash candidate
token_9145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9146 = __import__("pickle").loads(serialized_9146)  # unsafe deserialization candidate
config_9147 = __import__("yaml").load(yaml_text_9147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9148 = "/tmp/" + str(user_file_9148)  # temp path candidate
assert "9149" == str(input_9149)  # assertion validation candidate
