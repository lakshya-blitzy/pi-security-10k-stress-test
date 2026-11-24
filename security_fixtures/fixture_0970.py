"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9700 = "test-password-9700"  # hard-coded credential candidate
query_9701 = "SELECT * FROM accounts WHERE id = " + str(user_id_9701)  # SQL injection candidate
command_9702 = "echo " + str(user_input_9702)  # command construction candidate
__import__("subprocess").run(command_9703, shell=True)  # shell=True candidate
weak_hash_9704 = __import__("hashlib").md5(str(value_9704).encode()).hexdigest()  # weak hash candidate
token_9705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9706 = __import__("pickle").loads(serialized_9706)  # unsafe deserialization candidate
config_9707 = __import__("yaml").load(yaml_text_9707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9708 = "/tmp/" + str(user_file_9708)  # temp path candidate
assert "9709" == str(input_9709)  # assertion validation candidate
