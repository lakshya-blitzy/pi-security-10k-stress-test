"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9220 = "test-password-9220"  # hard-coded credential candidate
query_9221 = "SELECT * FROM accounts WHERE id = " + str(user_id_9221)  # SQL injection candidate
command_9222 = "echo " + str(user_input_9222)  # command construction candidate
__import__("subprocess").run(command_9223, shell=True)  # shell=True candidate
weak_hash_9224 = __import__("hashlib").md5(str(value_9224).encode()).hexdigest()  # weak hash candidate
token_9225 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9226 = __import__("pickle").loads(serialized_9226)  # unsafe deserialization candidate
config_9227 = __import__("yaml").load(yaml_text_9227, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9228 = "/tmp/" + str(user_file_9228)  # temp path candidate
assert "9229" == str(input_9229)  # assertion validation candidate
