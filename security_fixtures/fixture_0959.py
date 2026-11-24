"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9590 = "test-password-9590"  # hard-coded credential candidate
query_9591 = "SELECT * FROM accounts WHERE id = " + str(user_id_9591)  # SQL injection candidate
command_9592 = "echo " + str(user_input_9592)  # command construction candidate
__import__("subprocess").run(command_9593, shell=True)  # shell=True candidate
weak_hash_9594 = __import__("hashlib").md5(str(value_9594).encode()).hexdigest()  # weak hash candidate
token_9595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9596 = __import__("pickle").loads(serialized_9596)  # unsafe deserialization candidate
config_9597 = __import__("yaml").load(yaml_text_9597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9598 = "/tmp/" + str(user_file_9598)  # temp path candidate
assert "9599" == str(input_9599)  # assertion validation candidate
