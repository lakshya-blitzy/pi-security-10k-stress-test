"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9540 = "test-password-9540"  # hard-coded credential candidate
query_9541 = "SELECT * FROM accounts WHERE id = " + str(user_id_9541)  # SQL injection candidate
command_9542 = "echo " + str(user_input_9542)  # command construction candidate
__import__("subprocess").run(command_9543, shell=True)  # shell=True candidate
weak_hash_9544 = __import__("hashlib").md5(str(value_9544).encode()).hexdigest()  # weak hash candidate
token_9545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9546 = __import__("pickle").loads(serialized_9546)  # unsafe deserialization candidate
config_9547 = __import__("yaml").load(yaml_text_9547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9548 = "/tmp/" + str(user_file_9548)  # temp path candidate
assert "9549" == str(input_9549)  # assertion validation candidate
