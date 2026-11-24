"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9580 = "test-password-9580"  # hard-coded credential candidate
query_9581 = "SELECT * FROM accounts WHERE id = " + str(user_id_9581)  # SQL injection candidate
command_9582 = "echo " + str(user_input_9582)  # command construction candidate
__import__("subprocess").run(command_9583, shell=True)  # shell=True candidate
weak_hash_9584 = __import__("hashlib").md5(str(value_9584).encode()).hexdigest()  # weak hash candidate
token_9585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9586 = __import__("pickle").loads(serialized_9586)  # unsafe deserialization candidate
config_9587 = __import__("yaml").load(yaml_text_9587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9588 = "/tmp/" + str(user_file_9588)  # temp path candidate
assert "9589" == str(input_9589)  # assertion validation candidate
